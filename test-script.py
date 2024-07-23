"""
To run this script, you need to have Python,gcc,g++ and git installed on your system.

And install the following pip packages:
- rich

(just run `pip install rich` in your terminal)


If the command of the Python interpreter is not "Python", please modify the
"PYTHON_INTERPRETER" variable.

We will help you install esolangs by git.

@Author: fexcode
@Date: 2024.7.17 ~ 2024.7.18
"""

import os
import re
import shutil
import stat
import sys
import time
from typing import List, Callable

from rich import console


# Fill it out properly!
PYTHON_INTERPRETER: str = "python"

SOURCE_PATH            : str = os.path.join(".", "hello.any")
TEST_CACHE_DIR         : str = os.path.join(".", "test-caches")
TEST_CACHE_ESOLANGS_DIR: str = os.path.join(".", "test-caches", "esolangs")

GITEE_MIRROR : str = "https://gitee.com/fxbd/esolangs"
GITHUB_MIRROR: str = "https://github.com/fexcode/esolangs"


console = console.Console()

test_language_list: List[str] = ["python", "c++", "c", "brainfuck", "befunge"]
done_languages    : List[str] = []


def error_exit():
    sys.exit(114514)


def timer(name: str):
    def decorator(func: Callable[[], None]):
        def wrapper():
            start_time = time.time()
            func()
            end_time = time.time()

            elapsed_time = end_time - start_time
            print(f"{name}-test used: {elapsed_time:.6f}s")

        return wrapper

    return decorator


"""
to print ===========[ text ]===========  total long is 50 and text is in middle
str-long cannot be more than 40
"""
def print_beatiful_log(text: str, color: str = "blod white", long: int = 50):
    text = f"[ {text} ]"
    equals = "=" * (long - len(text)) // 2

    console.print(f"{equals}{text}{equals}", style=color)


def force_remove_dir_contents(path: str):
    for root, dirs, files in os.walk(path, topdown=False):

        for name in files:
            file_path = os.path.join(root, name)
            os.chmod(file_path, stat.S_IWRITE)
            os.remove(file_path)

        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)

    os.rmdir(path)


def clone_esolang_interpreters_for_mirror(mirror: str):
    os.system(f"git clone {mirror} {TEST_CACHE_ESOLANGS_DIR} ")
    print_beatiful_log("Cloned the esolangs interpreters!", "bold green")
    print_beatiful_log("Deleting the .git directory...", "bold blue")

    force_remove_dir_contents(os.path.join(TEST_CACHE_ESOLANGS_DIR, ".git"))


def clone_esolang_interpreters():
    print_beatiful_log("Cloning the esolangs interpreters...", "bold blue")

    try:
        clone_esolang_interpreters_for_mirror(GITEE_MIRROR)
    except OSError as e:
        console.print(
            f"Cannot clone from gitee.com.\n{e}\nTrying to clone from github.com...",
            style="bold red",
        )

        try:
            clone_esolang_interpreters_for_mirror(GITHUB_MIRROR)
        except OSError as e:
            console.print(
                f"Cannot clone from github.com, too.\n{e}\nPlease check your internet connection or try again later.",
                style="bold red",
            )
            error_exit()


def check_the_environment():
    console.print("Checking the environment...", style="bold blue")

    # Check hello.any file is present and it is in the current directory
    if not os.path.isfile(SOURCE_PATH):
        console.print(
            f"{SOURCE_PATH} file is not present in the current directory.", style="bold red"
        )
        error_exit()

    # Check if git is installed
    if not shutil.which("git"):
        console.print(
            "Sorry, git is not installed on your system. Please install it first.",
            style="bold red",
        )
        error_exit()

    # Check if gcc is installed
    if not shutil.which("gcc"):
        console.print("gcc is not installed on your system.", style="bold red")
        test_language_list.remove("c")
        test_language_list.remove("befunge")

    # Check if g++ is installed
    if not shutil.which("g++"):
        console.print("g++ is not installed on your system.", style="bold red")
        test_language_list.remove("c++")

    # Check if any language can test
    if not test_language_list:
        console.print("No language can test.", style="bold red")
        error_exit()

    console.print("Environment check Done!", style="bold green")
    console.print("We will test the following languages:", style="bold blue")
    for lang in test_language_list:
        console.print("\t" + lang, style="bold bright_white")


