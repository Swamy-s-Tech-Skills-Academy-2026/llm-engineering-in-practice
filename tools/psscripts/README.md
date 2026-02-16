# PowerShell Scripts

**Location**: `tools/psscripts/`

**Purpose**: Automation scripts for validation and repository maintenance (Windows 11 + PowerShell).

---

## 📋 Script Set (Standardized)

### Health Check & Validation

#### `RepoConfig.psd1`

Per-repo settings consumed by shared scripts (keeps behavior consistent across repos while allowing repo-specific structure/policy).

---

#### `Quick-HealthCheck.ps1`

Fast workspace health check. Reads expected folders from `RepoConfig.psd1`.

**Usage:**

```powershell
.\tools\psscripts\Quick-HealthCheck.ps1
```

---

#### `Validate-FileReferences.ps1`

Validates markdown file references point to existing files.

**Usage:**

```powershell
.\tools\psscripts\Validate-FileReferences.ps1
.\tools\psscripts\Validate-FileReferences.ps1 -Path "src"
```

---

#### `Verify-ZeroCopy.ps1`

Helps detect accidental verbatim copying from `source-material/` into educational content (docs, prompts, src).

**Usage:**

```powershell
.\tools\psscripts\Verify-ZeroCopy.ps1
.\tools\psscripts\Verify-ZeroCopy.ps1 -Strict
```

---

### Linting & Link Checking

#### `Run-MarkdownLintAndLychee.ps1`

Runs Markdown lint (`markdownlint-cli2`) and link checking (Lychee) using repo `lychee.toml`.

**Usage:**

```powershell
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1 -IncludeSourceMaterials
```

---

### Repo Stats / Utilities

- `Get-RepoStats.ps1` - Repository statistics (file counts, extensions, folder structure)

---

### Batch Execution

#### `Run-AllPSScripts.ps1`

Convenience runner to execute all validation scripts with safe defaults.

**Usage:**

```powershell
.\tools\psscripts\Run-AllPSScripts.ps1
.\tools\psscripts\Run-AllPSScripts.ps1 -IncludeHeavy
```

---

## 🚀 Quick Start

```powershell
.\tools\psscripts\Quick-HealthCheck.ps1
.\tools\psscripts\Validate-FileReferences.ps1
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1

# Run checks independently
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1 -MarkdownOnly
.\tools\psscripts\Run-MarkdownLintAndLychee.ps1 -LycheeOnly
```

---

## 🔗 Related Documentation

- [Project Focus](../../.cursor/rules/01_project-focus.mdc)
- [Repository Structure](../../.cursor/rules/02_repository-structure.mdc)
- [Quality Assurance](../../.cursor/rules/09_quality-assurance.mdc)
- [Source Material Rules](../../.cursor/rules/07_source_material_rules.mdc)
