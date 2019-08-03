$directory = Read-Host -Prompt 'Input your directory'
(gci "$directory\" -r | ? {$_.PSIsContainer -eq $True}) | ?{$_.GetFileSystemInfos().Count -eq 0} | remove-item
