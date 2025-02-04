# AUTO push for GitHub statistics
## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Automation with alias](#automation-with-alias)
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
    python3 generate_code.py -u  # To push the update of main script and documentation (optional add description of the update)
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

## Version History
- Version 1.5: Added documentation auto-generation feature.
- Version 1.4: Added the `--all` option to generate, fix, and document a script
- Version 1.3: Clean code
- Version 1.2: Added arguments to edit and document the generated code
- Version 1.1: Switched to local `deepseek-r1`.
- Version 1.0: Project initialization with the `deepseek-coder` model.


## Authors
- [Melissa Colin](https://github.com/ddsmlf) - Original author and maintainer