Installer Tool
A Python-based tool for creating .bat installers, automatically installing .exe files, and running processes with administrative privileges. This project provides a command-line interface (CLI) to manage installations efficiently and with additional features like backup, logging, and progress tracking.

Features
Create Installer.bat: Generate .bat installer scripts to run .exe files automatically.
Automatic .exe Installation: Install multiple .exe files simultaneously with progress tracking.
Run with Administrative Privileges: Execute installation with elevated permissions for system-level applications.
Backup Files: Backup files before starting the installation to avoid data loss.
Progress Tracking: Display progress bar while installing files and monitor installation status.
Logging: Keep track of all installation processes and errors in a log file for future review.
Prerequisites
Before using this tool, make sure you have Python 3.x installed. You will also need to install some required dependencies.

Installing Dependencies
To install the required dependencies, run the following command:

bash
Copy
Edit
pip install -r requirements.txt
This will install the necessary libraries, including:

colorama - for colored terminal output.
tqdm - for displaying progress bars during installation.
How to Use
Running the Program
Clone the repository or download the files.

Install the dependencies using the command above.

Run the program with:

bash
Copy
Edit
python main.py
Main Menu Options
Upon running the program, the following options will be available:

Create Installer.bat with advanced options: Create a .bat file for installing .exe files with custom settings.
Create Installer.bat and Install Automatically: Generate an installer .bat file and run it automatically.
Auto Install .exe files: Automatically install .exe files from a selected folder.
Exit: Exit the program.
Run with Admin Privileges (For system-level apps): Run the installation processes with elevated privileges (administrator rights).
Backup Files Before Installation
The tool will prompt for a backup folder before installation. All the files in the source folder will be copied to the backup folder to ensure no data is lost during the installation process.

Viewing Logs
A log file, installer_log.txt, will be created to track the installation process. This file contains information about successful installations, errors, and progress updates.

Example
Select a folder containing .exe files.
Choose a destination folder to save the installer script.
Optionally, select a backup folder before starting the installation.
After the installation, the process will show the status in the terminal and create an installer .bat file.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! If you would like to improve this tool or fix bugs, please fork the repository, create a branch, and submit a pull request.

Contact
For more information, contact the project maintainer:

Alirezashamsadinloo
