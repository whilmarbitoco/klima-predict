import os
import sys
import subprocess
import venv
import platform

# Define virtual environment directory
venv_dir = "venv"

# Create virtual environment if it doesn't exist
if not os.path.exists(venv_dir):
    print("Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)

# Determine the path to the Python executable inside the venv
if platform.system() == "Windows":
    python_executable = os.path.join(venv_dir, "Scripts", "python.exe")
    pip_executable = os.path.join(venv_dir, "Scripts", "pip.exe")
else:
    python_executable = os.path.join(venv_dir, "bin", "python")
    pip_executable = os.path.join(venv_dir, "bin", "pip")

# Install dependencies
print("Installing dependencies...")
subprocess.check_call([pip_executable, "install", "-r", "requirements.txt"])

# Start uvicorn server
print("Starting FastAPI server...")
subprocess.check_call([python_executable, "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

# os.system("uvicorn main:app --reload --host 0.0.0.0 --port 8000") 
