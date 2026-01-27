# Repository Structure (LLM Engineering in Practice)

This repository is a **personal learning workspace** for LLM Engineering. Content is organized to support structured learning, experimentation, and practical implementation across multiple platforms.

## Directory Structure

### Core Learning Content

- **`docs/`**: Documentation, guides, and decision logs
  - `weeks/`: 25 weekly learning guides (Week1.md - Week25.md)
  - `learning-plan.md`: Master 25-week learning plan
  - `reports/`: Generated reports and diagnostics
  - `retros/`: Retrospective notes and learnings

- **`notebooks/`**: Exploratory Jupyter notebooks & analysis
  - Setup diagnostics and troubleshooting
  - Experimentation and prototyping

- **`prompts/`**: Prompt templates & variant experiments
  - Format: `name.prompt.txt` + `name.meta.json` (metadata sidecar)

### Implementation Folders

- **`agents/`**: Agent & tool orchestration experiments
  - Agent loops, reasoning traces, tool registries
  - Supports CoT, ReAct, ToT, PoT, and other reasoning patterns

- **`rag/`**: Retrieval prototypes
  - Index builders, query flows
  - Vector stores, hybrid retrieval strategies

- **`tools/`**: Custom tool / function call definitions
  - Tool schemas (Pydantic or dataclass)
  - Handler functions, safety notes
  - Tool registry for model integration

- **`eval/`**: Evaluation scripts, metrics, and experiment logging
  - Metrics calculators
  - Experiment logs (CSV/JSONL format)
  - Harness scripts

- **`scripts/`**: Utility CLIs
  - Ingest scripts
  - Batch evaluation
  - Cost reporting

- **`src/`**: Source code modules (when needed)
  - Reusable helper functions
  - Shared utilities

### Data & Configuration

- **`data/`**: Sample corpora / synthetic sets (non-sensitive)
  - `raw/`: Unprocessed source data
  - `processed/`: Cleaned / chunked / vectorizable data

- **`source-material/`**: Staging area for raw content
  - **Read-Only**: Never modify or delete files
  - Permanent reference materials
  - Used for migration to educational content (zero-copy policy)

### Infrastructure

- **`.cursor/rules/`**: Cursor IDE rules for AI assistance
- **`.github/`**: GitHub templates, workflows, and copilot instructions
- **`tools/psscripts/`**: PowerShell automation scripts for validation

## Multi-Provider & Multi-Language Support

- **Providers**: All implementations support both OpenAI and Azure OpenAI from Week 1
- **Languages**: Python, Go, Node.js, Angular, React, Next.js, .NET (Aspire, Web API, Blazor)
- **Frameworks**: LangChain, LangGraph, OpenAI Agent SDK, Azure Agent SDK

## File Naming Conventions

- **Prompt Templates**: `name.prompt.txt` + `name.meta.json` (kebab-case)
- **Python Scripts**: `snake_case.py`
- **Notebooks**: Descriptive kebab-case (e.g., `01-setup-diagnostics.ipynb`)
- **Directories**: kebab-case (e.g., `prompts/`, `rag/`, `agents/`)

## Where New Content Should Go

- **Raw imports**: `source-material/` (read-only staging)
- **Synthesized learning content**: `docs/`, `notebooks/`, `prompts/`
- **Implementation code**: `agents/`, `rag/`, `tools/`, `eval/`, `scripts/`
- **Reusable utilities**: `src/`

---

If the structure changes, update this document and the repository root README.
