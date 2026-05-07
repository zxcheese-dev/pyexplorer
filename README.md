# pyexplorer

A lightweight command-line file manager written in Python for learning purposes.  
It allows basic file system operations like navigation, file creation, deletion, editing, and moving.

---

## Features

-  List files and folders in current directory
-  Change working directory
-  Create files and directories
-  Edit and read files
-  Delete files and folders
-  Move files and folders
-  Recursive directory tree view (walk)

---

## Run

python main.py

---

## Commands

### Navigation
chdir <path>

---

### Show directory tree
walk <path>

---

### Create files / folders
new file <filename> [content]
new dir <dirname>

---

### Delete files / folders
del <path>

---

### Edit file (overwrite)
chfile <file> <content>

---

### Read file
rdfile <file>

---

### Move files / folders
move <source> <destination>

---

## Notes

- Uses only built-in Python libraries (os, shutil)
- Works in current working directory
- Educational project — not intended for production use

---

## Warning

Be careful with `del`, it permanently deletes files and folders.

---

## Purpose

This project was made to learn:

- File system operations in Python
- CLI design
- Command parsing
- OS automation basics
