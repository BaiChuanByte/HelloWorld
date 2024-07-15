# HelloWorld

English | [简体中文](./README_zh.md)

A Hello World program written in many programming languages.

You can compile/run directly WITHOUT changing the source code.

## What languages does it support?
See the [languages list](./LANGUAGES.md).

## How to compile/run it?
1. Firstly, you usually need to change the extension of "hello.any".

    Although some compilers/interpreters (such as CPython) do not require changing the file extension, most still require the file to
    have the correct extension.(The extension ".any" means that any extension can be used)

    The file extension you should change depends on the situation.

    For example, in Linux, if you want to compile it as a C language source code file, you can use:
    ```
    mv hello.any hello.c
    ```
    You can change it in any way you want.

3. Now you can compile/run it.
    Here are some examples:

    - Python: `python3 hello.py`
    - C: `gcc -o hello hello.c`
    - C++: `g++ -o hello hello.cpp`
    - Brainfuck: `brainfuck hello.bf`
    - b̶r̶a̶i̶n̶f̶u̶c̶k̶: `python3 -m __hello__ hello.any`
    - Hello, golf!: `python3 -m __hello__ hello.any`
    - All other No-code esolang (provided they output Hello World): `python3 -m __hello__ hello.any`

So easy, isn't it?

If the output is not "Hello, world!", please report a bug. Thanks!

## License
This programm is licensed under the terms of the WTFPL
(DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE).

See [license](./LICENSE).

## Other
If you have any questions or suggestions, feel free to contact me at my email: bcbyte@foxmail.com.

Have fun!
