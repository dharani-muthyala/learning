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

# Understanding Service File Structure
**Open the service file:**
nano /etc/init.d/apache2
**You will see sections like:**
start)
stop)
restart)
status)
These define how the service behaves.

# Reload vs Restart
**Restart Apache:**
sudo service apache2 restart
**Reload configuration:**
sudo service apache2 reload
**Difference:**
restart -->	stop + start
reload --> reload config without full restart

# Monitor Running Services
**Check Apache process:**
ps aux | grep apache
You will see running worker processes.

# Test the Web Server
**Start Apache:**
sudo service apache2 start
**Check locally:**
curl localhost
You should see Apache default HTML page.

# Editing and Overriding systemd Unit Files
Since systemd is not running in Codespaces, the systemctl command cannot be used.
Instead, service behavior can be examined and modified through init scripts.
**View service scripts**
ls /etc/init.d/
**Example output:**
apache2
ssh
rsync
**Inspect a service script**
cat /etc/init.d/apache2
**This script contains the logic for**:
starting the service
stopping the service
restarting the service
**Create a custom copy (simulate overriding)**
sudo cp /etc/init.d/apache2 /etc/init.d/apache2-custom
**Edit the copied file:**
sudo nano /etc/init.d/apache2-custom
This simulates modifying service behavior similar to overriding a systemd unit file.

# Reloading systemd (daemon-reload) and Why It Is Needed
When a systemd unit file is modified, the changes are not automatically detected.
To apply the changes, systemd must reload its configuration.
**Command used in real systems:**
systemctl daemon-reload
**This command tells systemd to:**
Re-read all unit files and update its configuration.
**Typical workflow:**
Edit service file
systemctl daemon-reload 
systemctl restart service
This ensures the new configuration is applied.

# Codespaces (Equivalent):
Because systemd is not available in Codespaces, the equivalent approach is restarting the service after modifying its script.
**Edit the service script:**
sudo nano /etc/init.d/apache2
**Restart the service:**
sudo service apache2 restart
Restarting the service makes the system apply the updated configuration.


# Podman container management
**How to install podman**
sudo apt update
sudo apt install podman -y
**To check installation**
podman --version   # can able to see the podman installed version
**To check podman info**
podman info

# Running a Quart API Using Podman
This demo shows how to run a simple Python API built with the Quart framework using Podman.
**The goal is to learn how Podman can:**
build a container image
run an application inside a container
manage the running container
**Build the Container Image**
First, we need to build a container image using the Containerfile.
**Run the following command:**
podman build -t quart-api .
**What this command does**
podman build
Builds a container image using the instructions written in the Containerfile.
-t quart-api
Gives a name (tag) to the image. Here the image name will be quart-api.
.
The dot means current folder. Podman will use the files in this folder (like app.py, requirements.txt, and Containerfile) to build the image.
After running this command, Podman creates a container image for the application.
**To check if the image was created successfully, run:**
podman images
**What this command does**
podman images
Shows all container images stored on the system. You should see the quart-api image in the list.
Run the Application Container
After building the image, we can start a container from that image.
**Run the command:**
podman run -d -p 5000:5000 quart-api
**What this command does**
podman run
Creates and starts a container from the specified image.
-d
Runs the container in the background (detached mode).
-p 5000:5000
Connects the container port to the host port.
First 5000 --> port on your system
Second 5000 --> port inside the container where the API runs
This allows you to access the API from your browser.
quart-api
This is the name of the image used to create the container.

# Check Running Containers
To see if the container is running, use:
podman ps
**What this command does**
podman ps
Shows all currently running containers.
**It displays details like:**
container ID
image name
running status
port mapping
This helps confirm that the application container started successfully.
Codespaces automatically detects open ports and provides a forwarded public URL.
**When the container starts, Codespaces will show a notification similar to:**
Port 5000 forwarded
You can also view this in the Ports tab in the Codespaces interface.
The forwarded link will look similar to this:
https://<codespace-name>-5000.app.github.dev
Open this link in the browser to access the running API.
If the application is running correctly, you should see the response:
{"message":"Podman API running"}


# Podman commands for managing Containers
podman ps                                            # List Running containers
podman ps -a                                         # List all containers including running and stopped
podman stop <container_id> or <container_name>       # Stop container
podman start <container_id> or <container_name>      # start container
podman restart <container_id> or <container_name>    # restarts container
podman logs <container_id> or <container_name>       # View logs
podman inspect <container_id>                        # inspect container
podman rm <container_id>                             # remove container

# Podman commands for managing Images
podman images          # List images
podman rmi quart-api   # remove image
podman search nginx    # search images
podman pull nginx      # pull image

# Pulling Container Images
In some environments, Podman may not allow the use of short image names such as:
podman pull nginx
This happens when unqualified search registries are not configured in the system. In such cases, Podman cannot determine which container registry should be used to download the image.
**Pulling an Image Using Full Image Path**
Run the following command:
podman pull docker.io/library/nginx
**Command Explanation**
podman pull
Downloads a container image from a container registry.
docker.io
The container registry where the image is stored. Most official images are hosted on Docker Hub.
library/nginx
Represents the official Nginx image repository within Docker Hub.

