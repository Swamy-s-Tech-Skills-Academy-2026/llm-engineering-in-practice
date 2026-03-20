# Repository Structure (LLM Engineering in Practice)

Personal learning workspace with a **simple, incremental** layout.

## Core idea

- **One day = one folder:** `src/weekN/dayN/`
- **Add subfolders on demand** inside that day (`prompts/`, `data/`, `eval/`, `rag/`, …) when the lesson needs them — no empty scaffolding.
- **`src/setup/`** is the only shared code area outside `weekN/dayN/` (diagnostics & troubleshooting).
- **`.backup/`** holds frozen archives (e.g. full `docs/weeks/`, old root `notebooks/`, `prompts/`, `eval/`). Restore when you need that material.

See also: **`src/README.md`** for the live tree.

## `docs/`

- **`learning-plan.md`** — master roadmap
- **`01-setup.md`**, **`01_repository-structure.md`** — setup and structure notes
- **`weeks/`** — optional; may be empty if weekly guides live in **`.backup/docs/weeks/`** until restored
- **`reports/`** — generated diagnostics reports

## `source-material/`

- Read-only reference (course/community examples)
- **Zero-copy:** synthesize into `src/` or `docs/`, never paste verbatim

## `tools/`

- Optional shell / PowerShell helpers

## CI / Python

- Lint and notebooks under **`src/`** (see `.github/workflows/ci-python.yml`)
