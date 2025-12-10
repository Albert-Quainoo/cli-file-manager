import os
from files import display_file, touch, rm, mv
from directory import create_folder, delete_folder
from navigation import pwd, ls, cd

def main():
    current_dir = os.getcwd()
    
    print("Welcome to our CLI!")
    print("Type 'help' for available commands\n")
    
    while True:
        command = input(f"{current_dir} >> ").strip().split()
        
        if not command:
            continue
        
        cmd = command[0]
        args = command[1:]
        
        # Navigation
        if cmd == "pwd":
            pwd(current_dir)
        
        elif cmd == "ls":
            ls(current_dir)
        
        elif cmd == "cd":
            if args:
                new_dir = cd(args[0], current_dir)
                if new_dir:
                    current_dir = new_dir
            else:
                print("Usage: cd <directory>")
        
        # File operations
        elif cmd == "view" or cmd == "cat":
            if args:
                display_file(args[0], current_dir)
            else:
                print("Usage: view <filename>")
        
        elif cmd == "touch":
            if args:
                touch(args[0], current_dir)
            else:
                print("Usage: touch <filename>")
        
        elif cmd == "rm":
            if args:
                # Check for flags
                force = False
                recursive = False
                target = None
                
                for arg in args:
                    if arg == "-rf" or arg == "-fr":
                        force = True
                        recursive = True
                    elif arg == "-r":
                        recursive = True
                    elif arg == "-f":
                        force = True
                    else:
                        target = arg
                
                if target:
                    rm(target, current_dir, force=force, recursive=recursive)
                else:
                    print("Usage: rm <filename>")
            else:
                print("Usage: rm [-r] [-f] <filename>")
        
        elif cmd == "mv":
            if len(args) >= 2:
                mv(args[0], args[1], current_dir)
            else:
                print("Usage: mv <source> <destination>")
        
        # Directory operations
        elif cmd == "mkdir":
            if args:
                create_folder(args[0], current_dir)
            else:
                print("Usage: mkdir <foldername>")
        
        elif cmd == "rmdir":
            if args:
                delete_folder(args[0], current_dir)
            else:
                print("Usage: rmdir <foldername>")
        
        # Help and exit
        elif cmd == "help":
            print("\nAvailable commands:")
            print("  pwd                       Show current directory")
            print("  ls                        List directory contents")
            print("  cd <directory>            Change directory")
            print("  view <filename>           Display file contents")
            print("  touch <filename>          Create empty file")
            print("  rm <filename>             Delete file")
            print("  rm -r <foldername>        Delete folder and contents")
            print("  rm -rf <foldername>       Delete folder (no confirmation)")
            print("  mv <source> <dest>        Move/rename file")
            print("  mkdir <foldername>        Create directory")
            print("  rmdir <foldername>        Delete empty directory")
            print("  help                      Show this message")
            print("  exit                      Exit the program\n")
        
        elif cmd == "exit" or cmd == "quit":
            print("Goodbye!")
            break
        
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()