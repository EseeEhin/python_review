# 📝 第一部分：思维转换与基础语法（60 分钟）

> **目标**：从 C 的思维模式切换到 Python，掌握最基本的语法差异

---

## 📋 本部分学习目标

完成本部分后，你将能够：
- ✅ 理解 Python 动态类型与 C 静态类型的区别
- ✅ 掌握 Python 的缩进规则（替代 C 的花括号）
- ✅ 熟练使用 Python 的字符串操作
- ✅ 使用 `print()` 和 `input()` 进行输入输出

---

## ⏱️ 时间分配

| 内容 | 时间 | 状态 |
|------|------|------|
| 核心差异讲解 | 15 分钟 | ⬜ |
| 字符串操作详解 | 20 分钟 | ⬜ |
| 输入输出实践 | 15 分钟 | ⬜ |
| 休息与回顾 | 10 分钟 | ⬜ |

---

## 1️⃣ 核心差异（15 分钟）

### 1.1 动态类型 vs 静态类型

#### 🔵 C 语言（静态类型）

```c
// C 语言：必须声明变量类型，类型不可改变
int age = 25;           // 整数类型
float price = 19.99;    // 浮点类型
char name[] = "Alice";  // 字符数组

age = "Bob";  // ❌ 错误！类型不匹配
```

#### 🐍 Python（动态类型）

```python
# Python：无需声明类型，变量可以随时改变类型
age = 25              # 整数
age = "Bob"           # ✅ 可以！现在是字符串
age = 19.99           # ✅ 可以！现在是浮点数
age = [1, 2, 3]       # ✅ 可以！现在是列表
```

#### 💡 关键理解

| 特性 | C 语言 | Python |
|------|--------|--------|
| 类型声明 | 必须显式声明 | 自动推断 |
| 类型检查 | 编译时检查 | 运行时检查 |
| 类型改变 | 不允许 | 允许 |
| 变量本质 | 内存地址 + 类型 | 对象的引用 |

**重要提示**：Python 中的变量是"标签"，不是"盒子"。它们只是指向对象的引用。

---

### 1.1.1 Python 对象模型深入理解 ⭐ **第1章重点**

#### Python 中的"一切皆对象"

在 Python 中，所有的数据都是作为**对象**来处理的。每个对象都有三个核心属性：

1. **ID (`id`)**: 对象在内存中的唯一标识（可以看作内存地址）
2. **类型 (`type`)**: 对象的类型，决定了对象能进行哪些操作
3. **值 (`value`)**: 对象存储的具体数据

```python
x = 10
print(f"ID: {id(x)}")      # 对象的内存地址
print(f"Type: {type(x)}")  # <class 'int'>
print(f"Value: {x}")       # 10
```

#### 变量是"标签"，不是"盒子"

这是理解 Python 的关键！

```python
# 1. 创建对象 10，并贴上标签 a
a = 10

# 2. 将标签 b 也贴在对象 10 上
b = a

# 3. 创建新对象 20，并将标签 b 移过去
b = 20

print(f"a = {a}")  # a 仍然是 10
print(f"b = {b}")  # b 变成了 20

# 验证：a 和 10 是同一个对象
print(f"id(a) == id(10): {id(a) == id(10)}")  # True
```

#### `is` vs `==` 的区别

- `==`: 比较两个对象的**值**是否相等
- `is`: 比较两个变量是否引用**同一个对象**（即 `id` 是否相同）

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True (值相同)
print(f"a is b: {a is b}")  # False (是两个不同的列表对象)

