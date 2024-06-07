#!/usr/bin/python3
import glob
from pathlib import Path
import subprocess
import sys
import time

def run_solver(run_args):
    start_time = time.time()
    result = subprocess.run(run_args, capture_output=True, text=True)
    elapsed_time = time.time() - start_time
    return (result.stdout.strip(), elapsed_time)

def run_cargo_and_solver(executable):
    result = subprocess.run(["/usr/bin/cargo", "build", "-r", "--bin", executable], capture_output=True, text=True)
    if result.returncode == 0:
        return run_solver(["./target/release/" + executable])
    else:
        print(f"Error building:")
        print(result.stderr)
        return

def run_make_and_solver(executable):
    result = subprocess.run(["/usr/bin/make", executable], capture_output=True, text=True)
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

def get_files_using_module(module):
    command = f"/usr/bin/grep 'mod {module}' *.rs"
    run_result = subprocess.run(command, shell=True, capture_output=True, text=True)
    result = [line.split(':')[0] for line in run_result.stdout.split('\n') if line != '']
    return result

def print_module(module):
    print(f'{"program".ljust(15)} {"output".ljust(20)} elapsed_seconds')
    matching_files = get_files_using_module(module)
    for file_name in matching_files:
        (output, elapsed_time) = get_output(file_name)
        print(f'{file_name.ljust(15)} {output.ljust(20)} {elapsed_time:.4f}')

def get_problem_outputs(problem):
    matching_files = glob.glob(problem + '*.*')
    for file_name in matching_files:
        result = get_output(file_name)
        if result != None:
            yield (file_name, ) + result

def print_problem(problem):
    print(f'{"program".ljust(15)} {"output".ljust(20)} elapsed_seconds')
    for (file_name, output, elapsed_time) in get_problem_outputs(problem):
        print(f'{file_name.ljust(15)} {output.ljust(20)} {elapsed_time:.4f}')
        yield (file_name, output, elapsed_time)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print(f"Usage  : {sys.argv[0]} problem")
        print(f"Example: {sys.argv[0]} p007")
        print()
        print(f"Usage  : {sys.argv[0]} -m module_name")
        print(f"Example: {sys.argv[0]} -m prime_sieve")
    else:
        if sys.argv[1] == "-m":
             module = sys.argv[2]
             print_module(module)
        else:
            problem = sys.argv[1]
            results = list(print_problem(problem))
            outputs = [tup[1] for tup in results]
            if not all(elem == outputs[0] for elem in outputs):
                print("Error !! Not all outputs are the same !")
            else:
                print("Correct")
