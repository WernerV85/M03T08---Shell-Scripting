<# Shell scripting task 2 & 3:
If statement example#>

# If statement to check in a folder exist named new_folder
#if folder exist create another folder named if_folder in the same directory
if(Test-Path -Path "new_folder"){
    Write-Output "`nFolder contains new_folder, creating folder if_folder in same directory"
    New-Item -Path "if_folder" -ItemType Directory
    Write-Output "`nFolder if_folder created successfully!`n"
}
# If statement to check if if_folder exist
# if if_folder exist create another folder named hyperionDev
if(Test-Path -Path "if_folder"){
    Write-Output "`nif_folder exists, creating hyperionDev folder"
    New-Item -Path "hyperionDev" -ItemType Directory
}
# if if_folder does not exist create another folder named new-project
else{
    Write-Output "`nif_folder does not exist, creating new-project folder"
    New-Item -Path "new-project" -ItemType Directory
    }
