#!/usr/bin/env python3

import subprocess
import os
import sys


test_input_file = "input.txt"
test_output_file = "output.txt"

test_directory = "tests"

def main():
    files = os.listdir(os.getcwd())

    if test_input_file not in files:
        print(f"[!] No {test_input_file} found")
    if test_output_file not in files:
        print(f"[!] No {test_output_file} found")

    completed_process = None
    
    for f in files:
        with open(test_input_file, "r") as inf:
            if f == "main.py":
                completed_process = subprocess.run([sys.executable, f], stdin=inf, capture_output=True, text=True)
                break
            elif f == "main":
                completed_process = subprocess.run("main", stdin=inf, capture_output=True, text=True)
                break

    if completed_process == None:
        print(
'''\
[!] No appropriate main file found
    Options are: ./main, main.py
'''
)
        return

    elif completed_process.returncode != 0:
        print(f"Executed program failed with the exit code {completed_process.returncode}")


    with open(test_output_file, "r") as otf:
        for i, (l_otf, l_std) in enumerate(zip(otf.readlines(), completed_process.stdout.split("\n"))):
            l_otf = l_otf.strip()
            l_std = l_std.strip()
            if l_otf == l_std:
                print(f"✓ {i+1}: {l_otf}")
            else:
                print(f"✗ {i+1}: Expected - {l_otf} | Got - {l_std}")



if __name__=='__main__':
    main()
