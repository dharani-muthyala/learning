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

# File Permissions
ls -l          
**Displays detailed information about files including:**
File type
Permission structure (r, w, x)
Owner
Group
File size
**Example Output:**
-rw-r--r-- 1 user user 0 Mar 3 10:00 file.txt
**Modifying File permissions**
chmod 755 file.txt     # Changes the file permissions using numeric mode.
**Permission Breakdown:**
7 - rwx (Owner: read, write, execute)
5 - r-x (Group: read, execute)
5 - r-x (Others: read, execute)        # After modification, verify using: ls -l  command
**Chainging file ownership**
chown $(whoami) file.txt

#Changes the ownership of file.txt to the currently logged-in user.               
#$(whoami) dynamically fetches the current username.
#Ensures correct ownership of the file.
**Key Observations**
Permissions control access levels for owner, group, and others.
chmod modifies access rights.
chown modifies file ownership.
Permission structure directly impacts file security and execution capability.