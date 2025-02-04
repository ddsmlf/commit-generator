# AUTO push for GitHub statistics
## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
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
The script is built to be used as an alias. To create an alias, follow these steps:
1. Open your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`).
2. Add the following line:
    ```bash
    alias mkstat="alias mkstat='python3 path/to/generate_code.py -s 'path/to/your/repo'"$@"'
"
    ```
3. Reload your shell configuration file:
    ```bash
    source ~/.bashrc
    ```
4. Now you can run the script with the command `mkstat`.

To run the script, use the following command:
```bash
mkstat
```
You can also use the following options:
- `-s` or `--script`: Path to the script to generate.
- `-a` or `--all`: Generate, fix, and document the script.
- `-g` or `--generate`: Generate the script. (Default)
- `-f` or `--fix`: Fix the script.
- `-d` or `--document`: Document the script.

## Version History
- Version 1.6: Public version
- Version 1.5: Added documentation auto-generation feature.
- Version 1.4: Added the `--all` option to generate, fix, and document a script
- Version 1.3: Clean code
- Version 1.2: Added arguments to edit and document the generated code
- Version 1.1: Switched to local `deepseek-r1`.
- Version 1.0: Project initialization with the `deepseek-coder` model.


## Authors
- [Melissa Colin](https://github.com/ddsmlf) - Original author and maintainer