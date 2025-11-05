# 📝 第四部分：文件操作与实战冲刺（60 分钟）

> **目标**：掌握考试必考的文件操作，并练习综合应用

---

## 📋 本部分学习目标

完成本部分后，你将能够：
- ✅ 使用 `with open()` 安全地读写文件
- ✅ 理解不同的文件打开模式（`r`, `w`, `a`）
- ✅ 掌握 `read()`, `readline()`, `readlines()`, `write()` 等文件操作方法
- ✅ 熟练使用列表推导式，编写更 Pythonic 的代码
- ✅ 独立完成综合性的模拟考试题

---

## ⏱️ 时间分配

| 内容 | 时间 | 状态 |
|------|------|------|
| 文件输入输出（File I/O） | 20 分钟 | ⬜ |
| 列表推导式 | 10 分钟 | ⬜ |
| 模拟考试题练习 | 30 分钟 | ⬜ |

---

## 1️⃣ 文件输入输出（File I/O）（20 分钟）⭐ **考试必考**

### 1.1 `with open()`：最安全的文件操作方式

#### 🔵 C 语言

```c
#include <stdio.h>

FILE *fp;
fp = fopen("filename.txt", "w"); // 打开文件
if (fp == NULL) {
    // 错误处理
}
fprintf(fp, "Hello, World!\n");
fclose(fp); // 必须手动关闭文件
```

#### 🐍 Python

```python
# Python：使用 with open()，无需手动关闭文件
with open("filename.txt", "w") as f:
    f.write("Hello, World!\n")
# with 代码块结束时，文件会自动关闭
```

**为什么 `with open()` 更安全？**
- 无论代码块中是否发生错误，`with` 语句都会确保文件被正确关闭。
- 避免了忘记 `fclose()` 导致的文件句柄泄漏问题。

---

### 1.2 文件打开模式

| 模式 | 描述 | 文件不存在 | 文件存在 |
|------|------|------------|----------|
| `r` | **读**（默认） | 报错 `FileNotFoundError` | 从头读取 |
| `w` | **写** | 创建新文件 | **覆盖**原有内容 |
| `a` | **追加** | 创建新文件 | 在末尾追加内容 |
| `r+` | 读写 | 报错 | 从头读写 |
| `w+` | 读写 | 创建 | **覆盖** |
| `a+` | 读写 | 创建 | 在末尾读写 |
| `b` | 二进制模式（如 `rb`, `wb`） | - | - |

**考试重点**：`r`, `w`, `a`

---

### 1.3 读取文件

假设我们有一个 `data.txt` 文件，内容如下：
```
Line 1
Line 2
Line 3
```

#### `read()`：读取整个文件内容

```python
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
# 输出:
# Line 1
# Line 2
# Line 3
```

#### `readline()`：读取一行

```python
with open("data.txt", "r") as f:
    line1 = f.readline()
    print(line1.strip())  # .strip() 去除末尾的换行符
    line2 = f.readline()
    print(line2.strip())
# 输出:
# Line 1
# Line 2
```

#### `readlines()`：读取所有行并返回一个列表

```python
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
# 输出: ['Line 1\n', 'Line 2\n', 'Line 3\n']

# 处理列表
for line in lines:
    print(line.strip())
```

#### 遍历文件对象（最推荐的逐行读取方式）

```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
# 输出:
# Line 1
# Line 2
# Line 3
```

---

### 1.4 写入文件

#### `write()`：写入字符串

```python
with open("output.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is a new line.\n")
```
**注意**：`write()` 不会自动添加换行符，需要手动添加 `\n`。

#### `writelines()`：写入一个字符串列表

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```
**注意**：`writelines()` 也不会自动添加换行符，列表中的字符串需要包含 `\n`。

#### 综合示例：读取、处理、写入

```python
# 任务：读取 data.txt，给每一行加上行号，并写入到 new_data.txt

with open("data.txt", "r") as f_in:
    with open("new_data.txt", "w") as f_out:
        for i, line in enumerate(f_in, start=1):
            f_out.write(f"{i}: {line}")
```

---

### 1.5 文件路径

- **相对路径**：`"data.txt"`, `"files/data.txt"`
- **绝对路径**：`"C:/Users/name/Documents/data.txt"` (Windows), `"/home/user/data.txt"` (Linux/Mac)

**处理路径的最佳实践**：使用 `os` 或 `pathlib` 模块。

```python
import os

