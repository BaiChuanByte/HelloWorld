"""
To run this script, you need to have Python,gcc,g++ and git installed on your system.

And install the following pip packages:
- rich

(just run `pip install rich in your terminal)

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
import json


console = console.Console()

PYTHON_OR_PYTHON3 = "python"
BF_GEI_MIRROR = "https://github.com/pocmo/Python-Brainfuck.git"
BF_MAIN_FILE = "brainfuck.py"

test_language_list = ["python", "c++", "c", "brainfuck"]


"""

PYTHON_OR_PYTHON3 = "python"

mirrors = {
    "brainfuck": [
        {
            "NEED_LANGUAGE": "python" if PYTHON_OR_PYTHON3 == "python" else "python3",
            "GIT_MIRROR": "https://github.com/pocmo/Python-Brainfuck.git",
            "HOW_TO_RUN": "brainfuck.py",
        },
    ]
}

BRAINFUCK_GIT_MIRROR = (
    "https://github.com/pocmo/Python-Brainfuck"  # MUST WRITE BY PYTHON!!!
)
BRAINFUCK_MAIN_FILE_AND_ARGS = "brainfuck.py"
"""

"""
def get_or_ask_config():
    # check config.json file is exist
    global mirrors
    if os.path.isfile("config.json"):
        with open("config.json", "r") as f:
            global_config = json.load(f)
            return global_config
    else:
        config = {}

        console.print("No config.json file found", style="bold red")
        console.print("Createing...")

        # Create python config
        for i in range(3):
            p_or_p3 = console.input(
                "seting python or python3 as default(python/python3): "
            )
            if p_or_p3_l := (p_or_p3.lower()) not in ["python", "python3"]:
                console.print(
                    "Invalid input, seting python as default, please try again.",
                    style="bold red",
                )
                continue
            config["python-or-python3"] = p_or_p3_l

        # Crate brainfuck config
        for i in range(3):
            console.print("\nPlease choose a brainfuck mirror: ")

            for i, mirror in enumerate(mirrors["brainfuck"]):
                console.print(f"{i+1}. {mirror['GIT_MIRROR']}")

            choice = console.input("Please choose a mirror by number: ")
            if not (0 < int(choice) <= len(mirrors["brainfuck"])):
                console.print(
                    "Invalid input, seting the first mirror as default, please try again.",
                    style="bold red",
                )
                continue
            mirror = mirrors["brainfuck"][int(choice) - 1]
            config["brainfuck"] = {}
            config["brainfuck"]["GIT_MIRROR"] = mirror["GIT_MIRROR"]
            config["brainfuck"]["HOW_TO_RUN"] = mirror["HOW_TO_RUN"]

            with open("config.json", "w") as f:
                json.dump(config, f, indent=4)
            return config
