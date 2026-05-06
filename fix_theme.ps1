
$bytes = [System.IO.File]::ReadAllBytes('c:\Users\panup\OneDrive\Desktop\เว็บ\index2.html')
$html = [System.Text.Encoding]::UTF8.GetString($bytes)

$html = $html -replace 'background:#0f172a', 'background:#F0F4F8'
$html = $html -replace 'background:#0F172A', 'background:#F0F4F8'
$html = $html -replace 'background:#1e293b', 'background:#ffffff'
$html = $html -replace 'background:#1E293B', 'background:#ffffff'
$html = $html -replace 'background:#111827', 'background:#f8fafc'
$html = $html -replace 'background:#0a1628', 'background:#F0F4F8'
$html = $html -replace 'color:#f8fafc', 'color:#1E293B'
$html = $html -replace 'color:#cbd5e1', 'color:#334155'
$html = $html -replace 'color:#e2e8f0', 'color:#475569'
$html = $html -replace 'border:1px solid #334155', 'border:1px solid #DDE4EE'
$html = $html -replace 'border: 1px solid #334155', 'border: 1px solid #DDE4EE'
$html = $html -replace 'border:1px solid #1e293b', 'border:1px solid #DDE4EE'
$html = $html -replace 'border-bottom:1px solid #1e293b', 'border-bottom:1px solid #DDE4EE'

[System.IO.File]::WriteAllBytes('c:\Users\panup\OneDrive\Desktop\เว็บ\index2.html', [System.Text.Encoding]::UTF8.GetBytes($html))
Write-Host "HTML dark styles fixed successfully"
