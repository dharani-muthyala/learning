# To see ubantu info
uname -a

# Files and Directories
pwd                    # Displays the current working directory path in the Linux file system.
ls                     # Lists all files and directories available in the current directory.
mkdir testdir          # Creates a new directory named testdir inside the current location.
cd testdir             # Changes the current working directory to testdir(navigating).
touch file.txt         # Creates a new empty file named file.txt inside the current directory.

# Hard and Soft Links (difference between hard links and soft (symbolic) links and verify inode behavior)
echo "Hello Linux" > file.txt      # Creates a file named file.txt and writes the text "Hello Linux" into it.
ln file.txt hardlink.txt           # Creates a hard link named hardlink.txt pointing to the same inode as file.txt.
ln -s file.txt softlink.txt        # Creates a symbolic link named softlink.txt that references file.txt.
ls -li                             # verify inode numbers
# observation  
file.txt and hardlink.txt share the same inode number.
softlink.txt has a different inode number.
softlink.txt shows an arrow (->) pointing to file.txt.
# Key findings
**Hard link:**
Shares same inode as original file
Data remains accessible even if one filename is deleted
Cannot span across file systems
**Soft link:**
Has a different inode
Acts like a shortcut
Breaks if original file is deleted
Can span across file systems

