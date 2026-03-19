# CLI File Manger - Unix Based

A Python-based command-line file manager for navigating directories and performing core file and folder operations.


## Overview

This project is a modular CLI application built in Python that allows users to interact with the file system directly from the terminal. It supports common filesystem tasks such as checking the current directory, listing contents, changing directories, viewing files, creating files, moving or renaming files, creating folders, and deleting files or folders. 


## Features

- Show the current working directory with `pwd`
- List files and folders with `ls`
- Change directories with `cd`
- View file contents with `view` or `cat`
- Create empty files with `touch`
- Remove files with `rm`
- Remove directories recursively with `rm -r` or `rm -rf`
- Move or rename files with `mv`
- Create folders with `mkdir`
- Delete empty folders with `rmdir`
- Display built-in help with `help`


## Project Structure

```text
cli-file-manager/
├── cli-file-manager/
│   ├── main.py
│   ├── navigation.py
│   ├── files.py
│   └── directory.py
└── .gitignore
```

## Libraries Used

* os
* shutil

## How To Run

**1. Clone the repository:**
`git clone https://github.com/Albert-Quainoo/cli-file-manager.git`

**2. Move into the project directory:**
`cd cli-file-manager`

**3. Run the program:**
`python main.py`


## Available Commands

`pwd` - Show the current directory
`ls` - List the contents of the current directory
`cd <path>` - Change directory
`view <file>` - Display file contents
`cat <file>` - Alternative to `view`
`touch <file>` - Create an empty file or update timestamps
`rm <file>` - Delete a file
`rm -r <folder>` - Delete a folder and its contents
`rm -rf <folder>` - Delete a folder recursively without confirmation
`mv <source> <destination>` - Move or rename a file
`mkdir <folder>` - Create a folder
`rmdir <folder>` - Delete an empty folder
`help` - Show available commands
`exit`/`quit` - Exit the application

## Example Usage
```
pwd
ls
mkdir test_folder
cd test_folder
touch notes.txt
view notes.txt
cd ..
mv test_folder renamed_folder
rm -r renamed_folder
exit
```





