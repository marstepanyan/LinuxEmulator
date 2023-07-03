# Linux Emulator

This repository contains a Linux emulator implemented in Python. 
It provides a simplified version of a command-line interface that mimics the behavior of a Linux terminal.

## Features

The Linux emulator supports the following commands:

- `pwd`: Print the current working directory.
- `cd`: Change the current working directory.
- `ls`: List files and directories in the current directory or a specified directory.
- `mkdir`: Create a new directory.
- `touch`: Create a new file.
- `rm`: Remove a file or directory.
- `vim`: Open a file in a text editor and edit its content.
- `cat`: Display the content of a file.
- `cp`: Copy a file to a specified location.
- `mv`: Move or rename a file or directory.
- `less`: Display the content of a file one page at a time.
- `prc`: Take a snapshot of the file system.

## Usage

1. Clone the repository:
     git clone https://github.com/marstepanyan/LinuxEmulator.git
2. Change into the project directory:
     cd linux-emulator
3. Run the Linux emulator:
     python main.py
4. Once the emulator is running, you can use the available commands to interact with the Linux-like terminal.Here are some examples:

   1. Print the current working directory:
        > pwd
   2. Change the current working directory: 
        > cd directory-name
   3. List files and directories:
        > ls
   4. Create a new directory:
        > mkdir directory-name
   5. Create a new file:
        > touch file-name
   6. Remove a file or directory:
        > rm file-or-directory-path
   7. Open a file in the text editor and edit its content:
        > vim file-name
   8. Display the content of a file:
        > cat file-name
   9. Copy a file to a specified location:
        > cp source-file-path destination-file-path
   10. Move or rename a file or directory:
        > mv source-path destination-path

