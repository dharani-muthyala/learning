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

# grep and Regex
**Creating sample log file**
echo "error occurred" >> log.txt
echo "success message" >> log.txt
echo "warning message" >> log.txt    # Created a sample file log.txt containing multiple log messages to simulate real-world log analysis.

**Searching for a specific word** 
grep "error" log.txt         # Searches for lines containing the word "error" in the file. output should be: error occurred
**Observation:**
grep filters and displays only matching lines from the file.
**Using Extended Regular Expressions (Multiple Conditions)**
grep -E "error|warning" log.txt        
#Uses extended regular expression with the | operator (OR condition) to search for lines containing either "error" or "warning". 
**Output:**
error occurred
warning message 
**Observation:**
-E enables extended regex, allowing multiple pattern matching using the OR (|) operator.

# User Management(creating local user account in linux)
**Creating a new user**
sudo useradd testuser      # Creates a new local user named testuser.
**Setting password for user**
sudo passwd testuser
**Observation:**
The system prompted:
New password:
Retype new password:
After entering and confirming the password, the message displayed:
passwd: password updated successfully
**Verifying user creation**
id testuser       # Displays user ID (UID), group ID (GID), and associated groups.
**Modify a user**
**Add user to a group**
sudo usermod -aG sudo testuser    # To modify user properties we use usermod.
Explanation:
usermod → modify user
-a --> append
-G --> group
This adds testuser to the sudo group.
**Change user name**
sudo usermod -l newusername testuser    # Changes the username from testuser -> newusername.
**Change user home directory**
sudo usermod -d /home/newdir testuser    # Changes the home directory.
**Delete a user**
sudo userdel testuser    # This removes the user account.
**Delete user with home directory**
sudo userdel -r testuser   # -r removes the user's home directory and mail spool.

# Resource limits
**Checking Current Resource Limits**
ulimit -a        # Displays all the resource limits configured for the current user session.
Example Output Includes:
Maximum number of user processes
Maximum file size
Maximum open files
CPU time limits
**Observation:**
This command helps identify how many system resources are allowed for the current user.
**Temporarily Modifying Process Limits**
ulimit -u 50      # Sets the maximum number of processes that the current user can create to 50.
**Observation:**
This change applies only to the current terminal session and is not permanent.
**Resetting the Limit**
ulimit -u unlimited      # Removes the previously set limit and restores the default system behavior.

# Root Access
**Checking Current Logged-in User**
whoami         # Displays the username of the current logged-in user.
**Observation:**
Used to verify whether the session is running under a normal user or root user.
**Switching to Root User**
sudo su        # Grants temporary root (superuser) access using sudo privileges.
**Observation:**
After executing this command, the terminal session switches to root mode, allowing administrative commands to be executed.
**Key Learning**
Root user has full system privileges.
sudo allows controlled administrative access.
Root access should be used carefully to avoid system misconfiguration.


# How To Manage Linux Services
**Basic info about init systems**
In a full Linux system the init system (like systemd or System V init) manages services.
In Codespaces, check what process started the container.
Run:
ps -p 1
You will see the PID 1 process (the first process in the system).
This shows what is acting like the init process in the container.
**Understanding Services (Similar to systemd Units)**
service --status-all       # List available services.
**Example output:**
[ + ] ssh
[ - ] rsync
[ - ] dbus
"-" --> Stopped service
"+" --> Running service   # This is equivalent to checking units with systemctl.
# Installing a Service (Apache)
**Installing web server**
sudo apt update
sudo apt install apache2 -y     # This installs: Apache HTTP Server
**Checking Service Status**
Equivalent of systemctl status.
Run:
service apache2 status
You will see whether the service is running or stopped.

# Starting a Service
**Start the Apache service:**
sudo service apache2 start
**Verify:**
service apache2 status

# Stopping a Service
**Stop the web server:**
sudo service apache2 stop
**Check again:**
service apache2 status

# Restarting a Service
**Restart the service:**
sudo service apache2 restart
**This does:**
stop -> start

# Auto-Start Services (Enable / Disable)
**In full systemd systems you would use:**
systemctl enable apache2
In Codespaces you can inspect startup scripts instead.
**Check startup configuration:**
ls /etc/init.d/
**You will see scripts like:**
apache2
ssh
rsync
These scripts control service startup in older init systems.

# Where Service Files Are Stored
**Check service scripts:**
ls /etc/init.d/
**Example:**
apache2
ssh
rsync
**View the Apache service script:**
cat /etc/init.d/apache2
**This file defines:**
how the service starts
how it stops
restart logic