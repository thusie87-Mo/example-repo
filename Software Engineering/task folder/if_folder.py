# Check if 'new_folder' exists
if (Test-Path -Path "C:\Scripts\new_folder") {
    New-Item -ItemType Directory -Path "C:\Scripts\if_folder"
}

# Check if 'if_folder' exists
if (Test-Path -Path "C:\Scripts\if_folder") {
    Write-Output "using hyperionDev"
} else {
    New-Item -ItemType Directory -Path "C:\Scripts\new-projects"
}