print(f"a == c: {a == c}")  # True (值相同)
print(f"a is c: {a is c}")  # True (引用同一个对象)
```

#### 可变对象 vs 不可变对象

这个概念与内存管理密切相关。

**不可变对象 (Immutable)**：
- 类型: `int`, `float`, `bool`, `str`, `tuple`
- 特点: 对象的值一旦创建就不能被修改，任何修改操作都会创建新对象

```python
x = 10
print(f"id(x) before: {id(x)}")
x = x + 1  # 创建了一个新对象 11
print(f"id(x) after: {id(x)}")  # ID 改变了
```

**可变对象 (Mutable)**：
- 类型: `list`, `dict`, `set`
- 特点: 对象的值可以在原地被修改，不会创建新对象

```python
my_list = [1, 2, 3]
print(f"id before: {id(my_list)}")
my_list.append(4)  # 在原对象上修改
print(f"id after: {id(my_list)}")  # ID 不变
```

#### 函数参数传递的本质

Python 的参数传递是**"传对象引用"** (pass-by-object-reference)。

```python
# 不可变对象：函数内部无法修改原始对象
def modify_string(s):
    s = "world"  # 创建新对象，不影响外部

my_str = "hello"
modify_string(my_str)
print(my_str)  # "hello" (未改变)

# 可变对象：函数内部可以修改原始对象
def modify_list(lst):
    lst.append(4)  # 在原对象上修改

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] (已改变)
```

#### 内存管理机制

**1. 引用计数 (Reference Counting)**

Python 会跟踪每个对象的引用数量：
- 当一个对象被新变量引用时，引用计数 `+1`
- 当引用被销毁时，引用计数 `-1`
- 当引用计数变为 `0` 时，对象被立即回收

```python
import sys

a = []  # 引用计数为 1
print(f"引用计数: {sys.getrefcount(a) - 1}")  # getrefcount 本身会+1

b = a   # 引用计数变为 2
print(f"引用计数: {sys.getrefcount(a) - 1}")

del b   # 引用计数变回 1
print(f"引用计数: {sys.getrefcount(a) - 1}")
```

**2. 循环引用问题**

当两个对象互相引用时，它们的引用计数永远不会变为 0：

```python
a = []
b = []
a.append(b)  # a 引用 b
b.append(a)  # b 引用 a

# 即使删除 a 和 b 的原始引用
del a
del b
# 这两个列表对象仍然在内存中互相引用
```

**3. 分代回收 (Generational Garbage Collection)**

为了解决循环引用，Python 使用分代回收：
- 对象分为三代：0代（新对象）、1代、2代
- 0代回收频率最高，2代最低
- 存活时间越长的对象，越不可能是垃圾

**4. 小对象池 (Integer Caching)**

为了提高效率，Python 会预先创建并缓存一些常用的小对象：

```python
# 小整数池：-5 到 256 之间的整数是全局共享的
a = 256
b = 256
print(f"256 is 256: {a is b}")  # True

c = 257
d = 257
print(f"257 is 257: {c is d}")  # False (在某些环境下可能为 True)
```

**重要提示**：
- 使用 `==` 比较值，使用 `is` 比较身份
- 理解可变与不可变对象的区别
- 注意函数参数传递的行为


---

### 1.2 代码块与缩进规则 ⭐ **最容易出错**

#### 🔵 C 语言（使用花括号 `{}`）

```c
// C 语言：使用花括号定义代码块，缩进只是为了美观
if (x > 0) {
    printf("Positive\n");
    printf("Greater than zero\n");
}

// 即使不缩进，代码也能运行（但不推荐）
if (x > 0) {
printf("Positive\n");
printf("Greater than zero\n");
}
```

#### 🐍 Python（使用缩进）

```python
# Python：使用缩进定义代码块，缩进是语法的一部分！
if x > 0:
    print("Positive")
    print("Greater than zero")

# ❌ 错误！缩进不一致会导致语法错误
if x > 0:
    print("Positive")
  print("Greater than zero")  # IndentationError
