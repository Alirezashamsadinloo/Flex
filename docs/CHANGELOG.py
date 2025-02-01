# Changelog

All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]
### Added
- **Installer Batch Script**: `installer.py` script that allows the creation of `.bat` files to automate installation of `.exe` files.
- **File and Folder Selection**: Integration of graphical dialogs to select files and installation directories.
- **Multi-threaded Installation**: Support for parallel installation of `.exe` files, improving installation speed for multiple files.
- **Admin Privileges Support**: New option to run installation scripts with elevated admin privileges, especially for system-level apps.
- **File Backup**: Added a backup feature to create a copy of the original files before installation begins.
- **Error Handling & Logging**: Enhanced error handling with descriptive messages and the ability to log installation steps for troubleshooting.
- **Icon Support**: Now users can choose a custom icon for the installer `.bat` files.

### Changed
- **Improved UI Feedback**: Enhanced status updates and color-coded output to help users understand the current state of the installation process.
- **Refined Logging Mechanism**: Introduction of a more detailed logging system for each installation, allowing better tracking and issue resolution.
- **Optimized File Copying**: Performance improvements during the file copying process, reducing installation time for large `.exe` files.
- **Code Modularization**: Refactored code to improve structure, separating concerns into different modules (`installer.py`, `utils.py`, `config.py`).

### Fixed
- **File Path Handling**: Resolved issues with incorrect file path formatting and issues arising from file path inconsistencies during the batch script creation.
- **Parallel Installation Bugs**: Fixed race conditions that prevented proper parallel installation of multiple `.exe` files.
- **Admin Privileges**: Corrected an issue where certain systems would fail to elevate privileges when attempting to run installation with admin access.

## [1.0.0] - 2025-02-01
### Added
- **Batch File Creation**: Users can create a `.bat` file that automates the installation of selected `.exe` files.
- **Icon Integration**: Added support for selecting custom icons for the installer `.bat` files.
- **Multi-Threaded Installation**: Improved file installation by copying multiple `.exe` files concurrently using threading.
- **Admin Privileges**: Implemented a feature to run installers with administrator privileges using the `runas` command.
- **File Selection Dialogs**: Integrated `tkinter.filedialog` to select files and installation directories with a graphical interface.
- **Installation Logging**: Introduced logging of the installation process to a file, making it easier to troubleshoot issues.

### Changed
- **Code Structure**: Refactored code into multiple files for better readability and maintainability:
  - `installer.py`: Handles batch file creation and installer functionality.
  - `utils.py`: Contains helper functions for file and directory management.
  - `config.py`: Stores configuration settings for the project.
- **User Prompts**: Streamlined and improved user prompts to clarify options and steps throughout the installation process.
- **Error Handling**: Added more descriptive error messages to improve user experience when something goes wrong during installation.

### Fixed
- **Admin Privileges**: Fixed an issue where `runas` did not properly escalate privileges on all systems.
- **File Dialog Issues**: Addressed a bug where file dialogs would not display files correctly or cause crashes under certain conditions.
- **Path Handling**: Fixed issues related to file path handling, ensuring paths are correctly formatted and valid for both Windows and Unix-like systems.

## [0.1.0] - 2025-01-31
### Added
- **Initial Version**: Introduced the basic functionality for creating `.bat` files that can execute `.exe` files automatically.
- **File Selection**: Users can select `.exe` files and target directories for installation using file dialog prompts.
- **Basic Installer Creation**: Ability to generate basic `.bat` files for automatic installation.

### Changed
- **Basic Code Structure**: Initial architecture designed with room for future extensions, including error handling and parallel installations.
- **Minimal Error Handling**: Basic checks added for missing files or directories, but not extensive.

### Fixed
- **Path Issues**: Addressed a few minor bugs related to incorrect file paths in the initial version.
- **File Copying**: Fixed issues with file copying not functioning as expected in certain scenarios.

---

## [Known Issues]
### Unresolved
- **Admin Privileges on Older Systems**: Some older Windows systems may fail to gain admin privileges using the `runas` command.
- **File Dialog Compatibility**: There are occasional issues with file dialogs on older Windows versions, causing unexpected behavior when selecting files or directories.
  
---

## [Security Updates]
### [1.0.0] - 2025-02-01
- **No Known Vulnerabilities**: As of the current version, no security vulnerabilities have been reported.

---

## [Future Features]
- **Backup Installation**: Ability to automatically back up existing files before performing installation, providing a safety net.
- **Silent Installation**: A feature to run the installation without user interaction (i.e., silent install) for advanced users.
- **Extended Logging**: More detailed logging with the ability to generate logs for later analysis.

---

## [Contributors]
- **Alirezashamsadinloo**: Lead Developer, Project Maintainer.

