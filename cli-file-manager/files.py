import os
import shutil

def display_file(filename, directory=None):
    # Building the filepath
    if directory != None:
        filepath = os.path.join(directory, filename)
    else:
        filepath = os.path.join(os.getcwd(), filename)
    
    # Normalizing the filepath 
    filepath = os.path.normpath(filepath)

    # Checking if filepath exists
    if not os.path.exists(filepath):
        print(f" Error: `{filepath}` does not exist!")
        return False
    
    # Checking for file not directory
    if os.path.isdir(filepath):
        print(f" Error: `{filepath}` is a directory, not a file!")
        return False
    
    # Checking for read permission from file system
    if not os.access(filepath, os.R_OK):
        print(f"No read permission for {filepath}")
        return False
    
    # Checking the file size
    file_size = os.path.getsize(filepath)
    if file_size > 1_000_000: # 1 MB
        user_confirmation = input(f"File size is large ({file_size / 1_000_000:.2f}MB). Display anyway? (y/n): ")
        if user_confirmation.lower() != 'y':
            return False
        
    # File Reading & Error handling    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"\n--- {filepath} ---\n")
        print(content)
        print(f"\n--- End of file ({file_size} bytes) ---")
        return True
    
    except UnicodeDecodeError:
        print(f"Error: '{filepath}' appears to be a binary file")
        return False
    
    except PermissionError:
        print(f"Error: Permission denied reading '{filepath}'")
        return False
    
    except OSError as e:
        print(f"Error reading file: {e}")
        return False
    

def touch(filename, directory=None):
    # Building the filepath (for touch)
    if directory != None:
        filepath = os.path.join(directory, filename)
    else:
        filepath = os.path.join(os.getcwd(), filename)

    # Normalizing the filepath (for touch)
    filepath = os.path.normpath(filepath)

    # Checking if parent directory exists
    parent_directory = os.path.isdir(filepath)
    if parent_directory and not os.path.exists(parent_directory):
        print(f"Error: Directory `{parent_directory}` does not exist!")
        return False

    # Checking if a file is being touched (not directory)
    if os.path.isdir(filepath):
        print(f"Error: `{filepath}` is a directory, not a file!")
        return False
    
    # Handling touch execution & Error handling
    try:
        if os.path.exists(filepath):
            # if file exists, update timestamps (metadata)
            os.utime(filepath, None) # Sets to current timee
            print("File exists")
            print(f"Updated timestamps: `{filepath}`") # Log update
            
        else:
            # if file does not exist, create empty file
            with open(filepath, 'w') as file:
                pass
            print(f"Created: `{filepath}` ")
        return True
    except PermissionError:
        print(f"Error: Permission Denied for `{filepath}`")
        return False
    except OSError as e:
        print(f" Error: {e}")
        return False
    

def rm(filename, directory=None, force=None, recursive=False):
    # Building the filepath
    if directory != None:
        filepath = os.path.join(directory, filename)
    else:
        filepath = os.path.join(os.getcwd(), filename)
    
    # Nomralizing the filepath (for rm)
    filepath = os.path.normpath(filepath)

    # Checking if filepath exists
    if not os.path.exists(filepath):
        if force != None:
            return True
        print(f"Error: `{filepath}` does not exist!")
        return False
    
    # Handling Directories 
    if os.path.isdir(filepath):
        if not recursive:
            print(f"Error: '{filepath}' is a directory. Use rm -r to remove")
            return False
        
        if not force:
            confirm = input(f"Remove directory '{filepath}' and all contents? (y/n): ")
            if confirm.lower() != 'y':
             print("Cancelled")
             return False
        
        # Remove directory and contents
        try:
            shutil.rmtree(filepath)
            print(f"Removed directory: '{filepath}'")
            return True
        except PermissionError:
            print(f"Error: Permission denied for '{filepath}'")
            return False
        except OSError as e:
            print(f"Error: {e}")
            return False

    
    # Checking for write protection (For files)
    if not force and not os.access(filepath, os.W_OK):
        confirm = input(f"Remove write-protected file '{filepath}'? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled")
            return False
        
    # Removing file & Error handling 
    try:
        os.remove(filepath)
        print(f"Removed `{filepath}`")
        return True
    except PermissionError:
        print(f"Error: Permission denied for '{filepath}'")
        return False
    except OSError as e:
        print(f"Error: {e}")
        return False
    

def mv(filename, destination, directory=None, force=False):
    # Building the source path
    if directory != None:
        source = os.path.join(directory, filename)
    else:
        source = os.path.join(os.getcwd(), filename)

    # Normalizing the source path
    source = os.path.normpath(source)

    # Check if source exists
    if not os.path.exists(source):
        print(f"Error: '{source}' does not exist")
        return False

    # Reject directories
    if os.path.isdir(source):
        print(f"Error: '{source}' is a directory")
        return False
    
    # Building the destination path
    if directory != None:
        dest = os.path.join(directory, destination)
    else:
        dest = os.path.join(os.getcwd(), destination)
    
    dest = os.path.normpath(dest)

    # If destination is a directory, move the file into it
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(source))

    # Check if destination already exists
    if os.path.exists(dest):
        if not force:
            confirm = input(f"'{dest}' already exists. Overwrite? (y/n): ")
            if confirm.lower() != 'y':
                print("Cancelled")
                return False
            
    # Handling actual move & Error handling 
    try:
        shutil.move(source, dest)
        print(f"Moved: '{source}' -> '{dest}'")
        return True
    except PermissionError:
        print(f"Error: Permission denied")
        return False
    except OSError as e:
        print(f"Error: {e}")
        return False
    

        
        







    
    


    

    









    