```

#### 📏 缩进规则详解

| 规则 | 说明 | 示例 |
|------|------|------|
| **标准缩进** | 使用 4 个空格（推荐） | `    print("Hello")` |
| **一致性** | 同一代码块必须使用相同缩进 | ✅ 全部 4 空格 或 全部 1 Tab |
| **混用禁止** | 不要混用空格和 Tab | ❌ 有的用空格，有的用 Tab |
| **冒号标记** | 代码块开始前必须有冒号 `:` | `if x > 0:` |

**实战技巧**：
- 在 VSCode 中，按 `Tab` 键会自动转换为 4 个空格
- 使用 `Shift + Tab` 可以减少缩进

---

### 1.3 注释

#### 🔵 C 语言

```c
// 单行注释

/*
 * 多行注释
 * 可以跨越多行
 */
```

#### 🐍 Python

```python
# 单行注释

"""
多行注释（实际上是多行字符串）
可以跨越多行
常用于函数文档字符串（docstring）
"""

'''
也可以使用单引号
效果相同
'''
```

---

## 2️⃣ 基本数据类型与字符串（20 分钟）

### 2.1 基本数据类型

#### 对比表格

| 类型 | C 语言 | Python | 说明 |
|------|--------|--------|------|
| 整数 | `int`, `long` | `int` | Python 的 `int` 无溢出限制！ |
| 浮点数 | `float`, `double` | `float` | Python 只有一种浮点类型 |
| 布尔值 | `int` (0/1) | `bool` | `True` / `False`（首字母大写） |
| 字符 | `char` | `str` | Python 没有单独的字符类型 |

#### 🐍 Python 示例

```python
# 整数（无溢出限制）
x = 10
y = 999999999999999999999999999999  # ✅ 可以！Python 自动处理大整数

# 浮点数
price = 19.99
pi = 3.14159

# 布尔值（注意首字母大写）
is_student = True
is_adult = False

# 类型查询
print(type(x))        # <class 'int'>
print(type(price))    # <class 'float'>
print(type(is_student))  # <class 'bool'>
```

---

### 2.2 字符串（String）⭐ **重点内容**

#### 🔵 C 语言的字符串

```c
// C 语言：字符串是字符数组，以 '\0' 结尾
char name[10] = "Alice";
name[0] = 'B';  // ✅ 可以修改
printf("%s\n", name);  // 输出：Blice
```

#### 🐍 Python 的字符串

```python
# Python：字符串是不可变对象
name = "Alice"
name[0] = 'B'  # ❌ 错误！TypeError: 'str' object does not support item assignment

# 必须创建新字符串
name = "B" + name[1:]  # ✅ 正确：创建新字符串 "Blice"
```

#### 📌 字符串的不可变性（Immutability）

| 特性 | C 语言 | Python |
|------|--------|--------|
| 可修改性 | 可修改字符数组 | 不可变（Immutable） |
| 修改方式 | 直接修改 `str[i] = 'x'` | 创建新字符串 |
| 内存效率 | 可能更高 | 字符串共享，节省内存 |

---

### 2.3 字符串的创建

```python
# 单引号
s1 = 'Hello'

# 双引号（推荐，与 C 语言习惯一致）
s2 = "World"

# 三引号（多行字符串）
s3 = """这是一个
多行字符串
可以跨越多行"""

# 原始字符串（忽略转义字符）
path = r"C:\Users\name\file.txt"  # 不会把 \n 解释为换行符
```

---

### 2.4 字符串切片（Slicing）⭐ **Python 的杀手级特性**

#### 语法：`s[start:stop:step]`

```python
s = "Hello, World!"

# 基本切片
print(s[0:5])      # "Hello"  - 从索引 0 到 4（不包括 5）
print(s[7:12])     # "World"  - 从索引 7 到 11

# 省略参数
print(s[:5])       # "Hello"  - 从开头到索引 4
print(s[7:])       # "World!" - 从索引 7 到结尾
print(s[:])        # "Hello, World!" - 完整字符串（复制）

# 负数索引（从右往左）
print(s[-1])       # "!"      - 最后一个字符
print(s[-6:])      # "World!" - 最后 6 个字符
print(s[:-1])      # "Hello, World" - 除了最后一个字符

