#!/usr/bin/python3
import glob
from pathlib import Path
import subprocess
import sys
import time

def run_solver(run_args):
    start_time = time.time()
    result = subprocess.run(run_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    elapsed_time = time.time() - start_time
    return (result.stdout.strip(), elapsed_time)

def run_cargo_and_solver(executable):
    result = subprocess.run(["/usr/bin/cargo", "build", "-r", "--bin", executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return run_solver(["./target/release/" + executable])
    else:
        print(f"Error building:")
        print(result.stderr)
        return

def run_make_and_solver(executable):
    result = subprocess.run(["/usr/bin/make", executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return run_solver(["./" + executable])
    else:
        print(f"Error building:")
        print(result.stderr)
        return

def get_output(file_name):
    path = Path(file_name)
    if path.suffix == ".py" and not path.stem.endswith("_test"):
        return run_solver(["python3", file_name])
    elif path.suffix == ".rs":
        return run_cargo_and_solver(path.stem + "r")
    elif path.suffix == ".c" and not path.stem.endswith("_lib") and not path.stem.endswith("_test"):
        return run_make_and_solver(path.stem + "c")
    else:
        return

def get_outputs(problem):
    matching_files = glob.glob(problem + '*.*')
    for file_name in matching_files:
        result = get_output(file_name)
        if result != None:
            yield (file_name, ) + result

def print_table(problem):
    print(f'{"program".ljust(15)} output\telapsed_seconds')
    for (file_name, output, elapsed_time) in get_outputs(problem):
        print(f'{file_name.ljust(15)} {output}\t{elapsed_time:.4f}')
        yield (file_name, output, elapsed_time)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Usage  : python3 {sys.argv[0]} problem")
        print(f"Example: python3 {sys.argv[0]} p007")
    else:
        problem = sys.argv[1]
        results = list(print_table(problem))
        outputs = [tup[1] for tup in results]
        if not all(elem == outputs[0] for elem in outputs):
            print("Error !! Not all outputs are the same !")
        else:
            print("Correct")
