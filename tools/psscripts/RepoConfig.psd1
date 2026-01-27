@{
  RepoName = 'llm-engineering-in-practice'

  ExpectedFolders = @(
    '.copilot'
    '.cursor'
    'docs'
    'agents'
    'eval'
    'notebooks'
    'prompts'
    'rag'
    'scripts'
    'src'
    'tools'
    'source-material'
    '.github'
    '.cursor\rules'
  )

  YamlCheckRoots = @(
    'docs'
  )

  DisallowInterviewLanguage = $false
}
