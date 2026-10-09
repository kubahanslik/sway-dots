import subprocess
import os
import sys


test_input_file = "input.txt"
test_output_file = "output.txt"

def main():
    files = os.listdir(os.getcwd())
    if test_input_file not in files:
        print(f"[!] No {test_input_file} found")
    if test_output_file not in files:
        print(f"[!] No {test_output_file} found")

    for f in files:
        if f.startswith("main"):
            if f == "main.py":
                subprocess.run([sys.executable, f], stdin=test_input_file)



if __name__=='__main__':
    main()
