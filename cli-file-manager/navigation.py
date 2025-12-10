import os

# Shows current directory

def pwd(directory=None):
    if directory != None:
        print(f"Current Directory: {directory}")
    else:
        print(f"Current Directory: {os.getcwd()}")        

# List contents in current directory

def ls(directory=None):
    # Building file path
    if directory != None:
        path = directory
    else:
        path = os.getcwd()
    # Checking if path exists
    if not os.path.exists(path):
      print(f"Error: '{path}' does not exist")
      return False
    
    # Checking if it is actually a directory
    if not os.path.isdir(path):
     print(f"Error: '{path}' is not a directory")
     return False
    
   # Content list & Error Handling
    try:
       items = os.listdir(path)

       # Checking if directory is empty
       if len(items) == 0:
        print("(empty directory)")
       else:
          # Checking if item is a directory or file 
          for item in items:
             full_path = os.path.join(path, item)
             if os.path.isdir(full_path):
                print(f"  {item}/")
             else:
              print(f"  {item}")
          return True
    except PermissionError:
       print(f"Error: Permission denied for '{path}'")
       return False


# Changing Directory
def cd(destination, directory=None):
    # Building file path
    if directory != None:
        new_path = os.path.join(directory, destination)
    else:
        new_path = os.path.join(os.getcwd(), destination)

    # Normalizing file path
    new_path = os.path.normpath(new_path)
      
    # Checking if file path exists
    if not os.path.exists(new_path):
        print(f"Error: '{new_path}' does not exist")
        return None
      
    # Checking if it is directory
    if not os.path.isdir(new_path):
        print(f"Error: '{new_path}' is not a directory")
        return None
      
    # Returning new path for main.py file
    return new_path



          