# 步长（step）
print(s[::2])      # "Hlo ol!" - 每隔一个字符取一个
print(s[::-1])     # "!dlroW ,olleH" - 反转字符串！
```

#### 🔵 C 语言对比

```c
// C 语言：需要手动循环实现切片
char s[] = "Hello, World!";
char sub[6];
int i;
for (i = 0; i < 5; i++) {
    sub[i] = s[i];
}
sub[5] = '\0';
printf("%s\n", sub);  // "Hello"
```

**Python 的优势**：一行代码搞定！

---

### 2.5 字符串常用方法 ⭐ **考试必考**

```python
s = "  Hello, World!  "

# 1. 大小写转换
print(s.upper())       # "  HELLO, WORLD!  "
print(s.lower())       # "  hello, world!  "
print(s.capitalize())  # "  hello, world!  "
print(s.title())       # "  Hello, World!  "

# 2. 去除空白字符
print(s.strip())       # "Hello, World!" - 去除两端空白
print(s.lstrip())      # "Hello, World!  " - 去除左侧空白
print(s.rstrip())      # "  Hello, World!" - 去除右侧空白

# 3. 查找与替换
print(s.find("World"))    # 9 - 返回子串的起始索引
print(s.find("Python"))   # -1 - 未找到返回 -1
print(s.replace("World", "Python"))  # "  Hello, Python!  "

# 4. 分割与连接
words = "apple,banana,orange".split(",")  # ['apple', 'banana', 'orange']
print(words)

joined = "-".join(words)  # "apple-banana-orange"
print(joined)

# 5. 判断方法
print("123".isdigit())     # True - 是否全是数字
print("abc".isalpha())     # True - 是否全是字母
print("abc123".isalnum())  # True - 是否全是字母或数字
print("  ".isspace())      # True - 是否全是空白字符
```

#### 🔵 C 语言对比

```c
// C 语言：需要使用 <string.h> 库函数
#include <string.h>
#include <ctype.h>

char s[] = "Hello";

// 转大写（需要循环）
for (int i = 0; s[i]; i++) {
    s[i] = toupper(s[i]);
}

// 查找子串
char *pos = strstr(s, "World");

// 分割字符串
char *token = strtok(s, ",");
```

**Python 的优势**：内置方法丰富，无需额外库！

---

## 3️⃣ 基本输入输出（15 分钟）

### 3.1 输出：`print()` 函数

#### 🔵 C 语言

```c
int age = 25;
float price = 19.99;
printf("Age: %d, Price: %.2f\n", age, price);
```

#### 🐍 Python

```python
age = 25
price = 19.99

# 方法 1：逗号分隔（自动添加空格）
print("Age:", age, "Price:", price)  # Age: 25 Price: 19.99

# 方法 2：字符串拼接
print("Age: " + str(age) + ", Price: " + str(price))

# 方法 3：format() 方法
print("Age: {}, Price: {}".format(age, price))

# 方法 4：f-string（推荐！Python 3.6+）
print(f"Age: {age}, Price: {price}")
print(f"Age: {age}, Price: {price:.2f}")  # 保留 2 位小数
```

#### 📌 f-string 详解 ⭐ **最推荐的方式**

```python
name = "Alice"
age = 25
score = 95.678

# 基本用法
print(f"Name: {name}, Age: {age}")

# 表达式计算
print(f"Next year: {age + 1}")

# 格式化
print(f"Score: {score:.2f}")      # 95.68 - 保留 2 位小数
print(f"Score: {score:>10.2f}")   # "     95.68" - 右对齐，宽度 10
print(f"Name: {name:<10}")        # "Alice     " - 左对齐，宽度 10

# 多行 f-string
message = f"""
Name: {name}
Age: {age}
Score: {score:.2f}
"""
print(message)
```

#### `print()` 的常用参数

```python
# sep：分隔符（默认是空格）
print("apple", "banana", "orange", sep=", ")  # apple, banana, orange

