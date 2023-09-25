## Installation of Dependencies for Unit Tests

To run unit tests for this project, you'll need to set up a virtual environment and install the necessary dependencies. Here's a step-by-step guide:

### 1. Prerequisites

- Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/) if it's not already installed.

### 2. Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to isolate project dependencies from your system-wide Python installation. To create a virtual environment, open your terminal or command prompt and run the following commands:

```bash
# On macOS and Linux
python3 -m venv venv

# On Windows
python -m venv venv
```

This will create a virtual environment named `venv` in your project directory.

### 3. Activate the Virtual Environment

Before installing dependencies, activate the virtual environment:

- On macOS and Linux:
  ```bash
  source venv/bin/activate
  ```

- On Windows (cmd.exe):
  ```bash
  venv\Scripts\activate
  ```

- On Windows (PowerShell):
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

### 4. Install Required Dependencies

Now, you can install the required dependencies using pip, which should be automatically included in your virtual environment:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains a list of dependencies needed for running unit tests.

### 5. Run typing verification with mypy

You're all set! You can now run mypy for the project using the following command:

```bash
# Installing mypy in local conda env
python3.8 -m pip install mypy
```

```bash
# Running mypy over key files
python3.8 -m mypy utils/budget_import.py
python3.8 -m mypy routes/ynab.py
```

### 6. Deactivate the Virtual Environment

When you're done working on the project and want to exit the virtual environment, you can run:

```bash
deactivate
```

This will return you to your system's Python environment.

---