# 路径拼接
dir_path = "my_files"
file_name = "data.txt"
full_path = os.path.join(dir_path, file_name)
print(full_path)  # my_files\data.txt (Windows) 或 my_files/data.txt (Linux)

# 检查文件是否存在
if os.path.exists(full_path):
    print("文件存在")
else:
    print("文件不存在")
```

---

## 1️⃣.6 正则表达式（Regular Expression）⭐ **第4章重点**

正则表达式是一种强大的文本模式匹配工具，用于验证、查找、替换和提取文本中的特定模式。

### 什么是正则表达式？

正则表达式（regex）能让你：
- **验证**：检查字符串是否符合特定格式（如邮箱、手机号）
- **查找**：在文本中找到所有符合模式的子串
- **替换**：找到并替换文本中的特定部分
- **提取**：从文本中精确提取需要的信息

### `re` 模块核心函数

```python
import re
```

| 函数 | 描述 | 返回值 |
|:---|:---|:---|
| `re.match(pattern, string)` | 从字符串**开头**匹配模式 | Match 对象或 `None` |
| `re.search(pattern, string)`| 扫描整个字符串，找到**第一个**匹配 | Match 对象或 `None` |
| `re.findall(pattern, string)`| 找到**所有**匹配 | 字符串列表 |
| `re.split(pattern, string)` | 按模式分割字符串 | 字符串列表 |
| `re.sub(pattern, repl, string)`| 替换匹配的子串 | 新字符串 |
| `re.compile(pattern)` | 编译模式为正则表达式对象 | Regex 对象 |

#### `match` vs `search` 的区别

```python
text = "hello world"

# match 只能从开头匹配
print(re.match("world", text))  # None

# search 可以在任意位置匹配
print(re.search("world", text)) # <re.Match object; span=(6, 11), match='world'>
```

### 正则表达式核心语法

#### 基本元字符

| 元字符 | 描述 | 示例 |
|:---|:---|:---|
| `.` | 匹配任意单个字符（除换行符） | `a.c` 匹配 `abc`, `axc` |
| `^` | 匹配字符串开头 | `^hello` |
| `$` | 匹配字符串结尾 | `world$` |
| `*` | 匹配前面元素 0 次或多次 | `ab*c` 匹配 `ac`, `abc`, `abbc` |
| `+` | 匹配前面元素 1 次或多次 | `ab+c` 匹配 `abc`, `abbc` |
| `?` | 匹配前面元素 0 次或 1 次 | `ab?c` 匹配 `ac`, `abc` |
| `{m}` | 匹配前面元素 m 次 | `a{3}` 匹配 `aaa` |
| `{m,n}`| 匹配前面元素 m 到 n 次 | `a{2,4}` 匹配 `aa`, `aaa`, `aaaa` |

#### 字符集 `[]`

| 表达式 | 描述 |
|:---|:---|
| `[abc]` | 匹配 `a` 或 `b` 或 `c` |
| `[a-z]` | 匹配任意小写字母 |
| `[A-Z]` | 匹配任意大写字母 |
| `[0-9]` | 匹配任意数字 |
| `[a-zA-Z0-9]` | 匹配任意字母或数字 |
| `[^abc]` | **排除**：匹配除了 `a`, `b`, `c` 之外的字符 |

#### 特殊字符序列

| 序列 | 描述 | 等价于 |
|:---|:---|:---|
| `\d` | 匹配任意数字 | `[0-9]` |
| `\D` | 匹配任意非数字 | `[^0-9]` |
| `\w` | 匹配字母、数字、下划线 | `[a-zA-Z0-9_]` |
| `\W` | 匹配非字母、数字、下划线 | `[^a-zA-Z0-9_]` |
| `\s` | 匹配任意空白字符 | `[ \t\n\r\f\v]` |
| `\S` | 匹配任意非空白字符 | `[^ \t\n\r\f\v]` |
| `\b` | 匹配单词边界 | |

#### 分组 `()` 与或 `|`

```python
# 分组示例
text = "ababab"
print(re.findall("(ab)+", text))  # ['ab']

# 或示例
text = "I love cats or dogs"
print(re.search("cat|dog", text))  # <re.Match object; match='cat'>
```

### Match 对象

当 `re.match()` 或 `re.search()` 成功匹配时，返回 Match 对象：

```python
text = "My phone number is 123-456-7890."
pattern = r"(\d{3})-(\d{3})-(\d{4})"
match = re.search(pattern, text)

