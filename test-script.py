"""
To run this script, you need to have Python,gcc,g++ and git installed on your system.

And install the following pip packages:
- rich

(just run `pip install rich` in your terminal)

we will help you install esolangs by git

@Author: fexcode
@Date: 2024.7.17 ~ 2024.7.18
"""

import os
from rich import console
import shutil
import sys
import os
import stat
import time


def test_function(lang):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{lang}-test used: {elapsed_time:.6f}s")
            return result

        return wrapper

    return decorator


console = console.Console()

PYTHON_OR_PYTHON3 = "python"

test_language_list = ["python", "c++", "c", "brainfuck", "befunge"]
done_languages = []

TEST_CACHE_DIR = "./test-cache"
TEST_CACHE_ESOLANGS_DIR = "./test-cache/esolangs"

GITEE_MIRROR = "https://gitee.com/fxbd/esolangs"
GITHUB_MIRROR = "https://github.com/fexcode/esolangs"


# CONFIG = get_or_ask_config()


def print_beatiful_log(text, color="blod white", long=52):
    # to print ===========[ text ]===========  total long is 50 and text is in middle
    # str-long cannot be more than 40
    half_long = long // 2
    str_long = len(text) + 4
    half_square_long = half_long - str_long // 2

    console.print("=" * half_square_long, style=color, end="")
    console.print(f"[ {text} ]", style=color, end="")
    console.print("=" * half_square_long, style=color)


def if_the_language_is_supported(language):
    if language in test_language_list:
        return True
    else:
        return False


def force_remove_dir_contents(path):
    # 遍历目录树
    for root, dirs, files in os.walk(path, topdown=False):
        # 删除所有文件
        for name in files:
            file_path = os.path.join(root, name)
            # 尝试设置文件为可写
            os.chmod(file_path, stat.S_IWRITE)
            # 删除文件
            os.remove(file_path)
        # 删除所有空目录
        for name in dirs:
            dir_path = os.path.join(root, name)
            os.rmdir(dir_path)
    # 最后删除根目录
    os.rmdir(path)


def clone_esolang_interpreters():
    TEST_CACHE_ESOLANGS_DIR = "./test-cache/esolangs/"
    print_beatiful_log("Cloning the esolangs interpreters...", "bold blue")
    try:
            os.system(f"git clone {GITHUB_MIRROR} {TEST_CACHE_ESOLANGS_DIR} ")
            print_beatiful_log("Cloned the esolangs interpreters!", "bold green")
            print_beatiful_log("Deleting the .git directory...", "bold blue")
            force_remove_dir_contents(f"{TEST_CACHE_ESOLANGS_DIR}/.git")
    except OSError as e:
            console.print(
                "Cannot clone from github.com. Trying to clone from gitee.com...",
                style="bold red",
            )
            try:
                os.system(f"git clone {GITEE_MIRROR} {TEST_CACHE_ESOLANGS_DIR} ")
                print_beatiful_log("Deleting the .git directory...", "bold blue")
                force_remove_dir_contents(f"{TEST_CACHE_ESOLANGS_DIR}/.git")
            except OSError as e:
                console.print(
                    "Cannot clone from gitee.com. Please check your internet connection or try again later.",
                    style="bold red",
                )
                sys.exit(114514)


def check_the_environment_and_init():
    global test_language_list

    console.print("Checking the environment...", style="bold blue")
    # Check if gcc is installed
    if not shutil.which("gcc"):
        console.print("gcc is not installed on your system.", style="bold red")
        test_language_list.remove("c")
        test_language_list.remove("befunge")

    # Check if g++ is installed
    if not shutil.which("g++"):
        console.print("g++ is not installed on your system.", style="bold red")
        test_language_list.remove("c++")

    # Check if git is installed
    if not shutil.which("git"):
        console.print(
            "Sorry, git is not installed on your system.Please install it first.",
            style="bold red",
        )
        test_language_list.remove("brainfuck")
        test_language_list.remove("befunge")
        sys.exit(114514)
    else:
        clone_esolang_interpreters()

    # Check hello.any file is present and it is in the current directory
    if not os.path.isfile("hello.any"):
        console.print(
            "hello.any file is not present in the current directory.", style="bold red"
        )
        sys.exit(114514)

    if not test_language_list:
        console.print("No language can test.", style="bold red")
        sys.exit(114514)

    # Create test-cache directory if it does not exist
    if not os.path.exists("./test-cache"):
        console.print("Creating test-cache directory...", style="bold bright_black")
        os.makedirs("./test-cache")

    # console.input("Please check your BRAINFUCK mirrors and press a key to continue.")

    console.print("Environment check Done!", style="bold green")
    console.print("We will test the following languages:", style="bold blue")
    for lang in test_language_list:
        console.print("\t" + lang, style="bold bright_white")


