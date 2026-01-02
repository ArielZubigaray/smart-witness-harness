## YOUR ROLE - INITIALIZER AGENT (Session 1 of Many)

You are the FIRST agent in a long-running autonomous development process.
Your job is to set up the foundation for all future coding agents.

### FIRST: Read the Project Specification

Start by reading `app_spec.txt` in your working directory. This file contains
the complete specification for what you need to build.

### CRITICAL FIRST TASK: Create feature_list.json

Based on `app_spec.txt`, create a file called `feature_list.json` with 70 detailed
end-to-end test cases.

**Format:**
```json
[
  {
    "category": "functional",
    "description": "Brief description of the feature",
    "steps": [
      "Step 1: Navigate to relevant page",
      "Step 2: Perform action",
      "Step 3: Verify expected result"
    ],
    "passes": false
  }
]
```

**Feature Categories for Smart Witness:**
1. Backend API (FastAPI): ~20 features
2. Mock Device Webapp: ~15 features
3. Mock Telegram Webapp: ~15 features
4. Dashboard: ~15 features
5. Integration & Style: ~5 features

**CRITICAL:** Features can ONLY be marked as passing, never removed or edited.

### SECOND TASK: Create init.sh

Create a script that starts all services:
- Backend (FastAPI): http://localhost:8000
- Mock Device: http://localhost:3001
- Mock Telegram: http://localhost:3002
- Dashboard: http://localhost:3000

### THIRD TASK: Initialize Git

Commit: feature_list.json, init.sh, README.md

### FOURTH TASK: Create Project Structure

- backend/ - FastAPI application
- mock-device-webapp/ - React app simulating ESP32-CAM
- mock-telegram-webapp/ - React app simulating Telegram
- dashboard/ - React app for user interface

### ENDING THIS SESSION

1. Commit all work
2. Update claude-progress.txt
3. Leave the environment clean

---

**Remember:** Focus on getting each feature working correctly. Quality over quantity.
