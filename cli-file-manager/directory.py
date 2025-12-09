import os
'''
The Following were used to help make the task effective:
Pythons OS module for file reading:
    os.path.join: safely combines folder and file names into full paths
    os.path.isdir: checks if a path points to a directory(folder)
    os.listdir: lists all files/folders inside a given directory
    os.rmdir: deletes an empty directory
    os.mkdir: creates a new directory(folder)
'''
def create_folder(directory_path, folder_args):
#This is to check if the folder name was given
    if len(folder_args) == 0:
        print("Please Provide a folder name")
        return
    
#Creating its variable
    folder_name = folder_args[0]
    full_path = os.path.join(directory_path, folder_name)

#To check if the folder already exists
    if os.path.exists(full_path):
        print("Folder already exists.")
        return
    else:
        os.mkdir(full_path)
        print("Folder created successfully.")

#To create the new folder with error handling to minimize errors        
    try:
        os.mkdir(full_path)
        print("Folder created successfully.")
    except Exception as e:
        print(f"Error creating folder: {e}")


def delete_folder(directory_path, folder_args):
#This is to check if the folder name was given
    if len(folder_args) == 0:
        print("Please Provide a folder name")
        return
    
#Creating its variable
    folder_name = folder_args[0]
    full_path = os.path.join(directory_path, folder_name)

#Checking if the folder exists
    if os.path.exists(full_path) == False:
        print(f"This foldername doesnt exist")
        return
#Checking if the directory was typed by mistake
    if os.path.isdir(full_path) == False:
        print("This is a directory name, not a folder name")

#Checking if the folder is empty and deletion if its empty
    if len(os.listdir(full_path)) > 1:
        print("It has content so can't be deleted")
        return
    else:
        os.rmdir(full_path)
        print("Folder has been deleted successfully")
    

def help_function(directory_path, folder_args):
#Giving the list of commands for the user
    commands = {
        "ls": "Lists directory contents",
        "pwd": "Shows current directory",
        "cd <folder>": "Change directory",
        "view <filename>": "Display file contents",
        "touch <filename>": "Create empty file",
        "rm <filename>": "Delete file with confirmation",
        "mv <oldname> <newname>": "Rename file or folder",
        "mkdir <foldername>": "Create a new directory",
        "rmdir <foldername>": "Delete an empty directory",
        "help": "Show this help message",
        "exit": "Exit the program"}
    for cmds in commands.items():
        print(cmds)