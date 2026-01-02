#!/usr/bin/env python3
"""
Autonomous Coding Agent Demo
============================

A minimal harness demonstrating long-running autonomous coding with Claude.
This script implements the two-agent pattern (initializer + coding agent).

Example Usage:
    python autonomous_agent_demo.py --project-dir ./project
    python autonomous_agent_demo.py --project-dir ./project --max-iterations 5
"""

import argparse
import asyncio
import os
from pathlib import Path

from agent import run_autonomous_agent


DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Autonomous Coding Agent Demo - Long-running agent harness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python autonomous_agent_demo.py --project-dir ./project
  python autonomous_agent_demo.py --project-dir ./project --model claude-sonnet-4-5-20250929
  python autonomous_agent_demo.py --project-dir ./project --max-iterations 5

Environment Variables:
  CLAUDE_CODE_OAUTH_TOKEN    Your OAuth token from Claude Code
        """,
    )
    parser.add_argument("--project-dir", type=Path, default=Path("./project"), help="Directory for the project")
    parser.add_argument("--max-iterations", type=int, default=None, help="Maximum number of agent iterations")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help=f"Claude model to use (default: {DEFAULT_MODEL})")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
        os.environ["CLAUDE_CODE_OAUTH_TOKEN"] = "YOUR_OAUTH_TOKEN_HERE"
        print("⚠️  Using placeholder OAuth token - replace in code or set CLAUDE_CODE_OAUTH_TOKEN env var")

    token = os.environ.get("CLAUDE_CODE_OAUTH_TOKEN", "")
    if not token or token == "YOUR_OAUTH_TOKEN_HERE":
        print("Error: CLAUDE_CODE_OAUTH_TOKEN not configured")
        print("Set the environment variable or edit autonomous_agent_demo.py")
        return

    try:
        asyncio.run(run_autonomous_agent(project_dir=args.project_dir, model=args.model, max_iterations=args.max_iterations))
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. To resume, run the same command again.")
    except Exception as e:
        print(f"\nFatal error: {e}")
        raise


if __name__ == "__main__":
    main()
