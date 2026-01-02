"""
Agent Session Logic
===================

Core agent interaction functions for running autonomous coding sessions.
"""

import asyncio
from pathlib import Path
from typing import Optional

from claude_code_sdk import ClaudeSDKClient

from client import create_client
from progress import print_session_header, print_progress_summary
from prompts import get_initializer_prompt, get_coding_prompt, copy_spec_to_project


AUTO_CONTINUE_DELAY_SECONDS = 3


async def run_agent_session(client: ClaudeSDKClient, message: str, project_dir: Path) -> tuple[str, str]:
    print("Sending prompt to Claude Agent SDK...\n")
    try:
        await client.query(message)
        response_text = ""
        async for msg in client.receive_response():
            msg_type = type(msg).__name__
            if msg_type == "AssistantMessage" and hasattr(msg, "content"):
                for block in msg.content:
                    block_type = type(block).__name__
                    if block_type == "TextBlock" and hasattr(block, "text"):
                        response_text += block.text
                        print(block.text, end="", flush=True)
                    elif block_type == "ToolUseBlock" and hasattr(block, "name"):
                        print(f"\n[Tool: {block.name}]", flush=True)
                        if hasattr(block, "input"):
                            input_str = str(block.input)
                            print(f"   Input: {input_str[:200]}..." if len(input_str) > 200 else f"   Input: {input_str}", flush=True)
            elif msg_type == "UserMessage" and hasattr(msg, "content"):
                for block in msg.content:
                    if type(block).__name__ == "ToolResultBlock":
                        result_content = getattr(block, "content", "")
                        is_error = getattr(block, "is_error", False)
                        if "blocked" in str(result_content).lower():
                            print(f"   [BLOCKED] {result_content}", flush=True)
                        elif is_error:
                            print(f"   [Error] {str(result_content)[:500]}", flush=True)
                        else:
                            print("   [Done]", flush=True)
        print("\n" + "-" * 70 + "\n")
        return "continue", response_text
    except Exception as e:
        print(f"Error during agent session: {e}")
        return "error", str(e)


async def run_autonomous_agent(project_dir: Path, model: str, max_iterations: Optional[int] = None) -> None:
    print("\n" + "=" * 70)
    print("  AUTONOMOUS CODING AGENT")
    print("=" * 70)
    print(f"\nProject directory: {project_dir}")
    print(f"Model: {model}")
    print(f"Max iterations: {max_iterations}" if max_iterations else "Max iterations: Unlimited")
    print()

    project_dir.mkdir(parents=True, exist_ok=True)
    tests_file = project_dir / "feature_list.json"
    is_first_run = not tests_file.exists()

    if is_first_run:
        print("Fresh start - will use initializer agent\n")
        print("=" * 70)
        print("  NOTE: First session may take 10-20+ minutes")
        print("  The agent is analyzing specs and generating feature tests.")
        print("=" * 70 + "\n")
        copy_spec_to_project(project_dir)
    else:
        print("Continuing existing project")
        print_progress_summary(project_dir)

    iteration = 0
    while True:
        iteration += 1
        if max_iterations and iteration > max_iterations:
            print(f"\nReached max iterations ({max_iterations})")
            break

        print_session_header(iteration, is_first_run)
        client = create_client(project_dir, model)
        prompt = get_initializer_prompt() if is_first_run else get_coding_prompt()
        if is_first_run:
            is_first_run = False

        async with client:
            status, response = await run_agent_session(client, prompt, project_dir)

        if status == "continue":
            print(f"\nAgent will auto-continue in {AUTO_CONTINUE_DELAY_SECONDS}s...")
            print_progress_summary(project_dir)
            await asyncio.sleep(AUTO_CONTINUE_DELAY_SECONDS)
        elif status == "error":
            print("\nSession encountered an error, retrying...")
            await asyncio.sleep(AUTO_CONTINUE_DELAY_SECONDS)

        if max_iterations is None or iteration < max_iterations:
            print("\nPreparing next session...\n")
            await asyncio.sleep(1)

    print("\n" + "=" * 70)
    print("  SESSION COMPLETE")
    print("=" * 70)
    print(f"\nProject directory: {project_dir}")
    print_progress_summary(project_dir)
    print("\n" + "-" * 70)
    print("  TO RUN THE GENERATED APPLICATION:")
    print("-" * 70)
    print(f"\n  cd {project_dir.resolve()}")
    print("  ./init.sh")
    print("\n  Then open http://localhost:3000")
    print("-" * 70)
    print("\nDone!")