"""

# CONFIG = get_or_ask_config()


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


def check_the_environment():
    global test_language_list

    console.print("Checking the environment...", style="bold blue")
    # Check if Python is installed
    if not shutil.which("python"):
        console.print("Python is not installed on your system.", style="bold red")
        test_language_list.remove("python")
        test_language_list.remove("brainfuck")

    # Check if gcc is installed
    if not shutil.which("gcc"):
        console.print("gcc is not installed on your system.", style="bold red")
        test_language_list.remove("c")

    # Check if g++ is installed
    if not shutil.which("g++"):
        console.print("g++ is not installed on your system.", style="bold red")
        test_language_list.remove("c++")

    # Check if git is installed
    if not shutil.which("git"):
        console.print("git is not installed on your system.", style="bold red")
        test_language_list.remove("brainfuck")

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
    console.print("Deleting test-cache directory...", style="bold bright_white")
    try:
        shutil.rmtree("./test-cache")
    except OSError as e:
        print(
            f"FUCKIT! Cannot deleted ./test-cache directory by shutil.rmtree() method \n because [[ {e} ]].\n But don't be worried.\n =============[ Trying force delete... ]==",
        )
        force_remove_dir_contents("./test-cache")
        console.print("Cleaned up!", style="bold green")
    console.print(
        "===========[ ALL TESTS HAS BEEN DONE!!! ]==========", style="bold green"
    )


def test_python_language():
    console.print("===========[ TESTING PYTHON ]==========", style="bold blue")

    # Python does not need any installation, just run the hello.any file
    console.log("Running hello.any file...")
    os.system("python hello.any > ./test-cache/python_output.txt")

    console.log("Checking the output...")
    # Check if the output is correct
    with open("./test-cache/python_output.txt", "r") as f:
        output = f.read()
        if "Hello world!\n" == output:
            console.print(
                "==========[ PYTHON TEST PASSED ]==========", style="bold green"
            )
        else:
            console.print(
                "==========[ PYTHON TEST FAILED ]==========", style="bold red"
            )


def test_brainfuck_language():
    console.print("===========[ TESTING BRAINF**K ]==========", style="bold blue")

    console.log("Installing brainf**k language...")
    # Install brainf**k language

    try:
        os.system(f"git clone {BF_GEI_MIRROR} Python-Brainfuck ")
    except OSError as e:
        console.print(
            "Cannot clone from github.com. Please check your internet connection or mirrors.",
            style="bold red",
        )
        return

    # os.chdir("./Python-Brainfuck")

    # 如果是linux使用mv,如果是windows使用move
    shutil.copyfile("./hello.any", "./Python-Brainfuck/hello.bf")
    # os.system(
    #     "powershell.exe -Command copy ../hello.any ./hello.bf "
    #     if os.name == "nt"
    #     else "cp ../hello.any ./hello.bf"
    # )

    os.system(
        f"python ./Python-Brainfuck/{BF_MAIN_FILE} ./Python-Brainfuck/hello.bf > ./Python-Brainfuck/output.txt"
    )
    console.log(
        "Output of the program is in ./Python-Brainfuck/output.txt file, but we will delete it after we checked the output."
    )

    # Check if the output is correct
    with open("./Python-Brainfuck/output.txt", "r") as f:
        output = f.read()
        # console.print('Hello world!\n')
        # console.print(repr(output))

        if "Hello world!\n" == output:
            console.print("Test passed")
        else:
            console.print("Test failed, maybe your mirror cannot use")
            console.print(
                "===========[ BRAINF**K TEST FAILED ]==========X", style="bold red"
            )
            return

    console.print("Cleaning up...")
    # os.chdir("..")
    # os.system("rmdir /s /q  Python-Brainfuck")

    try:
        shutil.rmtree("./Python-Brainfuck")
    except OSError as e:
        print(
            f"FUCKIT! Cannot deleted ./Python-Brainfuck directory by shutil.rmtree() method \n because [[ {e} ]].\n But don't be worried.\n =============[ Trying force delete... ]============",
        )
        force_remove_dir_contents("./Python-Brainfuck")
        console.print("Cleaned up!", style="bold green")

    console.print("Done!")
    console.print("===========[ BRAINF**K TEST PASSED]==========√", style="bold green")


def test_c_language():
    console.print("===========[ TESTING C ]==========", style="bold blue")

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
            console.print("===========[ C TEST PASSED ]==========", style="bold green")
        else:
            console.print("===========[ C TEST FAILED ]==========X", style="bold red")
            return


def test_cpp_language():
    console.print("===========[ TESTING C++ ]==========", style="bold blue")

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
            console.print(
                "===========[ C++ TEST PASSED ]==========", style="bold green"
            )
        else:
            console.print("===========[ C++ TEST FAILED ]==========X", style="bold red")
            return


def main():
    check_the_environment()
    test_python_language()
    test_c_language()
    test_cpp_language()
    test_brainfuck_language()
    delete_test_cache_directory()


if __name__ == "__main__":
    main()
