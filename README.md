# AUTO push for GitHub statistics
## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Automation with alias](#automation-with-alias)
6. [Auto Generation of Documentation](#auto-generation-of-documentation)
7. [Troubleshooting](#troubleshooting)
8. [Versions](#versions)
9. [Authors](#authors)

## Introduction
This project automates the generation and push of Python scripts to a GitHub repository using Ollama's `deepseek-r1` model. The script generates a Python file based on a predefined prompt, adds it to the repository, commits, and pushes it automatically.

## Prerequisites
- Python 3.10
- Ollama installed and configured
- Git installed and configured
- Access to a GitHub repository

## Installation
1. Clone the repository to your local machine:
    ```bash
    git clone <REPOSITORY_URL>
    ```
2. Navigate to the project folder:
    ```bash
    cd /home/melissa/Documents/automat-gh/AUTO
    ```

## Usage
1. Run the script with the appropriate parameters to generate, repair, document, clean, or update a Python file:
    ```bash
    python3 generate_code.py -g  # To generate a script
    python3 generate_code.py -f  # To repair an existing script
    python3 generate_code.py -d  # To generate documentation for a script
    python3 generate_code.py -c  # To clean the repository
    python3 generate_code.py -u  # To update the code generation model
    python3 generate_code.py -a  # To generate, fix, and document a script
    ```
2. The script will:
    - Check and download the `deepseek-r1` model if necessary.
    - Generate, repair, or document a Python script based on a predefined prompt.
    - Create a file with a unique name including a timestamp (for generation).
    - Add, commit, and push the file to the GitHub repository.

## Automation with Alias
To simplify running the script, you can create an alias in your terminal:
1. Open your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`).
2. Add the following line:
    ```bash
    alias mkstat="alias mkstat='python3 /home/melissa/Documents/automat-gh/AUTO/generate_code.py "$@"'
"
    ```
3. Reload your shell configuration file:
    ```bash
    source ~/.bashrc
    ```
4. Now you can run the script with the command `mkstat`.

## Auto Generation of Documentation
The script includes an auto-generation feature for documentation when specific flags are used. Here's how it works:

1. **Enabling Documentation Generation**: Use the `-d` flag while running the script to enable auto-documentation.
   
   ```bash
   python3 generate_code.py -d
   ```

2. **Documentation Flags**:
   - `-d`: Enable documentation generation for the generated file.

3. **Output Directories**:
   - The generated Python files will be placed in a subdirectory named `generated/`.
   - Documentation files (e.g., `.md`, `.rst`, `.mdwn`) will be created in the same directory as the script output.

4. **Customization**: Users can customize the documentation format by modifying the template files located in the `templates` directory within the project.

5. **Clean-Up**: The `-c` flag can be used to clean up unnecessary directories after generation:
   
   ```bash
   python3 generate_code.py -c
   ```

## Troubleshooting
[Troubleshooting](#troubleshooting)

## Version History
1. 1.0.0 - Initial release with core functionality.
2. 1.1.0 - Added documentation auto-generation feature.

## Authors
- [Melissa Carter](https://github.com/melissacarter) - Original author and maintainer