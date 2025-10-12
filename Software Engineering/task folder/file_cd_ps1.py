# Create three folders
New-Item -ItemType Directory -Path "C:\Scripts\FolderA"
New-Item -ItemType Directory -Path "C:\Scripts\FolderB"
New-Item -ItemType Directory -Path "C:\Scripts\FolderC"

# Navigate into FolderA
Set-Location -Path "C:\Scripts\FolderA"

# Create three subfolders inside FolderA
New-Item -ItemType Directory -Path ".\Sub1"
New-Item -ItemType Directory -Path ".\Sub2"
New-Item -ItemType Directory -Path ".\Sub3"

# Remove two of the subfolders
Remove-Item -Path ".\Sub2" -Recurse
Remove-Item -Path ".\Sub3" -Recurse