def delete_test_cache_directory():
    print_beatiful_log("Cleaning up...", "bold yellow")
    try:
        shutil.rmtree("./test-cache")
    except OSError as e:
        print(
            f"FUCKIT! Cannot deleted ./test-cache directory by shutil.rmtree() method \n because [[ {e} ]].\n But don't be worried.",
        )
        print_beatiful_log("Trying force delete...", "bold yellow")
        force_remove_dir_contents("./test-cache")
        console.print("Cleaned up!", style="bold green")

    print_beatiful_log("ALL TESTS HAS BEEN DONE!!!", "bold green")


@test_function("Python")
def test_python_language():
    print_beatiful_log("TESTING PYTHON", "bold blue")

    # Python does not need any installation, just run the hello.any file
    console.log("Running hello.any file...")
    os.system("python hello.any > ./test-cache/python_output.txt")

    console.log("Checking the output...")
    # Check if the output is correct
    with open("./test-cache/python_output.txt", "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("PYTHON TEST PASSED", "bold green")
            done_languages.append("python")
        else:
            print_beatiful_log("PYTHON TEST FAILED", "bold red")


@test_function("C")
def test_c_language():
    print_beatiful_log("TESTING C", "bold blue")

    console.log("Copying hello.any file...")
    # Copy hello.any file to ./test-cache/hello.c
    shutil.copyfile("./hello.any", "./test-cache/hello.c")

    console.log("Compiling hello.c file...")
    # Compile hello.c file
    os.system(
        "gcc -o ./test-cache/hello.exe ./test-cache/hello.c"
        if os.name == "nt"
        else "gcc -o ./test-cache/hello ./test-cache/hello.c"
    )

    console.log("Running hello.exe file...")
    os.system(
        r".\test-cache\hello.exe > ./test-cache/c_output.txt"
        if os.name == "nt"
        else "./test-cache/hello > ./test-cache/c_output.txt"
    )

    console.log("Checking the output...")
    # Check if the output is correct
    with open("./test-cache/c_output.txt", "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("C TEST PASSED", "bold green")
            done_languages.append("c")
        else:
            print_beatiful_log("C TEST FAILED", "bold red")
            return


@test_function("C++")
def test_cpp_language():
    print_beatiful_log("TESTING C++", "bold blue")

    console.log("Copying hello.any file...")
    # Copy hello.any file to ./test-cache/hello.cpp
    shutil.copyfile("./hello.any", "./test-cache/hello.cpp")

    console.log("Compiling hello.cpp file...")
    # Compile hello.cpp file
    os.system(
        "g++ -o ./test-cache/hello.exe ./test-cache/hello.cpp"
        if os.name == "nt"
        else "g++ -o ./test-cache/hello ./test-cache/hello.cpp"
    )

    console.log("Running hello.exe file...")
    os.system(
        r".\test-cache\hello.exe > ./test-cache/cpp_output.txt"
        if os.name == "nt"
        else "./test-cache/hello > ./test-cache/cpp_output.txt"
    )

    console.log("Checking the output...")
    # Check if the output is correct
    with open("./test-cache/cpp_output.txt", "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("C++ TEST PASSED", "bold green")
            done_languages.append("c++")
        else:
            print_beatiful_log("C++ TEST FAILED", "bold red")
            return


@test_function("Brainfuck")
def test_brainfuck_language():
    # esolang interpreters have installed in ./test-cache/esolangs already.

    print_beatiful_log("TESTING BRAINF**K", "bold blue")

    BRAINFUCK_ROOT_DIR = f"{TEST_CACHE_ESOLANGS_DIR}/brainfuck"

    shutil.copyfile("./hello.any", f"{BRAINFUCK_ROOT_DIR}/hello.bf")

    os.system(
        f"python {BRAINFUCK_ROOT_DIR}/main.py {BRAINFUCK_ROOT_DIR}/hello.bf > {BRAINFUCK_ROOT_DIR}/output.txt"
        if PYTHON_OR_PYTHON3 == "python"
        else f"python3 {BRAINFUCK_ROOT_DIR}/main.py {BRAINFUCK_ROOT_DIR}/hello.bf > {BRAINFUCK_ROOT_DIR}/output.txt"
    )
    console.log(
        f"Output of the program is in {BRAINFUCK_ROOT_DIR}/output.txt file, but we will delete it after we checked the output."
    )

    # Check if the output is correct
    with open(f"{BRAINFUCK_ROOT_DIR}/output.txt", "r") as f:
        output = f.read()

        if "Hello world!\n" == output:
            print_beatiful_log("BRAINF**K TEST PASSED", "bold green")
            done_languages.append("brainfuck")
        else:
            console.print(
                "Test failed, maybe your mirror cannot use or your internet is not good.And you can check hello.any file and try again."
            )
            print_beatiful_log("Here is the output of the program:", "bold yellow")
            console.print(output)
            print_beatiful_log("Please check your output!.", "bold yellow")
            print_beatiful_log("BRAINF**K TEST FAILED", "bold red")
            return


@test_function("Befunge")
def test_befunge_language():
    print_beatiful_log("TESTING BEFUNGE", "bold blue")

    BEFUNGE_ROOT_DIR = f"{TEST_CACHE_ESOLANGS_DIR}/befunge"

    # copy hello.any file to {BEFUNGE_ROOT_DIR}/hello.bf
    shutil.copyfile("./hello.any", f"{BEFUNGE_ROOT_DIR}/hello.bf")

    # to run befunge, we need to have gcc installed.

    # First we need to compile the main.c file.
    console.log("Compiling main.c file...")
    os.system(
        f"gcc -o {BEFUNGE_ROOT_DIR}/main.exe {BEFUNGE_ROOT_DIR}/main.c"
        if os.name == "nt"
        else f"gcc -o {BEFUNGE_ROOT_DIR}/main {BEFUNGE_ROOT_DIR}/main.c"
    )

    # Then we can run the program.
    # To run hello.bf , just run `main.exe hello.bf`
    console.log("Running the program...")
    os.system(
        c := (
            f'powershell -Command "{BEFUNGE_ROOT_DIR}/main.exe {BEFUNGE_ROOT_DIR}/hello.bf > {BEFUNGE_ROOT_DIR}/output.txt"'
            if os.name == "nt"
            else f"{BEFUNGE_ROOT_DIR}/main {BEFUNGE_ROOT_DIR}/hello.bf > {BEFUNGE_ROOT_DIR}/output.txt"
        )
    )
    console.log(f"Ran {c}")

    # Check if the output is correct
    console.log("Checking the output...")
    with open(f"{BEFUNGE_ROOT_DIR}/output.txt", "r", encoding="ascii") as f:
        output = f.read()
        if "Hello world!\n" == output:
            print_beatiful_log("BEFUNGE TEST PASSED", "bold green")
            done_languages.append("befunge")
        else:
            console.print(
                "Test failed, maybe your mirror cannot use or your internet is not good.And you can check hello.any file and try again."
            )
            print_beatiful_log("Here is the output of the program:", "bold yellow")
            console.print(output)
            print_beatiful_log("\nPlease check your output!.", "bold yellow")


def summary():
    print_beatiful_log("SUMMARY", "bold blue")
    console.print("We have tested the following languages:", style="bold blue")
    for lang in test_language_list:
        if lang in done_languages:
            done_languages.remove(lang)
            if lang == "brainfuck":
                console.print(f"\t{lang} \t[PASSED]", style="bold green")
                continue
            if lang == "befunge":
                console.print(f"\t{lang} \t[PASSED]", style="bold green")
                continue
            else:
                console.print(f"\t{lang} \t\t[PASSED]", style="bold green")
        else:
            if lang == "brainfuck":
                console.print(f"\t{lang} \t[FAILED]", style="bold red")
            if lang == "befunge":
                console.print(f"\t{lang} \t[FAILED]", style="bold red")
            else:
                console.print(f"\t{lang} \t\t[FAILED]", style="bold red")

    print_beatiful_log("ALL DONE! | THANKS FOR USING!", "bold green")


@test_function("ALL")
def main():
    check_the_environment_and_init()

    test_python_language()
    test_c_language()
    test_cpp_language()
    test_brainfuck_language()
    test_befunge_language()

    delete_test_cache_directory()
    summary()


if __name__ == "__main__":
    main()
