<# Shell scripting task 1:
Creating Folders and Sub-folder
Deleting folders
I did take the task into consideration, but I thought to create a menu style;
more user friendly and task did not state whet folder to delete, so I am taking the user input into consideration#>

# Creating 3 folders
# Requesting user input to create names for folders
# Checking if folder already exist in directory before creating a folder
$menu = Read-Host "`nSelect an option from blow list: `n1 - Create 3 folders `n2 - Create Sub-folders (3) `n3 - Delete folders `n Please select your option "
while($menu -ne 4){
    if ($menu -eq 1){
        $folder1 = Read-Host "`nPlease enter name for folder 1 "
        if(Test-Path -Path $folder1){
            Write-Host "`nFolder $folder1 already exits!"
        }
        else{
            New-Item -Path $folder1 -ItemType Directory
            Write-Host "`nFolder $folder1 created successfully!"
        }
        $folder2 = Read-Host "`nPlease enter name for folder 2 "
        if(Test-Path -Path $folder2){
            Write-Host "`nFolder $folder2 already exits!"
        }
        else{
                New-Item -Path $folder2 -ItemType Directory
                Write-Host "`nFolder $folder2 created successfully!"
            }
        $folder3 = Read-Host "`nPlease enter name for folder 3 "
        if(Test-Path -Path $folder3){
            Write-Host "`nFolder $folder3 already exits!"
        }
        else{
            New-Item -Path $folder3 -ItemType Directory
            Write-Host "`nFolder $folder3 created successfully!"
           }
    }
    # Creating Sub - Folder
    # Requesting user input to where the sub-folder should be created.
    # Checking it the main folder exist
    # Checking if the sub-folder already exist in the main folder before creating it
    elseif ($menu -eq 2){
        Get-ChildItem -Directory
        $mainFolder = Read-Host "`nPlease select the main folder to create Sub-Folders in "
        if(Test-Path -Path $mainFolder){
            $subFolder1 = Read-Host "`nPlease enter name for Sub-folder 1 "
                if(Test-Path -Path $subFolder1){
                Write-Host "`nSub-folder $subFolder1 already exits in $mainFolder!"
                }
                else{
                New-Item -Path "$mainFolder\$subFolder1" -ItemType Directory
                Write-Host "`nSub-folder $subFolder1 created successfully in $mainFolder!"
                }
            $subFolder2 = Read-Host "`nPlease enter name for Sub-folder 2 "
                if(Test-Path -Path $subFolder2){
                Write-Host "`nSub-folder $subFolder2 already exits in $mainFolder!"
                }
                else{
                New-Item -Path "$mainFolder\$subFolder2" -ItemType Directory
                Write-Host "`nSub-folder $subFolder2 created successfully in $mainFolder!"
                }
            $subFolder3 = Read-Host "`nPlease enter name for Sub-folder 3 "
                if(Test-Path -Path $subFolder3){
                Write-Host "`nSub-folder $subFolder3 already exits in $mainFolder!"
                }
                else{
                New-Item -Path "$mainFolder\$subFolder3" -ItemType Directory
                Write-Host "`nSub-folder $subFolder3 created successfully in $mainFolder!"
                }
            }
        else{
            Write-Host "`nThe folder $mainFolder does not exist!"
            }
    }
    # Deleting Folders
    # Requesting user input to where the folder should be deleted from, gave option for main directory or sub-folders
    # Checking if the folder exist before deleting it
    elseif ($menu -eq 3){
        $select_folder = Read-Host "`nPlease select where you want to delete folder from `n1 - Main folders `n2 - Sub-Folders"
        if($select_folder -eq 1){
            Get-ChildItem -Directory
            $del_folder1 = Read-Host "`nPlease enter the names of the folders you want to delete in the main directory "
                if(Test-Path -Path $del_folder1){
                    Remove-Item -Path $del_folder1 -Recurse -Force
                    Write-Host "`nFolder $del_folder1 deleted successfully!"
                }
                else{
                    Write-Host "`nFolder $del_folder1 does not exist!"
                    }
               $del_folder2 = Read-Host "`nPlease enter the names of the folders you want to delete in the main directory "
                if(Test-Path -Path $del_folder2){
                    Remove-Item -Path $del_folder2 -Recurse -Force
                    Write-Host "`nFolder $del_folder2 deleted successfully!"
                    }
                else{
                    Write-Host "`nFolder $del_folder2 does not exist!"
                }         
        }
        # code for deleting sub-folders
        elseif($select_folder -eq 2){
            Get-ChildItem -Directory
            $mainFolderDel = Read-Host "`nPlease select the main folder to delete Sub-Folders from "
            if(Test-Path -Path $mainFolderDel){
                Get-ChildItem -Path $mainFolderDel -Directory
                $del_subfolder1 = Read-Host "`nPlease enter the names of the Sub-folders you want to delete in $mainFolderDel "
                    if(Test-Path -Path "$mainFolderDel\$del_subfolder1"){
                        Remove-Item -Path "$mainFolderDel\$del_subfolder1" -Recurse -Force
                        Write-Host "`nSub-folder $del_subfolder1 deleted successfully from $mainFolderDel!"
                    }
                    else{
                        Write-Host "`nSub-folder $del_subfolder1 does not exist in $mainFolderDel!"
                    }
                $del_subfolder2 = Read-Host "`nPlease enter the names of the Sub-folders you want to delete in $mainFolderDel "
                    if(Test-Path -Path "$mainFolderDel\$del_subfolder2"){
                        Remove-Item -Path "$mainFolderDel\$del_subfolder2" -Recurse -Force
                        Write-Host "`nSub-folder $del_subfolder2 deleted successfully from $mainFolderDel!"
                    }
                    else{
                        Write-Host "`nSub-folder $del_subfolder2 does not exist in $mainFolderDel!"
                    }                
            }
            else{
                Write-Host "`nThe folder $mainFolderDel does not exist!"
            }
        }
    }
    else{
        Write-Host "`nInvalid option selected. Please try again."
            }
    $menu = Read-Host "`nSelect an option from blow list: `n1 - Create 3 folders `n2 - Create Sub-folders (3) `n3 - Delete folders `n4 - Exit `n Please select your option"
}
