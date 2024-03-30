import sys
import os
import subprocess

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    input_dir = os.path.join(current_dir, "input")
    python_executable = sys.executable
    main_script = os.path.join(current_dir, "main.py")
    subprocess.run([python_executable, main_script, "-d", output_dir, input_dir])