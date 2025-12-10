import os

'''
The Following were used to help make the task effective:
Pythons OS module for file reading:
    os.path.join: safely combines folder and file names into full paths
    os.path.isdir: checks if a path points to a directory(folder)
    os.listdir: lists all files/folders inside a given directory
    os.rmdir: deletes an empty directory
    os.mkdir: creates a new directory(folder)

Main Roles:
Creating Files
Deleting Files safely
A Help Command System

'''

def create_folder(folder_name, directory=None):
    # Building the path
    if directory != None:
        full_path = os.path.join(directory, folder_name)
    else:
        full_path = os.path.join(os.getcwd(), folder_name)

    # Normalizing the path
    full_path = os.path.normpath(full_path)
    
    # Checking if folder already exists
    if os.path.exists(full_path):
        print(f"Error: '{full_path}' already exists")
        return False
    
    # Handling folder creation & Error handling 
    try:
        os.mkdir(full_path)
        print(f"Created folder: '{full_path}'")
        return True
    except PermissionError:
        print(f"Error: Permission denied for '{full_path}'")
        return False
    except OSError as e:
         print(f"Error creating folder: {e}")
         return False
    
    

def delete_folder(folder_name, directory=None):
    # Building the path
    if directory != None:
        full_path = os.path.join(directory, folder_name)
    else:
        full_path = os.path.join(os.getcwd(), folder_name)

    # Normalizing the path
    full_path = os.path.normpath(full_path)

    # Check if path exists
    if not os.path.exists(full_path):
         print(f"Error: '{full_path}' does not exist")
         return False
    
    # Checking if it is an actual directory
    if not os.path.isdir(full_path):
        print(f"Error: '{full_path}' is not a directory")
        return False
    
    # Checking if the folder is an empty folder
    if len(os.listdir(full_path)) > 0:
        print(f"Error: '{full_path}' is not empty")
        return False
    
    # Handling deletion & Error handling
    try:
        os.rmdir(full_path)
        print(f"Deleted folder: '{full_path}'")
        return True
    except PermissionError:
     print(f"Error: Permission denied for '{full_path}'")
     return False
    except OSError as e:
     print(f"Error deleting folder: {e}")
     return False
