# ⚡ Python-C 语法速查对照表

> **专为 C 语言背景学习者设计**

---

## 1. 基础语法

| 特性 | C 语言 | Python |
| :--- | :--- | :--- |
| **变量声明** | `int a = 10;` | `a = 10` (动态类型) |
| **常量** | `const int A = 10;` | 约定俗成全大写 `A = 10` |
| **代码块** | `{ ... }` | 缩进 (4个空格) |
| **行尾分号** | 必须 `;` | 不需要 |
| **注释** | `// ...` `/* ... */` | `# ...` `""" ... """` |
| **头文件/库** | `#include <stdio.h>` | `import math` |

---

## 2. 数据类型

| 类型 | C 语言 | Python | 示例 |
| :--- | :--- | :--- | :--- |
| **整数** | `int`, `long` | `int` (无限精度) | `x = 100` |
| **浮点数** | `float`, `double` | `float` | `y = 3.14` |
| **布尔值** | `int` (0/1) | `bool` | `is_true = True` |
| **字符** | `char c = 'a';` | 无 (单字符字符串) | `c = 'a'` |
| **字符串** | `char s[] = "abc";` | `str` (不可变) | `s = "abc"` |
| **空值** | `NULL` | `None` | `x = None` |

---

## 3. 运算符

| 运算符 | C 语言 | Python | 备注 |
| :--- | :--- | :--- | :--- |
| **算术** | `+ - * / %` | `+ - * / %` | |
| **整除** | `/` (对整数) | `//` | `7 // 3` 结果是 `2` |
| **幂** | `pow(2, 3)` | `**` | `2 ** 3` 结果是 `8` |
| **自增/减** | `i++`, `i--` | `i += 1`, `i -= 1` | Python 没有 `++` / `--` |
| **逻辑** | `&&` `||` `!` | `and` `or` `not` | 使用英文单词 |
| **比较** | `== != > < >= <=` | `== != > < >= <=` | 相同 |
| **三元** | `(x > y) ? x : y` | `x if x > y else y` | 语法顺序不同 |

---

## 4. 流程控制

| 控制流 | C 语言 | Python |
| :--- | :--- | :--- |
| **if-else** | `if (x > 0) { ... }` | `if x > 0:` |
| **else if** | `else if (x == 0) { ... }` | `elif x == 0:` |
| **switch** | `switch (c) { case 'a': ... }` | 无 (用 `if-elif-else` 或字典) |
| **while** | `while (i < 5) { ... }` | `while i < 5:` |
| **for** | `for (int i=0; i<5; i++) { ... }` | `for i in range(5):` |
| **for-each** | (需手动实现) | `for item in my_list:` |

---

## 5. 函数

| 特性 | C 语言 | Python |
| :--- | :--- | :--- |
| **定义** | `int add(int a, int b) { ... }` | `def add(a, b): ...` |
| **返回类型** | 必须声明 | 无需声明 |
| **参数类型** | 必须声明 | 无需声明 |
| **多返回值** | 指针或结构体 | `return a, b` (返回元组) |
| **默认参数** | 不支持 | `def func(a, b=10): ...` |

---

## 6. 核心数据结构

### 字符串 (`str`)

| 操作 | C 语言 (`<string.h>`) | Python |
| :--- | :--- | :--- |
| **长度** | `strlen(s)` | `len(s)` |
| **拼接** | `strcat(dest, src)` | `s1 + s2` |
| **比较** | `strcmp(s1, s2)` | `s1 == s2` |
| **查找** | `strstr(s, sub)` | `s.find(sub)` 或 `sub in s` |
| **切片** | (手动循环) | `s[start:stop:step]` |
| **分割** | `strtok(s, delim)` | `s.split(delim)` |
| **连接** | (手动循环) | `delim.join(list_of_strings)` |

### 列表 (`list`) vs 数组

| 特性 | C 数组 | Python 列表 |
| :--- | :--- | :--- |
| **定义** | `int arr[5];` | `my_list = []` |
| **长度** | 固定 | 动态 |
| **类型** | 单一 | 可混合 |
| **添加元素** | 不支持 | `my_list.append(item)` |
| **删除元素** | 不支持 | `my_list.remove(item)` `my_list.pop(index)` |
| **获取长度** | `sizeof(arr)/sizeof(arr[0])` | `len(my_list)` |

### 字典 (`dict`) vs 结构体 (`struct`)

| 特性 | C 结构体 | Python 字典 |
| :--- | :--- | :--- |
| **定义** | `struct S { int a; };` | `my_dict = {}` |
| **字段/键** | 固定 | 动态 |
| **访问** | `s.a` | `my_dict['a']` 或 `my_dict.get('a')` |
| **添加** | 不支持 | `my_dict['new_key'] = value` |
| **遍历** | 不支持 | `for key, value in my_dict.items():` |

---

## 7. 输入输出

| 操作 | C 语言 (`<stdio.h>`) | Python |
| :--- | :--- | :--- |
| **打印** | `printf("Val: %d\n", x);` | `print(f"Val: {x}")` (f-string) |
| **读输入** | `scanf("%d", &x);` | `x = int(input("Enter a number: "))` |
| **文件打开** | `FILE *f = fopen("f.txt", "r");` | `with open("f.txt", "r") as f:` |
| **文件关闭** | `fclose(f);` | 自动关闭 (使用 `with`) |
| **读一行** | `fgets(buf, size, f);` | `line = f.readline()` |
| **写文件** | `fprintf(f, "Hello");` | `f.write("Hello")` |

---

## 8. 常见模式转换

| 任务 | C 语言 | Python |
| :--- | :--- | :--- |
| **遍历0到N-1** | `for (int i=0; i<N; i++)` | `for i in range(N):` |
| **遍历数组/列表** | `for (int i=0; i<len; i++)` | `for item in my_list:` |
| **遍历并获取索引** | `for (int i=0; i<len; i++)` | `for i, item in enumerate(my_list):` |
| **交换变量** | `temp=a; a=b; b=temp;` | `a, b = b, a` |
| **字符串反转** | (手动循环) | `s[::-1]` |