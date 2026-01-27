# LLM Engineering Mastery Journey

**Complete 25-week structured learning path for mastering LLM Engineering from basics to multi-platform mastery**

This repository is a comprehensive, hands-on exploration of modern Large Language Model (LLM) engineering, tooling, and real-world application patterns. It accompanies **Ed Donner's "LLM Engineering: Master AI, Large Language Models & Agents"** Udemy course and provides a structured roadmap to build practical skills across multiple platforms and languages.

---

## 🎯 Objectives

* Master LLM engineering from foundations to advanced multi-platform applications
* Build practical skills with **OpenAI** and **Azure OpenAI** (dual provider support from Week 1)
* Implement LLM applications across **multiple languages**: Python, Go, Node.js, Angular, React, Next.js, .NET
* Master advanced patterns: Chain-of-Thought (CoT), ReAct, Reasoning Patterns, RAG, Agents
* Practice retrieval, fine-tuning, function calling, and agent patterns
* Compare frameworks (LangChain, LangGraph, OpenAI Agent SDK, Azure Agent SDK) pragmatically
* Establish reproducible, evaluable experiment workflows
* Develop production-ready, full-stack LLM applications

## 📦 Learning Path Overview

**25-Week Structured Journey:**
- **Weeks 1-5**: Foundations (Python, OpenAI + Azure OpenAI)
- **Weeks 6-10**: Intermediate (Add Go, Node.js)
- **Weeks 11-15**: Advanced (Add React, Angular, Next.js)
- **Weeks 16-20**: Production (Add .NET Web API, Blazor, Aspire)
- **Weeks 21-25**: Mastery (All platforms + frameworks)

**Key Deep Dives:**
- **Week 3**: Chain-of-Thought (CoT) - Complete patterns and best practices
- **Week 5**: ReAct (Reasoning + Acting) - Full implementation guide
- **Week 14**: Reasoning Patterns - All patterns (CoT, ReAct, ToT, PoT, etc.)
- **Week 21**: Azure OpenAI Deep Dive - Multi-provider patterns
- **Week 22**: Multi-Language Mastery - Python, Go, Node.js
- **Week 23**: Frontend Mastery - React, Angular, Next.js
- **Week 24**: .NET Mastery - Aspire, Web API, Blazor
- **Week 25**: Agentic Frameworks - LangChain, LangGraph, SDKs

**Multi-Platform Support:**
- **Providers**: OpenAI + Azure OpenAI (dual support from Week 1)
- **Languages**: Python, Go, Node.js, Angular, React, Next.js, .NET Aspire, .NET Web API, .NET Blazor
- **Frameworks**: LangChain, LangGraph, OpenAI Agent SDK, Azure Agent SDK

> **Note**: Detailed weekly guides are in [`docs/weeks/`](docs/weeks/) - each week contains day-by-day breakdowns, exercises, and deliverables.

## 🧪 Current Status

✅ **25-Week Learning Plan Complete** - All weekly guides structured and ready  
✅ **Multi-Platform Support** - OpenAI + Azure OpenAI from Week 1  
✅ **Multi-Language Support** - Progressive introduction across 9 platforms  
✅ **Deep Dives** - 8 dedicated deep dive weeks (CoT, ReAct, Reasoning, Platforms, Frameworks)  
🚧 **In Progress** - Code implementation as you learn (planning structure complete)

**Ready to Start**: Begin with [`docs/learning-plan.md`](docs/learning-plan.md) and [`docs/weeks/Week1.md`](docs/weeks/Week1.md)

## References

> 1. <https://docs.astral.sh/uv/getting-started/installation/#standalone-installer>

## ⚡ Quick Start (Local)

```powershell
# Clone (adjust URL if you forked)
git clone <YOUR_FORK_URL> llm-engineering-learning
cd llm-engineering-learning

# Install uv (if not already installed)
# Using standalone installer (recommended):
#   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Or via pip:
#   pip install uv

# Sync environment and install dependencies
uv sync

# Set up API keys (create .env file)
# OpenAI: https://platform.openai.com/api-keys
# Azure OpenAI: https://portal.azure.com → Create Azure OpenAI resource
# Copy .env.example to .env and fill in your keys

# (Optional) Run diagnostics to verify setup
cd notebooks/01-setup && uv run python diagnostics.py

# (Optional) Smoke test logging + metrics modules
uv run python -m eval.log_utils
uv run python -m eval.metrics
```

**Start Learning**: Open [`docs/learning-plan.md`](docs/learning-plan.md) for the master guide, then begin with [`docs/weeks/Week1.md`](docs/weeks/Week1.md)

## 📚 Primary Course Reference

Studying: "LLM Engineering: Master AI, Large Language Models & Agents" by Ed Donner on Udemy.
Course link: <https://www.udemy.com/course/llm-engineering-master-ai-and-large-language-models>

Supplemented with official docs, open papers, and community benchmarks.

