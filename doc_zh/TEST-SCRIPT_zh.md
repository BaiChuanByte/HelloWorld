# 测试脚本
[English](../TEST-SCRIPT.md) | 简体中文


## 用法
如果您没有安装任何 esolang 的解释器或编译器，但仍然想运行这个项目，请不要担心。<br>
您可能注意到了，这个项目的根目录下有一个 `test-script.py` 文件。
TA可以帮助您运行**任何**我们支持的语言。<br>

要运行它，请按照以下步骤操作：
1. 克隆这个仓库。  `shell git clone (-b dev) https://github.com/BaiChuanByte/HelloWorld.git`
2. 进入这个项目的根目录。
3. 安装pip依赖包。   `pip3 install -r requirements.txt` 或 `pip install -r requirements.txt`
4. 运行测试脚本。    `python test-script.py` 或 `python3 test-script.py`


### 注意：
您需要在运行测试脚本之前安装所需的解释器或编译器：
- Python (python3, pip3)
- C (gcc)
- C++ (g++)

---
## 原理
测试脚本的工作原理是：
1. 检测运行环境
    > 环境要求:
    > - Python 3    `for Python/Brainfuck`
    > - rich       `for nice output`
    > - gcc/g++     `for C/C++/Begunge`
    > - git         `for Esolangs`
    > 其它要求:
    > - 在项目根目录
    > - 可以连接 github.com 或 gitee.com
2. 创建 `test-caches` 目录
3. 从 `github` 或 `gitee` 克隆仓库,到 `test-caches` 目录
4. 逐个测试
    1. 复制文件到语言根目录 `./test-caches/<语言名>/`
    2. 解释/编译 运行`hello.any` (后缀会自动更改)
    1. 把程序的输出和期望输出对比,保存到 `test-caches/<语言名>/output.txt`
        > 期望输出:<br>
        > "Hello world!\n"<br>
        > 详见 [CONTRIBUTING_zh.md](./CONTRIBUTING_zh.md)
5. 打印测试结果