def init():
    if os.path.exists(TEST_CACHE_DIR):
        console.print(
            f"The {TEST_CACHE_DIR} directory already exists. Deleting it...",
            style="bold yellow",
        )
        force_remove_dir_contents(TEST_CACHE_DIR)

        console.print("Creating test-caches directory...", style="bold bright_black")
        os.makedirs(TEST_CACHE_DIR)

    clone_esolang_interpreters()


def delete_test_cache_directory():
    print_beatiful_log("Cleaning up...", "bold yellow")

#   try:
#       shutil.rmtree(TEST_CACHE_DIR)
#   except OSError as e:
#       print(
#           f"FUCKIT! Cannot deleted {TEST_CACHE_DIR} directory by shutil.rmtree() method \n because [[ {e} ]].\n But don't be worried.",
#       )
#       print_beatiful_log("Trying force delete...", "bold yellow")

    force_remove_dir_contents(TEST_CACHE_DIR)
    console.print("Cleaned up!", style="bold green")


@timer("Python")
def test_python_language():
    print_beatiful_log("TESTING PYTHON", "bold blue")

    output = os.path.join(TEST_CACHE_DIR, 'python-output.txt')

    # Python does not need any installation, just run the hello.any file
    console.log(f"Running {SOURCE_PATH} file...")
    os.system(f"{PYTHON_INTERPRETER} hello.any > {output}")

    # Check if the output is correct
    console.log("Checking the output...")
    with open(output, "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("PYTHON TEST PASSED", "bold green")
            done_languages.append("python")
        else:
            print_beatiful_log("PYTHON TEST FAILED", "bold red")


@timer("C")
def test_c_language():
    print_beatiful_log("TESTING C", "bold blue")

    c_source = os.path.join(TEST_CACHE_DIR, "hello.c")
    target   = os.path.join(TEST_CACHE_DIR, "hello") + (".exe" if os.name == "nt" else "")
    output   = os.path.join(TEST_CACHE_DIR, "c_output.txt")

    # Copy hello.any file to ./test-caches/hello.c
    console.log(f"Copying {SOURCE_PATH} file...")
    shutil.copyfile(SOURCE_PATH, c_source)

    # Compile hello.c file
    console.log(f"Compiling {c_source} file...")
    os.system(f"gcc -o {target} {c_source}")

    # Running hello.exe file
    console.log("Running hello.exe file...")
    os.system("{target} > {output}")

    # Check if the output is correct
    console.log("Checking the output...")
    with open(output, "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("C TEST PASSED", "bold green")
            done_languages.append("c")
        else:
            print_beatiful_log("C TEST FAILED", "bold red")


@timer("C++")
def test_cpp_language():
    print_beatiful_log("TESTING C++", "bold blue")

    cpp_source = os.path.join(TEST_CACHE_DIR, "hello.cpp")
    target     = os.path.join(TEST_CACHE_DIR, "hello") + (".exe" if os.name == "nt" else "")
    output     = os.path.join(TEST_CACHE_DIR, "cpp_output.txt")

    # Copy hello.any file to ./test-caches/hello.cpp
    console.log(f"Copying {SOURCE_PATH} file...")
    shutil.copyfile(SOURCE_PATH, cpp_source)

    # Compile hello.cpp file
    console.log(f"Compiling {cpp_source} file...")
    os.system("g++ -o {target} {cpp_source}")

    # Running hello.exe file
    console.log(f"Running {target} file...")
    os.system("{target} > {output}")

    # Check if the output is correct
    console.log("Checking the output...")
    with open(output, "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("C++ TEST PASSED", "bold green")
            done_languages.append("c++")
        else:
            print_beatiful_log("C++ TEST FAILED", "bold red")


@timer("Brainfuck")
def test_brainfuck_language():
    # esolang interpreters have installed in ./test-caches/esolangs already.

    print_beatiful_log("TESTING BRAINF**K", "bold blue")

    root_dir    = os.path.join(TEST_CACHE_ESOLANGS_DIR, "brainfuck")
    interpreter = os.path.join(root_dir, "main.py")
    bf_file     = os.path.join(root_dir, "hello.bf")
    output      = os.path.join(root_dir, "output.txt")

    # Copy hello.any file to ./test-caches/esolangs/brainfuck/hello.bf
    shutil.copyfile(SOURCE_PATH, BRAINFUCK_FILE)

    # Running hello.bf file
    os.system(f"{PYTHON_INTERPRETER} {interpreter} {bf_file} > {output}")

    # Check if the output is correct
    with open(output, "r") as f:
        output = f.read()

        if "Hello world!\n" == output:
            print_beatiful_log("BRAINF**K TEST PASSED", "bold green")
            done_languages.append("brainfuck")
        else:
            console.print(
                "Test failed, maybe your mirror cannot use or your internet is not good. "
                "And you can check hello.any file and try again."
            )
            print_beatiful_log("Here is the output of the program:", "bold yellow")
            console.print(output)
            print_beatiful_log("Please check your output!.", "bold yellow")
            print_beatiful_log("BRAINF**K TEST FAILED", "bold red")


@timer("Befunge")
def test_befunge_language():
    print_beatiful_log("TESTING BEFUNGE", "bold blue")

    root_dir         = os.path.join(TEST_CACHE_ESOLANGS_DIR, "befunge")
    interpreter_file = os.path.join(root_dir, "main.c")
    interpreter      = os.path.join(root_dir, "main") + (".exe" if os.name == "nt" else "")
    bf_file          = os.path.join(root_dir, "hello.bf")
    output           = os.path.join(root_dir, "output.txt")

    # copy hello.any file to ./test-caches/esolangs/hello.bf
    shutil.copyfile(SOURCE_PATH, bf_file)

    # to run befunge, we need to have gcc installed.

    # First we need to compile the main.c file.
    console.log("Compiling main.c file...")
    os.system(f"gcc -o {interpreter} {interpreter_file}")

    # Then we can run the program.
    # To run hello.bf, just run `{interpreter} hello.bf`
    console.log("Running the program...")
    os.system(
        c := (f"{interpreter} {bf_file} > {output}")
    )
    console.log(f"Ran {c}")

    # Check if the output is correct
    console.log("Checking the output...")
    with open(
        f"{output}", "r", encoding="utf-16-le", errors="ignore"
    ) as f:
        output = f.read()

        target = "Hello world!"

        if target in output:
            print_beatiful_log("BEFUNGE TEST PASSED", "bold green")
            done_languages.append("befunge")
        else:
            console.print(
                "Test failed the output is not correct. ",
                style="bold red",
            )
            print_beatiful_log("Here is the output of the program:", "bold yellow")
            console.print(output)
            print_beatiful_log("Please check your output!.", "bold yellow")


def summary():
    print_beatiful_log("SUMMARY", "bold blue")

    console.print("We have tested the following languages:", style="bold blue")

    for lang in test_language_list:

        if lang in done_languages:
            done_languages.remove(lang)
            console.print(f"\t{lang} \t\t[PASSED]", style="bold green")
        else:
            console.print(f"\t{lang} \t\t[FAILED]", style="bold red")

    print_beatiful_log("ALL DONE! | THANKS FOR USING!", "bold green")


@timer("ALL")
def main():
    check_the_environment()
    init()

    test_python_language()
    test_c_language()
    test_cpp_language()
    test_brainfuck_language()
    test_befunge_language()

    delete_test_cache_directory()
    summary()


if __name__ == "__main__":
    main()