## 🗺 25-Week Learning Roadmap

### Foundation Phase (Weeks 1-5)
1. **Week 1**: Environment setup, API keys, dual provider (OpenAI + Azure OpenAI)
2. **Week 2**: Python & data handling, text chunking
3. **Week 3**: Prompt engineering + **Chain-of-Thought (CoT) Deep Dive**
4. **Week 4**: Web scraping & LLM integration
5. **Week 5**: Multi-agent intro + **ReAct (Reasoning + Acting) Deep Dive**

### Intermediate Phase (Weeks 6-10)
6. **Week 6**: Structured outputs, function calling + **Go intro**
7. **Week 7**: Optimization & performance + **Node.js intro**
8. **Week 8**: Applied mini projects (multi-language)
9. **Week 9**: Autonomous/planning agents
10. **Week 10**: Deployment & scaling

### Advanced Phase (Weeks 11-15)
11. **Week 11**: Capstone build + **React intro**
12. **Week 12**: Review & deep dives
13. **Week 13**: Advanced RAG techniques + **Angular intro**
14. **Week 14**: **Reasoning Patterns Deep Dive** (all patterns)
15. **Week 15**: Multi-agent systems + **Next.js intro**

### Production Phase (Weeks 16-20)
16. **Week 16**: Production optimization + **.NET Web API intro**
17. **Week 17**: Advanced evaluation
18. **Week 18**: Specialized applications + **Blazor intro**
19. **Week 19**: Research & experimentation + **.NET Aspire intro**
20. **Week 20**: Mastery & beyond (all platforms)

### Mastery Phase (Weeks 21-25)
21. **Week 21**: **Azure OpenAI Deep Dive** + multi-provider patterns
22. **Week 22**: **Multi-Language Mastery** (Python, Go, Node.js)
23. **Week 23**: **Frontend Mastery** (React, Angular, Next.js)
24. **Week 24**: **.NET Mastery** (Aspire, Web API, Blazor)
25. **Week 25**: **Agentic Frameworks Mastery** (LangChain, LangGraph, SDKs)

**See** [`docs/learning-plan.md`](docs/learning-plan.md) **for the complete master guide with all 25 weeks detailed.**

## 🧱 Repository Structure

```text
├─ .backup/            # Archived legacy files (environment.yml, requirements.txt)
├─ agents/             # Agent & tool orchestration experiments
├─ data/               # Sample corpora / synthetic sets (non-sensitive)
│  ├─ raw/             # Unprocessed source data
│  └─ processed/       # Cleaned / chunked / vectorizable data
├─ docs/               # Documentation, guides, and decision logs
│  ├─ images/          # Documentation images
│  ├─ reports/         # Generated reports and diagnostics
│  ├─ retros/          # Retrospective notes and learnings
│  ├─ weeks/           # 25 weekly learning guides (Week1.md - Week25.md)
│  └─ learning-plan.md # Master 25-week learning plan
├─ eval/               # Evaluation scripts, metrics, and experiment logging
├─ notebooks/          # Exploratory Jupyter notebooks & analysis
│  └─ 01-setup/        # Setup diagnostics and troubleshooting
├─ prompts/            # Prompt templates & variant experiments
├─ rag/                # Retrieval prototypes (index builders, query flows)
├─ scripts/            # Utility CLIs (ingest, batch eval, cost reporting)
├─ src/                # Source code modules (when needed)
├─ tools/              # Custom tool / function call definitions
├─ .gitignore          # Git ignore rules
├─ LICENSE             # Project license
├─ lychee.toml         # Link checker configuration
├─ pyproject.toml      # Project dependencies and metadata (uv)
├─ uv.lock             # Locked dependency versions (uv)
└─ README.md            # This file
```

## 🛠 Environment Setup

