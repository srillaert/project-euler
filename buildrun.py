import subprocess
import time

executables = ["p007r", "p010r", "p035r", "p037r"]

for executable in executables:
    print(executable)
    result = subprocess.run(["/usr/bin/make", executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        start_time = time.time()
        result = subprocess.run(["./" + executable], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Output:", result.stdout.strip())
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.3f}s\n")
    else:
        print(f"Error building:")
        print(result.stderr)
        break
