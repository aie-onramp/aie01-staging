# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the AI Engineer Onramp Course (AIEO1) repository - a structured learning environment for building production LLM applications. The repository is organized by sessions, each focusing on different aspects of AI-assisted development and LLM application deployment.

## Repository Structure

- **Session_01_LLM_APIs_&_AI-Assisted_Development/**: Python environment with Jupyter notebooks for OpenAI API exploration
- **Session_02_Front_End_UI_Development_&_Deployment_of_LLM_Applications/**: Frontend development workflows and v0.dev integration
- **Session_03_Back_End_Web_App_Development_&_Deployment_of_LLM_Applications/**: FastAPI backend development with HotMessCoach example app

## Technology Stack

- **Package Management**: uv (Astral)
- **Python**: Jupyter notebooks, FastAPI backends
- **Frontend**: Next.js (generated via v0.dev)
- **LLM APIs**: OpenAI GPT models
- **Backend Framework**: FastAPI + Streamlit variants
- **Deployment**: Vercel for both frontend and backend
- **Version Control**: Git with GitFlow methodology

## Common Commands

### Python Environment Setup

```bash
# Install dependencies using uv
uv sync

# Activate virtual environment (if needed)
source .venv/bin/activate  # Linux/Mac
```

### Running Session 1 (Jupyter Notebooks)

```bash
# Launch Jupyter from Session_01 directory
cd Session_01_LLM_APIs_&_AI-Assisted_Development
jupyter notebook OpenAI_playground_for_developers.ipynb
```

### Running Session 3 (FastAPI Backend)

```bash
# Navigate to HotMessCoach backend
cd "Session_03_Back_End_Web_App_Development_&_Deployment_of_LLM_Applications/HotMessCoach"

# Install additional dependencies for LLM variants
pip install fastapi "uvicorn[standard]" python-dotenv openai streamlit

# Run different app variants:

# STEP 0: Simple HTML FastAPI app
uvicorn backend.STEP0_app_html:app --reload --host 0.0.0.0 --port 8000

# STEP 1: LLM backend (no UI, Swagger at /docs)
uvicorn backend.STEP1_app_llm:app --reload --host 0.0.0.0 --port 8000

# STEP 2: LLM backend with minimal HTML UI
uvicorn backend.STEP2_app_llm_html:app --reload --host 0.0.0.0 --port 8000

# STEP 3: Streamlit chat UI
streamlit run backend/STEP3_app_llm_st.py

# STEP 4: Streamlit with document upload (PDF/CSV)
pip install PyPDF2 pandas
streamlit run backend/STEP4_app_llm_st_doc.py
```

### Testing Session 3 Endpoints

```bash
# Test FastAPI /chat endpoint (STEP1, STEP2)
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "I feel overwhelmed with my tasks"}'

# Access interactive API docs (FastAPI variants)
# Open browser to: http://localhost:8000/docs

# Check running services
lsof -i :8000  # FastAPI
lsof -i :8501  # Streamlit
```

### Deploying Session 3 to Vercel

```bash
# Install Vercel CLI (first time only)
npm install -g vercel

# Deploy from HotMessCoach directory
cd "Session_03_Back_End_Web_App_Development_&_Deployment_of_LLM_Applications/HotMessCoach"
vercel

# Set environment variables in Vercel dashboard
# Project Settings → Environment Variables → Add OPENAI_API_KEY

# Important: Rename your chosen STEP file to app.py before deploying
# OR update vercel.json to point to your specific STEP file
```

## Git Workflow

This repository follows **GitFlow** methodology with some customizations for course materials.

### Working with Upstream Course Materials

```bash
# Initial setup - add course repo as upstream
git remote add upstream git@github.com:AI-Maker-Space/AIEO1.git
git remote -v

# Pull course materials
git pull upstream main --allow-unrelated-histories

# Push to your own repo
git push origin main
```

### Feature Branch Workflow

```bash
# Create feature branch from develop
git switch develop
git pull origin develop
git switch -c feature/your-feature-name

# Work on your feature
git add .
git commit -m "Descriptive commit message"
git push origin feature/your-feature-name

# Merge back to develop
git switch develop
git merge --no-ff feature/your-feature-name
git push origin develop
```

### Release Workflow

```bash
# Create release branch
git switch develop
git switch -c release/1.2.0
git push -u origin release/1.2.0

# Merge to main and tag
git switch main
git merge --no-ff release/1.2.0
git tag -a v1.2.0 -m "Release version 1.2.0"
git push origin main
git push origin v1.2.0

# Merge back to develop
git switch develop
git merge --no-ff release/1.2.0
git push origin develop

# Clean up release branch
git branch -d release/1.2.0
git push origin --delete release/1.2.0
```

## Code Style & Conventions

### Naming Conventions
- **Variables**: camelCase
- **Components & Classes**: PascalCase
- **Constants**: UPPER_SNAKE_CASE

### File Organization
- One clear entry point per application (main.tsx, api.py, etc.)
- Descriptive folder names (/components, /hooks, /services)
- Each component in its own file
- Use absolute paths for imports (avoid deep relative paths like ../../../)
- Limit file size to ~300 lines where practical

## Environment Variables

LLM applications require OpenAI API key:

```bash
export OPENAI_API_KEY=sk-...
```

For persistent configuration, create a `.env` file:
```
OPENAI_API_KEY=your-key-here
```

## Session-Specific Architecture

### Session 1: LLM API Development
- Python-based Jupyter notebooks for interactive API exploration
- Uses `python-dotenv` for API key management
- Dependencies defined in `pyproject.toml`

### Session 2: Frontend Development
- Frontend apps generated using v0.dev (AI-powered UI generation)
- Next.js/React applications
- Deployed to Vercel with CI/CD pipeline
- Focus on multi-agent workflow using feature branches

### Session 3: Backend Development (HotMessCoach)

The HotMessCoach application demonstrates progressive complexity through five self-contained variants:

| STEP | Technology | Use Case | Access Points |
|------|------------|----------|---------------|
| **STEP0** | FastAPI + HTML | Prove FastAPI setup works | `http://localhost:8000` |
| **STEP1** | FastAPI + LLM | API-first backend (no UI) | `http://localhost:8000/docs` (Swagger) |
| **STEP2** | FastAPI + LLM + HTML | Minimal embedded UI | `http://localhost:8000` + `/docs` |
| **STEP3** | Streamlit + LLM | Chat interface | Auto-opens browser |
| **STEP4** | Streamlit + LLM + Docs | PDF/CSV analysis | Auto-opens browser |

**Progressive Complexity Pattern:**
1. Start with STEP0 to verify FastAPI installation and routing
2. Add LLM capabilities in STEP1 (test via Swagger UI at `/docs`)
3. Add basic UI in STEP2 for human interaction
4. Upgrade to Streamlit in STEP3 for better UX
5. Add document upload/analysis in STEP4

All variants are completely independent - each can run without modifying others. This supports parallel development and A/B testing different approaches.

## Deployment

### Backend Deployment (Vercel)
- Uses `vercel.json` for configuration
- Ensure environment variables (OPENAI_API_KEY) are set in Vercel dashboard
- FastAPI apps deploy as serverless functions

### Frontend Deployment (Vercel)
- Push to GitHub triggers automatic deployment
- Configure project in Vercel dashboard
- Next.js apps deploy with zero-config

## Converting GitHub Notebooks to Google Colab

To make notebooks shareable on Google Colab:
```
# Change from:
https://github.com/username/repo/blob/main/notebook.ipynb

# To:
https://colab.research.google.com/github/username/repo/blob/main/notebook.ipynb
```

## Dependency Management Strategy

**Repository Level:**
- Use `uv sync` for initial repository setup (manages `.venv` and shared dependencies)

**Session Level:**
- Use `pip install` for session-specific dependencies (FastAPI, Streamlit, etc.)
- Session 3 requires manual installation as dependencies vary by STEP variant

**Why Both?**
- Repository-level `uv` ensures consistent Python environment across all sessions
- Session-level `pip` allows students to install only what they need for specific exercises

## Troubleshooting

### Session 3 Common Issues

**Missing OpenAI API Key:**
```bash
# Error: "OpenAI API key not found"
# Solution: Set environment variable
export OPENAI_API_KEY=sk-...

# Or create .env file in HotMessCoach directory
echo "OPENAI_API_KEY=sk-..." > .env
```

**Port Already in Use:**
```bash
# Error: "Address already in use"
# Solution: Kill process on port 8000 or 8501
lsof -ti:8000 | xargs kill -9  # FastAPI
lsof -ti:8501 | xargs kill -9  # Streamlit

# Or use different port
uvicorn backend.STEP1_app_llm:app --reload --port 8001
```

**Vercel Deployment Fails:**
```bash
# Error: "Could not find app.py"
# Solution: Rename your STEP file
cp backend/STEP1_app_llm.py app.py

# OR update vercel.json:
# Change "backend/app.py" to "backend/STEP1_app_llm.py"
```

**PDF Extraction Not Working:**
```bash
# Error: "No module named 'PyPDF2'"
# Solution: Install document processing dependencies
pip install PyPDF2 pandas
```

**CORS Errors (when connecting v0 frontend):**
```python
# Add to FastAPI app (STEP1, STEP2)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Key Development Patterns

1. **Iterative Development**: Start with simple variants (STEP0) and progressively add complexity
2. **GitFlow Discipline**: Always work on feature branches, never commit directly to main
3. **AI-Assisted Development**: Use Cursor/AI tools to generate and refactor code
4. **Documentation-First**: Each session has detailed README with instructions
5. **Environment Isolation**: Use uv for reproducible Python environments
