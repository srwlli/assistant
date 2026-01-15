$stubs = @(
  "C:\Users\willh\Desktop\assistant\coderef\working\agent-completion-workflow\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\agent-dashboard-filesystem-workflow\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\agent-git-branches\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\agent-persona-team-page\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\agent-perspective-session-reports\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\agent-reporting-prompts\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\ai-context-improvements\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\ai-video-gen\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\align-plan-command-refactor\stub.json",
  "C:\Users\willh\Desktop\assistant\coderef\working\assistant-to-other-projects\stub.json"
)

Write-Host "Processing first 10 stubs..."
$stubs | ForEach-Object {
  Write-Host "Validating: $_"
  Get-Content $_
  Write-Host "---"
}
