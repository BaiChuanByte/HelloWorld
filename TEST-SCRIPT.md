# Test Script
[English](../TEST-SCRIPT.md) | Simplified Chinese
## Usage
If you haven't installed any interpreters or compilers for esolangs<br>
 but still want to run this project, don't worry.

You may have noticed that there is a `test-script.py` file in the root directory of this project.<br>
It can help you run **ALL** language we support.<br>

To run it, please follow these steps:
1. Clone this repository. `shell git clone (-b dev) https://github.com/BaiChuanByte/HelloWorld.git`
2. `cd` to the root directory of this project.
3. Install pip dependencies. `pip3 install -r requirements.txt` or `pip install -r requirements.txt`
4. Run the test script. `python test-script.py` or `python3 test-script.py`
### Note:
You need to install the required interpreters or compilers before running the test script:
- Python (python3, pip3)
- C (gcc)
- C++ (g++)
---
## Principle
The test script works as follows:
1. Check the running environment
    > Environmental requirements:
    > - Python 3 `for Python/Brainfuck`
    > - rich `for nice output`
    > - gcc/g++ `for C/C++/Begunge`
    > - git `for Esolangs`
    > Other requirements:
    > - In the root directory of the project
    > - Able to connect to github.com or gitee.com
2. Create a `test-caches` directory
3. Clone the repository from `github` or `gitee` into the `test-caches` directory
4. Test each one individually
    1. Copy the file to the language root directory `./test-caches/<language-name>/`
    2. Interpret/compile and run `hello.any` (the suffix will be changed automatically)
    3. Compare the program's output with the expected output and save it to `test-caches/<language-name>/output.txt`
        > Expected output:<br>
        > "Hello world!\n"<br>
        > For more details, see [CONTRIBUTING_zh.md](./CONTRIBUTING.md)
5. Print the test results