This project uses [`uv`](https://github.com/astral-sh/uv) for fast dependency management and virtual environment handling.

### Installing uv

**PowerShell (Windows):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Alternative (via pip):**
```powershell
pip install uv
```

### Setup Steps

```powershell
# Optional: Suppress cross-drive hardlink warnings (if expected)
$Env:UV_LINK_MODE = "copy"

# 1. Sync environment (creates .venv and installs all dependencies from pyproject.toml)
uv sync

# 2. Use uv run prefix (no activation needed - recommended)
uv run python -m eval.log_utils

# 3. (Optional) Activate the virtual environment manually if needed
# . .venv/Scripts/Activate.ps1  # (bash/zsh: source .venv/bin/activate)

# 4. Provide your API key (either set env var or create .env)
setx OPENAI_API_KEY "sk-..."  # (bash/zsh: export OPENAI_API_KEY="sk-...")
# Then restart the shell so setx takes effect.
```

### Run Diagnostics

Verify your environment is properly configured by running the diagnostics script:

```powershell
cd notebooks/01-setup && uv run python diagnostics.py
```

This will check:
- System information (OS, RAM, disk space)
- Git repository configuration
- Environment file (.env) and API keys
- Python environment (virtualenv/conda)
- Required package installations
- Network connectivity

A `report.txt` file will be generated in `notebooks/01-setup/` with detailed diagnostics.

### (Optional) Jupyter Smoke Test

```powershell
uv run jupyter lab
```

Close it after confirming it opens. See `notebooks/01-setup/` for setup diagnostics and troubleshooting notebooks.

### Updating Dependencies

```powershell
# Update dependencies to latest compatible versions
uv sync --upgrade

# Add a new dependency
uv add package-name

# Remove a dependency
uv remove package-name
```


## 🔍 Evaluation Philosophy

* Prefer small, fast feedback loops
* Track: latency, token usage, factuality, relevance, refusal rate
* Store experiment metadata (prompt hash, model, temperature, dataset slice)
* Re-run baselines after significant changes

## ✅ Progress Log

| Date | Area | Activity | Notes |
|------|------|----------|-------|
| 2025-08-18 | Init | Enhanced README | Structured plan & roadmap |
| YYYY-MM-DD | RAG | Build first vector index |  |
| YYYY-MM-DD | Eval | Add basic factuality check |  |

## 📘 Key Resources (Growing List)

* OpenAI & Anthropic model docs
* LlamaIndex, LangChain, Semantic Kernel docs
* Papers: RAG triad (retrieval quality, generation control, evaluation), Toolformer, Self-Ask
* Evaluation frameworks: RAGAS, TruLens, LM Evaluation Harness

## 📚 Comprehensive Learning Plan

For the complete **25-week structured learning path**, daily workflow patterns, metrics schema, multi-platform support, and detailed weekly guides, see:

- **[`docs/learning-plan.md`](docs/learning-plan.md)** - Master learning plan with overview, quick start, prerequisites, and 25-week table
- **[`docs/weeks/Week1.md`](docs/weeks/Week1.md) through [`docs/weeks/Week25.md`](docs/weeks/Week25.md)** - Detailed day-by-day guides for each week

**Each week includes:**
- Learning objectives
- 5 days × 30 minutes breakdown (2.5 hours/week)
- Practical exercises with success criteria
- Code examples (planned - add as you learn)
- Deep dive sections for key concepts
- Deliverables and reflection templates

## 🔐 Ethics & Safety Notes (Intent)

* Avoid storing or committing sensitive data
* Log only minimal necessary interaction metadata
* Track model + prompt versions for reproducibility

## 🤝 Contributions

Currently a personal learning space—external PRs likely paused until a baseline structure exists.

## 📝 License

See `LICENSE` for details.

---
If you're reading along: suggestions & refinement ideas welcome once core scaffolding ships.

## Development

### Docs quality checks (local)

Run Markdown lint against README and all docs before opening a PR:

```powershell
# From repo root
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"
```

This uses the repository's .markdownlint.json automatically.

### Link check (Lychee)

CI currently checks `README.md` and `docs/**/*.md`. To replicate locally (Docker image mirrors CI action):

```powershell
# List links only (no validation)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest \
 --config lychee.toml --no-progress --dump README.md docs/**/*.md .github/**/*.md

# Validate links (same as CI)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress README.md docs/**/*.md .github/**/*.md
```

If you add markdown elsewhere (e.g. prompt notes), update both:

* `.github/workflows/docs-quality.yml` (lychee args)
* `lychee.toml` (optional path excludes)

#### Excluded links

Certain domains (e.g. private course pages) can return steady 403s to unauthenticated bots. The Udemy course link in the Primary Course Reference section is intentionally excluded in `lychee.toml` via a regex literal to avoid noisy failures:

```toml
exclude = [
 # ...other patterns...
 'https?://www\.udemy\.com/course/llm-engineering-master-ai-and-large-language-models/?'
]
```

Remove that pattern if you want Lychee to re-validate it (may still 403). Keep exclusions minimal so real link rot is caught.

### Manual Docs Quality Workflow

CI runs automatically on PRs and pushes that modify documentation, but you can also trigger it manually:

1. Open GitHub → Actions → "Docs Quality" workflow
2. Click "Run workflow" (no inputs required)
3. View markdownlint + Lychee results; download the `lychee-report` artifact for details

Reason: Manual trigger accelerates iteration when adjusting large batches of links or performing structural renumbering.

### Local Experiment Logging Smoke Test

```powershell
python -m eval.log_utils
python -m eval.metrics
```

Expected: `eval/experiment_log.csv` created and a sample metrics dict printed.

### Consistency Checklist

| Item | Expectation |
|------|-------------|
| Prompts | Stored under `prompts/` with metadata sidecars |
| Experiments | Each new run logged via `log_utils.log_run` |
| Links | New external links validated or excluded intentionally |
| Structure | New folders documented in Repository Structure section |
| Reproducibility | No secrets committed; env handling via `.env` |
