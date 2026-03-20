# Week 1: Foundations & Environment

**Theme:** Foundations & Environment
**Time Commitment:** 5 days × 30 minutes = 2.5 hours
**Primary Outcome:** Reproducible Python environment, working API connections (OpenAI + Azure OpenAI)
**Platforms:** OpenAI + Azure OpenAI (Python) - Dual provider support from Day 1

---

## 🎯 Week 1 Learning Objectives

By the end of this week, you will:

- [ ] Set up a reproducible Python 3.12 development environment using `uv`
- [ ] Configure API keys for both OpenAI and Azure OpenAI securely via `.env`
- [ ] Make successful API calls to OpenAI and Azure OpenAI from Python
- [ ] Understand the difference between chat and completion APIs
- [ ] Run the project diagnostics script and resolve any issues
- [ ] Log your first experiment run using `eval/log_utils.py`
- [ ] Understand the repository structure and contribution conventions

---

## 📅 Day-by-Day Breakdown

### Day 1: Environment Setup (30 minutes)

**Learning Goal:** Create a reproducible, isolated Python environment

**Tasks (30 min):**

1. **Install uv** (10 min)
   - Follow the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/)
   - Verify: `uv --version`

2. **Clone and sync dependencies** (10 min)

   ```powershell
   git clone <YOUR_FORK_URL> llm-engineering-learning
   cd llm-engineering-learning
   uv sync
   ```

3. **Run diagnostics** (10 min)

   ```powershell
   cd notebooks/01-setup
   uv run python run_diagnostics.py
   ```

**Success Criteria:**

- [ ] `uv sync` completes without errors
- [ ] Diagnostics report generated in `docs/reports/`

---

### Day 2: API Key Setup (30 minutes)

**Learning Goal:** Securely configure credentials for both LLM providers

**Tasks (30 min):**

1. **Create your `.env` file** (5 min)
   - Copy the template from `docs/01-setup.md` (Step 4)
   - Populate `OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`

2. **Verify credentials work** (20 min)

   ```powershell
   uv run python scripts/api_client.py
   ```

   Expected output: `✅ OPENAI API connection successful!` and `✅ AZURE_OPENAI API connection successful!`

3. **Understand the dual-provider pattern** (5 min)
   - Review `scripts/api_client.py` — note how `get_openai_client()` and `get_azure_openai_client()` follow the same interface
   - This pattern is used throughout all 25 weeks

**Success Criteria:**

- [ ] `.env` file created (and git-ignored)
- [ ] Both providers return a successful test response

---

### Day 3: First LLM Call (30 minutes)

**Learning Goal:** Send a prompt and receive a response from both providers

**Tasks (30 min):**

1. **Open the Week 1 notebook** (5 min)
   - Navigate to `notebooks/week1-first-llm-lab.ipynb`
   - Select the `.venv` Python kernel

2. **Run the notebook cells** (20 min)
   - Follow the guided exercises: system prompt, user message, temperature exploration
   - Run the same prompt against OpenAI and Azure OpenAI and compare responses

3. **Reflect on the output** (5 min)

   ```python
   # Key observations to note:
   # - Response latency (ms)
   # - Token counts (prompt + completion)
   # - Any differences between providers
   ```

**Success Criteria:**

- [ ] Notebook runs end-to-end without errors
- [ ] Both OpenAI and Azure OpenAI produce responses to the same prompt

---

### Day 4: Experiment Logging (30 minutes)

**Learning Goal:** Establish a consistent habit for experiment tracking from Day 1

**Tasks (30 min):**

1. **Understand the logging schema** (10 min)
   - Read `eval/log_utils.py`
   - Review `FIELD_ORDER` — these fields will be used every week

2. **Log your first experiment run** (15 min)

   ```python
   from eval.log_utils import log_run

   run_id = log_run({
       "task":             "week1_first_call",
       "model":            "openai:gpt-4o-mini",
       "prompt_hash":      "hello_world_v1",
       "temperature":      0.7,
       "input_tokens":     12,
       "output_tokens":    35,
       "latency_ms":       420.0,
       "score_relevance":  1.0,
       "score_factuality": 1.0,
       "notes":            "first call, week 1 exercise",
   })
   print(f"Logged: {run_id}")
   ```

3. **Verify the CSV was created** (5 min)
   - Check `eval/experiment_log.csv`

**Success Criteria:**

- [ ] `eval/experiment_log.csv` exists and contains at least one row
- [ ] Row matches the schema defined in `FIELD_ORDER`

---

### Day 5: Review & Repository Orientation (30 minutes)

**Learning Goal:** Understand the project conventions before Week 2

**Tasks (30 min):**

1. **Review the copilot instructions** (10 min)
   - Read `.github/copilot-instructions.md`
   - Key conventions: prompt metadata sidecar, experiment logging, `source-material/` read-only policy

2. **Explore the repository structure** (10 min)
   - Review `docs/01_repository-structure.md`
   - Identify where Week 2 deliverables (`scripts/ingest.py`) will live

3. **Reflection** (10 min)
   - Which provider felt faster?
   - What questions arose about API pricing or rate limits?
   - Which area do you want to explore deeper this week?

**Success Criteria:**

- [ ] Can explain the purpose of each top-level folder
- [ ] Committed first entry to `eval/experiment_log.csv`

---

## 🎁 Week 1 Deliverables

- [ ] Working `.env` with both provider credentials
- [ ] Diagnostics report saved to `docs/reports/`
- [ ] `notebooks/week1-first-llm-lab.ipynb` completed
- [ ] At least one row in `eval/experiment_log.csv`
- [ ] Personal notes on Day 5 reflection

---

## 🔑 Key Concepts

### Dual Provider Pattern

From Week 1 onward, all exercises support both OpenAI and Azure OpenAI. The `scripts/api_client.py` module abstracts provider selection behind a common interface. Use this pattern in all future code.

### Experiment Logging Discipline

Every API call whose output you care about should produce a log entry. The fields `task`, `model`, `prompt_hash`, `temperature`, `latency_ms` are the minimum required. Start logging now so the habit is automatic by Week 5.

### Environment Hygiene

- `.env` must never be committed to git (already in `.gitignore`)
- Always use `uv run` to ensure the correct virtual environment
- API keys rotate — store them in `.env`, not in notebooks or scripts

---

## 📚 Resources

- [OpenAI Python SDK docs](https://platform.openai.com/docs/api-reference)
- [Azure OpenAI SDK docs](https://learn.microsoft.com/azure/ai-services/openai/)
- [uv documentation](https://docs.astral.sh/uv/)
- Course: "LLM Engineering: Master AI, Large Language Models & Agents" by Ed Donner (Udemy)
- `docs/01-setup.md` — detailed Windows 11 setup guide for this repo

---

## ✅ Retrospective Template

Answer these questions in your learning journal after completing Week 1:

1. What went smoothly in the environment setup?
2. What error or blocker did you hit, and how did you resolve it?
3. Of OpenAI and Azure OpenAI, which will be your default going forward, and why?
4. What do you look forward to building in Week 2 (data handling + text chunking)?