if match:
    print(f"整个匹配: {match.group(0)}")   # 123-456-7890
    print(f"第一个分组: {match.group(1)}") # 123
    print(f"第二个分组: {match.group(2)}") # 456
    print(f"第三个分组: {match.group(3)}") # 7890
    print(f"所有分组: {match.groups()}")   # ('123', '456', '7890')
    print(f"起始位置: {match.start()}")   # 19
    print(f"结束位置: {match.end()}")     # 31
```

### 贪婪模式 vs 非贪婪模式

默认情况下，`*`, `+`, `?` 都是**贪婪的**，会尽可能多地匹配。加上 `?` 变为**非贪婪**。

```python
text = "<a>content1</a><a>content2</a>"

# 贪婪模式
greedy = r"<a>.*</a>"
print(re.search(greedy, text).group())  
# <a>content1</a><a>content2</a>

# 非贪婪模式
non_greedy = r"<a>.*?</a>"
print(re.search(non_greedy, text).group())  
# <a>content1</a>
```

### 实用案例

#### 案例 1：验证邮箱地址

```python
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))  # True
print(is_valid_email("test@example"))      # False
```

#### 案例 2：提取手机号

```python
text = "联系方式：13812345678 或 13987654321"
pattern = r"1[3-9]\d{9}"
phones = re.findall(pattern, text)
print(phones)  # ['13812345678', '13987654321']
```

#### 案例 3：隐藏手机号中间4位

```python
text = "我的手机号是 13812345678"
pattern = r"(\d{3})\d{4}(\d{4})"
hidden = re.sub(pattern, r"\1****\2", text)
print(hidden)  # 我的手机号是 138****5678
```

#### 案例 4：分割字符串

```python
text = "apple,banana;orange:grape"
# 按多种分隔符分割
parts = re.split(r'[,;:]', text)
print(parts)  # ['apple', 'banana', 'orange', 'grape']
```

### 编译正则表达式

如果一个正则表达式需要多次使用，先编译可以提高效率：

```python
# 编译模式
phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

# 多次使用
text1 = "Call me at 123-456-7890."
text2 = "My office number is 987-654-3210."

print(phone_pattern.search(text1))
print(phone_pattern.search(text2))
```

### 常用正则模式速查

| 用途 | 正则表达式 |
|:---|:---|
| 邮箱 | `r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'` |
| 手机号(中国) | `r'^1[3-9]\d{9}$'` |
| 身份证号 | `r'^\d{17}[\dXx]$'` |
| IP地址 | `r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'` |
| 日期(YYYY-MM-DD) | `r'^\d{4}-\d{2}-\d{2}$'` |
| URL | `r'^https?://[^\s]+$'` |

### 易错点提醒

1. **使用原始字符串**：`r"..."` 避免转义问题
2. **match vs search**：match 只从开头匹配
3. **findall 返回列表**：不是 Match 对象
4. **分组编号从 1 开始**：`group(0)` 是整个匹配
5. **贪婪匹配**：记得使用 `?` 变为非贪婪


---

## 2️⃣ 列表推导式（List Comprehension）（10 分钟）⭐ **Pythonic!**

列表推导式提供了一种简洁的方式来创建列表。

### 2.1 基本语法

`[expression for item in iterable]`

#### 示例 1：创建平方数列表

```python
# 传统 for 循环
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2.2 带条件的列表推导式

`[expression for item in iterable if condition]`

#### 示例 2：筛选偶数

```python
# 传统 for 循环
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)  # [0, 2, 4, 6, 8]

# 列表推导式
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

### 2.3 更多示例

```python
# 字符串列表转大写
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# 从文件中读取行并去除换行符
with open("data.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# 字典推导式
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 集合推导式
squares_set = {x**2 for x in range(5)}
print(squares_set)  # {0, 1, 4, 9, 16}
```

**为什么使用列表推导式？**
- **简洁**：代码更短，更易读。
- **高效**：通常比等效的 `for` 循环更快。
- **Pythonic**：是 Python 语言的标志性特性，能体现你的熟练度。

---

## 3️⃣ 模拟考试题练习（30 分钟）

### 题目 1：字符串处理 - 统计单词频率

**任务**：编写一个程序，读取一个文本文件，统计其中每个单词出现的次数，并按出现次数从高到低输出前 10 个单词。

