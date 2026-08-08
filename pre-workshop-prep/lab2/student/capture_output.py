###
# Name: Joseph Johnson
# Date: 8/7/2026
#
# AI tool: Sonnet 5 Medium
# Percentage of code AI: 100%
#
# Description: Runs a given Python script, captures everything it prints
# to the console, and saves that output into a text file inside an
# "output/" folder, named after the original script.
###

"""
Capture Script Output to a File
---------------------------------
Goal: automatically run a Python file, grab everything it prints while
running, and save that as a .txt log inside an "output/" folder — named
to match the script that produced it.

Why this is useful: it gives you a permanent record of what a script
printed (results, logs, errors) without needing to copy-paste from the
terminal, and keeps all those logs organized in one place instead of
scattered or lost when the terminal closes.

Usage:
    python3 capture_output.py path/to/some_script.py

This will create:
    output/some_script.txt
containing everything that script printed when it ran.
"""

import sys
import os
import io
import contextlib
import runpy


def capture_script_output(script_path):
    """
    Runs the given script and captures everything it prints (stdout),
    returning that captured text as a string.
    """
    # io.StringIO() acts like an in-memory text file — anything "printed"
    # gets written here instead of to the real terminal, so we can grab it
    # afterward as a string.
    captured = io.StringIO()

    # redirect_stdout temporarily sends all print() output into `captured`
    # instead of the terminal, for the duration of the `with` block only.
    with contextlib.redirect_stdout(captured):
        try:
            # runpy.run_path actually executes the target script, just like
            # running `python3 script.py` would, but from inside our program.
            runpy.run_path(script_path, run_name="__main__")
        except Exception as e:
            # If the script errors out, we still want a record of that in
            # the log rather than crashing this wrapper script silently.
            print(f"\n[ERROR while running script: {e}]")

    return captured.getvalue()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 capture_output.py path/to/script.py")
        sys.exit(1)

    script_path = sys.argv[1]

    if not os.path.isfile(script_path):
        print(f"File not found: {script_path}")
        sys.exit(1)

    # Create the output/ folder if it doesn't already exist.
    # exist_ok=True means this won't error out if the folder is already there.
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Build the output filename from the script's name, e.g.
    # "some_script.py" -> "some_script.txt"
    script_name = os.path.splitext(os.path.basename(script_path))[0]
    output_path = os.path.join(output_dir, f"{script_name}.txt")

    print(f"Running {script_path} and capturing output...")
    output_text = capture_script_output(script_path)

    # Write the captured print output to the .txt file.
    with open(output_path, "w") as f:
        f.write(output_text)

    print(f"Done. Output saved to {output_path}")


if __name__ == "__main__":
    main()