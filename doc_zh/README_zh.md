# HelloWorld

[English](../README.md) | 简体中文

一个使用许多语言编写而成的HelloWorld程序。

你可以直接编译/运行它，而无需对代码作任何更改。

## 这个项目支持什么语言？
参见 [语言列表](./LANGUAGES.md)。

## 如何编译/运行这个项目？
1. 首先，你通常需要更改"hello.any"的后缀名。

    虽然一部分编译/解释器 (例如CPython) 不要求你更改后缀名, 但其他大部分会要求提供正确的
    后缀名。(".any"后缀名的意思就是可以使用任何后缀名)

    你需要更改的后缀名视情况而定。

    例如，在Linux系统中，如果您想将其作为C语言源代码编译，你可以使用：
    ```
    mv hello.any hello.c
    ```
    你可以使用任何方式更改它。

2. 现在你可以编译/运行它了。
    一些示例：

    - Python: `python3 hello.py`
    - C: `gcc -o hello hello.c`
    - C++: `g++ -o hello hello.cpp`
    - Brainfuck: `brainfuck hello.bf`
    - B̶r̶a̶i̶n̶f̶u̶c̶k̶: `python3 -m __hello__ hello.any`
    - Hello, golf!: `python3 -m __hello__ hello.any`
    - 其他所有无语法Esolang（前提是他们输出HelloWorld）: `python3 -m __hello__ hello.any`

多简单，不是吗？

如果没有输出“Hello world!”，请提交一个BUG。谢谢！

## 许可
该程序采用WTFPL
（DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE，“你tm想做啥都行”开源许可）许可。

参见[许可](./LICENSE)。

## 其他
如果您有任何问题或建议，请随时通过我的电子邮件与我联系：bcbyte@foxmail.com。

祝您开心！