**提示**：
1. 读取文件内容。
2. 将所有字母转为小写，并替换掉标点符号。
3. 使用 `split()` 将文本分割成单词列表。
4. 使用字典来存储每个单词的频率。
5. 使用 `sorted()` 函数对字典的 `items()` 进行排序。

<details>
<summary>点击查看参考代码</summary>

```python
import string

def word_count(filename):
    """统计文件中单词的频率"""
    word_freq = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            
            # 替换标点符号为空格
            for p in string.punctuation:
                text = text.replace(p, ' ')
            
            words = text.split()
            
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
                
        # 按频率排序
        sorted_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        
        # 输出前 10 个
        print(f"'{filename}' 中频率最高的 10 个单词:")
        for i, (word, freq) in enumerate(sorted_freq[:10], 1):
            print(f"{i}. '{word}': {freq} 次")
            
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到。")

# 创建一个测试文件
with open("sample.txt", "w") as f:
    f.write("Python is a great language. I love Python. Python is easy to learn.")

# 运行函数
word_count("sample.txt")
```
</details>

---

### 题目 2：文件操作 - 计算平均值

**任务**：一个文本文件 `numbers.txt` 中每行包含一个数字。编写一个程序，读取该文件，计算所有数字的总和与平均值，并将结果追加到文件末尾。

**提示**：
1. 使用 `with open()` 以 `r+` 模式打开文件。
2. 逐行读取，将每行字符串转换为浮点数。
3. 计算总和与平均值。
4. 使用 `f.write()` 将结果写入文件。

<details>
<summary>点击查看参考代码</summary>

```python
def calculate_average(filename):
    """计算文件中数字的总和与平均值"""
    numbers = []
    total = 0
    
    try:
        with open(filename, 'r+') as f:
            # 读取所有行
            lines = f.readlines()
            
            # 转换为数字
            for line in lines:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"警告: 无法转换行 '{line.strip()}' 为数字，已忽略。")
            
            if not numbers:
                print("文件中没有有效的数字。")
                return
                
            # 计算总和与平均值
            total = sum(numbers)
            average = total / len(numbers)
            
            # 将结果追加到文件末尾
            f.write("\n---\n")
            f.write(f"总和: {total:.2f}\n")
            f.write(f"平均值: {average:.2f}\n")
            
        print(f"计算完成，结果已写入 '{filename}'。")
        
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到。")

# 创建一个测试文件
with open("numbers.txt", "w") as f:
    f.write("10.5\n")
    f.write("20.0\n")
    f.write("15.5\n")
    f.write("30.0\n")

# 运行函数
calculate_average("numbers.txt")
```
</details>

---

### 题目 3：综合应用 - 筛选偶数

**任务**：编写一个函数 `filter_even_numbers(input_list)`，输入一个包含整数的列表，返回一个只包含其中偶数的新列表。请分别使用 `for` 循环和列表推导式两种方法实现。

**提示**：
- 使用 `%` 运算符判断奇偶。

<details>
<summary>点击查看参考代码</summary>

```python
def filter_even_numbers_loop(input_list):
    """使用 for 循环筛选偶数"""
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def filter_even_numbers_comprehension(input_list):
    """使用列表推导式筛选偶数"""
    return [num for num in input_list if num % 2 == 0]

# 测试
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("使用 for 循环:", filter_even_numbers_loop(numbers))
print("使用列表推导式:", filter_even_numbers_comprehension(numbers))
```
</details>

---

## 🎯 恭喜你！

你已经完成了 Python 速成计划的所有核心内容！

### ✅ 你现在应该能够

- 理解 Python 的基本语法和核心数据结构
- 编写包含条件、循环和函数的程序
- 进行文件读写操作
- 使用列表推导式等 Pythonic 特性
- 解决常见的编程问题

---

## 🚀 最后冲刺

- 📖 **复习**：快速浏览 [第一部分](part1_basics.md)、[第二部分](part2_data_structures.md)、[第三部分](part3_control_flow.md) 的小结。
- ⚡ **速查**：打开 [Python-C 语法速查对照表](quick_reference.md)，巩固记忆。
- ⚠️ **避坑**：阅读 [常见错误与陷阱](common_mistakes.md)，避免考试失误。
- 🎯 **速记**：考前 30 分钟，看一遍 [考前速记清单](exam_cheatsheet.md)。

**祝你考试顺利，取得好成绩！🎉**