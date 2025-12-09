import os

def display_file(filename, directory=None):
    if directory:
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
    if not os.path.isdir(filepath):
        print(f" Error: `{filepath}` is a directory, not a file!")
        return False
    
   # Checking for read permission from file system
    if not os.access(filename, os.R_OK):
        print(f"No read permission for {filepath}")
        return False
    
    # Checking the file size
    file_size = os.path.getsize(filepath)
    if file_size > 1_000_000: # 1 MB
        user_confirmation = input(f"File size is large ({file_size / 1_000_000:.2f}MB). Display anyway? (y/n): ")
        if user_confirmation.lower() != 'y':
            return False
        
    # Error handling    
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

