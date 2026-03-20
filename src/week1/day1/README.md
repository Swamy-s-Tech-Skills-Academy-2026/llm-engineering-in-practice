# Week 1 · Day 1 — Environment + first web summarizer

**Today’s focus only.** Add more folders under `day1/` (e.g. `prompts/`, `data/`) when this day’s learning needs them.

## What to do today

1. **Environment:** From repo root run `uv sync` and create `.env` with `OPENAI_API_KEY` (see repo root `README.md`).
2. **Diagnostics:** `uv run python src/setup/run_diagnostics.py`
3. **Lab:** Open and run `day1.ipynb` top to bottom (kernel = project `.venv`).
4. **Code:** `scraper.py` fetches page text; the notebook calls the LLM and can log runs via `eval/log_utils.py`.

## Layout (this day)

```text
src/week1/day1/
├── README.md          ← you are here
├── day1.ipynb         ← main lab
├── scraper.py
└── eval/
    ├── log_utils.py
    └── .gitignore     ← ignores experiment_log.csv
```

## Full week / course context

- Master plan: `docs/learning-plan.md` (repo root).
- Archived weekly guides (Week1–Week25): `.backup/docs/weeks/` — copy or restore files into `docs/weeks/` when you reach that week.

## Troubleshooting

- `src/setup/03_troubleshooting.ipynb`