# end：结尾字符（默认是换行符 \n）
print("Hello", end=" ")
print("World")  # Hello World（在同一行）

# 不换行输出（常用于进度条）
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
```

---

### 3.2 输入：`input()` 函数

#### 🔵 C 语言

```c
int age;
char name[50];

printf("Enter your name: ");
scanf("%s", name);

printf("Enter your age: ");
scanf("%d", &age);
```

#### 🐍 Python

```python
# input() 总是返回字符串！
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# 需要手动类型转换
age = int(age_str)  # 字符串 → 整数
```

#### ⚠️ 重要提示：`input()` 返回的永远是字符串

```python
# ❌ 错误示例
age = input("Enter your age: ")  # 用户输入 "25"
next_year = age + 1  # TypeError: can only concatenate str (not "int") to str

# ✅ 正确示例
age = int(input("Enter your age: "))  # 转换为整数
next_year = age + 1  # 26
```

#### 类型转换函数

```python
# 字符串 → 整数
age = int("25")        # 25
age = int("25.5")      # ❌ ValueError（不能直接转换浮点数字符串）

# 字符串 → 浮点数
price = float("19.99")  # 19.99
price = float("20")     # 20.0

# 字符串 → 布尔值
flag = bool("True")     # True（任何非空字符串都是 True）
flag = bool("")         # False（空字符串是 False）

# 其他类型 → 字符串
s = str(25)            # "25"
s = str(19.99)         # "19.99"
s = str(True)          # "True"
```

---

### 3.3 综合示例：简单的用户交互程序

```python
# 程序：计算矩形面积
print("=== 矩形面积计算器 ===")

# 获取用户输入
length = float(input("请输入长度: "))
width = float(input("请输入宽度: "))

# 计算面积
area = length * width

# 输出结果（使用 f-string）
print(f"\n矩形的面积是: {area:.2f} 平方单位")
print(f"周长是: {2 * (length + width):.2f} 单位")
```

---

## 🎯 本部分小结

### ✅ 你已经掌握了

1. **核心差异**
   - Python 是动态类型语言
   - 使用缩进（4 个空格）定义代码块
   - 使用 `#` 和 `"""..."""` 注释

2. **基本数据类型**
   - `int`（无溢出限制）、`float`、`bool`、`str`

3. **字符串操作**
   - 字符串是不可变的
   - 切片语法：`s[start:stop:step]`
   - 常用方法：`split()`, `join()`, `strip()`, `find()`, `replace()`

4. **输入输出**
   - `print()` 函数和 f-string 格式化
   - `input()` 函数（返回字符串）
   - 类型转换：`int()`, `float()`, `str()`

---

## 📝 快速练习

### 练习 1：字符串反转

```python
# 任务：输入一个字符串，输出其反转
s = input("请输入一个字符串: ")
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
s = input("请输入一个字符串: ")
print(f"反转后: {s[::-1]}")
```
</details>

### 练习 2：温度转换

```python
# 任务：输入摄氏温度，转换为华氏温度
# 公式：F = C * 9/5 + 32
celsius = float(input("请输入摄氏温度: "))
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
celsius = float(input("请输入摄氏温度: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")
```
</details>

### 练习 3：字符串处理

```python
# 任务：输入一个句子，统计单词数量
sentence = input("请输入一个句子: ")
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
sentence = input("请输入一个句子: ")
words = sentence.split()
print(f"单词数量: {len(words)}")
```
</details>

---

## ⏭️ 下一步

恭喜你完成第一部分！休息 10 分钟后，继续学习：

👉 **[第二部分：核心数据结构（90 分钟）](part2_data_structures.md)**

---

## 📚 相关资源

- 📖 [Python-C 语法速查对照表](quick_reference.md)
- ⚠️ [常见错误与陷阱](common_mistakes.md)
- 💻 [第一部分代码示例](examples/part1_examples.py)