# Run the container with volume 
podman run -d \
-p 5000:5000 \
-v $(pwd)/data:/app/data \
quart-api
**Command Explanation**
-p 5000:5000
Maps host port 5000 to container port 5000 so the API can be accessed.
-v $(pwd)/data:/app/data   # folder on the host system and folder inside the container
Creates a volume mount.    # This allows data to persist outside the container.

# Anaconda concepts
**Installing Miniconda**
To work with Conda environments for Python development, install Miniconda, which is a lightweight installer for Conda.
**Download the Miniconda Installer**
**1.Run the following command in the terminal to download the installer:**
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

**2.Run the Installer**
**Execute the downloaded script:**
bash Miniconda3-latest-Linux-x86_64.sh
**Follow the installation prompts:**
Press Enter to review the license agreement
Type yes to accept the license
Press Enter to accept the default installation location

**3.Initialize Conda**
**Reload the shell configuration so that Conda becomes available in the terminal:**
source ~/.bashrc

**4.Verify the Installation**
**Check whether Conda is installed successfully:**
conda --version
If the Conda version is displayed, the installation was successful and we can start creating and managing environments.


# Conda Basics
**What is Conda?**
Conda is an open-source package manager and environment manager used to install, manage, and update software packages and their dependencies.
It allows developers to create isolated environments for different projects so that packages and Python versions do not conflict with each other.
**Why use Conda?**
**Conda provides several benefits:**
Environment Isolation - Create separate environments for different projects.
Dependency Management - Automatically installs required dependencies for packages.
Version Control - Easily manage different Python or package versions.
Cross-Platform Support - Works on Linux, macOS, and Windows.
Using Conda helps avoid conflicts when multiple projects require different package versions.

# Working with Environments
**Creating and Activating an Environment**
**Create a new environment with a specific Python version:**
conda create --name myenv python=3.10
**Activate the environment:**
conda activate myenv
**Deactivate the environment:**
conda deactivate
**Specifying a Location for an Environment**
Instead of using a name, we can create an environment at a specific path.
conda create --prefix ./env python=3.10
**Activate the environment:**
conda activate ./env

# Installing Packages into an Environment
**Install a package inside the active environment:**
conda install numpy
**You can also install multiple packages:**
conda install pandas matplotlib

# Listing Packages and Environments
**List all environments:**
conda env list
**List installed packages in the current environment:**
conda list

# Deleting a Package or Environment
**Remove a package:**
conda remove numpy
**Delete an environment:**
conda remove --name myenv --all

# Conda Packages
**A Conda package is a compressed file that contains:**
The software or library (for example: NumPy, Pandas)
Metadata about the package
Dependency information required for installation
Conda packages allow you to easily install, update, and remove libraries in your environment.
**Example: Installing a Package**
conda install numpy
This command downloads the NumPy package and its required dependencies into the active environment.
**Example: Installing Multiple Packages**
conda install pandas matplotlib
Conda automatically resolves and installs all required dependencies.

# Conda Channels
A channel is a location where Conda searches for packages.
Channels host collections of packages that can be installed using Conda.
By default, Conda installs packages from the default channel provided by Anaconda.
**Example: Installing from a Specific Channel**
conda install -c conda-forge numpy
**Here:**
-c means channel
conda-forge is a popular community-maintained channel.
**Example: View Configured Channels**
conda config --show channels
**Example: Add a New Channel**
conda config --add channels conda-forge

# Searching for Packages
You can search for available packages in Conda repositories before installing them.
conda search numpy
**This command displays:**
Available versions of the package
The channel providing the package
Compatible builds
**Example:**
conda search pandas
This helps identify the correct package version before installation.

# Installing a Package from a Specific Channel
Conda allows installing packages from a specific channel.
**Example:**
conda install -c conda-forge numpy
**Explanation:**
-c --> Specifies the channel
conda-forge --> Community-maintained channel containing many packages
This installs the package from the specified channel instead of the default channel.

# Channels - Deeper Dive
Channels are repositories where Conda packages are stored.
**To view configured channels:**
conda config --show channels
**To add a new channel:**
conda config --add channels conda-forge
**To check channel priority:**
conda config --show channel_priority
Channels help manage package sources and control where packages are installed from.

# Local Channels
**Creating a Local Channel:**
A local channel allows you to store and install packages from a local directory.
**Step 1: Create a directory**
mkdir local-channel
cd local-channel
**Step 2: Install conda-build**
conda install conda-build
**Step 3: Index the directory**
conda index .
This converts the directory into a local Conda channel.
**Step 4: Add the local channel**
conda config --add channels file:///path/to/local-channel
Now packages stored in this directory can be installed using Conda.
