# 📝 第三部分：流程控制与函数（60 分钟）

> **目标**：熟悉 Python 的逻辑控制和代码组织方式

---

## 📋 本部分学习目标

完成本部分后，你将能够：
- ✅ 使用 `if-elif-else` 进行条件判断
- ✅ 掌握 `while` 和 `for` 循环，特别是 Python 的 `for-each` 循环
- ✅ 使用 `range()` 函数进行数字序列循环
- ✅ 定义和调用 Python 函数，理解参数和返回值

---

## ⏱️ 时间分配

| 内容 | 时间 | 状态 |
|------|------|------|
| 条件与循环 | 20 分钟 | ⬜ |
| 函数（Function）详解 | 30 分钟 | ⬜ |
| 休息 | 10 分钟 | ⬜ |

---

## 1️⃣ 条件与循环（20 分钟）

### 1.1 条件语句：`if-elif-else`

#### 🔵 C 语言

```c
int score = 85;

if (score >= 90) {
    printf("A\n");
} else if (score >= 80) {
    printf("B\n");
} else if (score >= 70) {
    printf("C\n");
} else {
    printf("D\n");
}
```

#### 🐍 Python

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:  # 注意是 elif，不是 else if
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
```

#### 对比表格

| 特性 | C 语言 | Python |
|------|--------|--------|
| 关键字 | `if`, `else if`, `else` | `if`, `elif`, `else` |
| 括号 | 条件必须用 `()` 包围 | 条件不需要 `()` |
| 代码块 | 使用 `{}` | 使用缩进 |
| 真值判断 | `0` 为假，非 `0` 为真 | `False`, `0`, `""`, `[]`, `{}`, `()` 为假 |

#### Python 的真值判断

```python
# 以下值在 Python 中被认为是 False
if 0: print("0 is True")
if 0.0: print("0.0 is True")
if "": print("Empty string is True")
if []: print("Empty list is True")
if {}: print("Empty dict is True")
if (): print("Empty tuple is True")
if None: print("None is True")

# 其他所有值都为 True
if 1: print("1 is True")
if -1: print("-1 is True")
if "hello": print("'hello' is True")
if [1, 2]: print("[1, 2] is True")
```

---

### 1.2 `while` 循环

`while` 循环在 Python 和 C 中几乎一样。

#### 🔵 C 语言

```c
int i = 0;
while (i < 5) {
    printf("%d ", i);
    i++;
}
// 输出: 0 1 2 3 4
```

#### 🐍 Python

```python
i = 0
while i < 5:
    print(i, end=" ")
    i += 1  # Python 中没有 i++
# 输出: 0 1 2 3 4
```

#### `break` 和 `continue`

`break` 和 `continue` 的用法与 C 语言完全相同。

```python
# break: 终止循环
i = 0
while True:  # 无限循环
    if i >= 5:
        break
    print(i, end=" ")
    i += 1
# 输出: 0 1 2 3 4

# continue: 跳过本次循环
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
# 输出: 1 3 5
```

#### `while-else` 循环

Python 有一个独特的 `while-else` 结构：`else` 子句在循环正常结束时（即没有被 `break` 中断）执行。

```python
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("循环正常结束")

# 如果被 break 中断，else 不会执行
count = 0
while count < 3:
    if count == 1:
        break
    print(f"Count: {count}")
    count += 1
else:
    print("循环正常结束")
```

---

### 1.3 `for` 循环 ⭐ **巨大差异**

#### 🔵 C 语言的 `for` 循环

```c
// C 语言：基于计数器的循环
for (int i = 0; i < 5; i++) {
    printf("%d ", i);
}
// 输出: 0 1 2 3 4
```

#### 🐍 Python 的 `for` 循环

Python 的 `for` 循环是 **`for-each`** 循环，用于遍历任何**可迭代对象**（如列表、字符串、元组、字典、集合等）。

```python
# 遍历列表
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "hello":
    print(char)

# 遍历字典
student = {"name": "Alice", "age": 20}
for key, value in student.items():
    print(f"{key}: {value}")
```

#### 使用 `range()` 模拟 C 风格循环

要实现类似 C 语言的数字循环，需要使用 `range()` 函数。

```python
# range(stop)
for i in range(5):  # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

# range(start, stop)
for i in range(2, 5):  # 2, 3, 4
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i, end=" ")
print()

# 倒序循环
for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(i, end=" ")
print()
```

#### `for-else` 循环

与 `while-else` 类似，`for` 循环也有 `else` 子句，在循环正常结束时执行。

```python
for i in range(3):
    print(i)
else:
    print("循环正常结束")

# 如果被 break 中断，else 不会执行
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("循环正常结束")
```

---

## 2️⃣ 函数（Function）详解（30 分钟）

### 2.1 函数定义与调用

#### 🔵 C 语言

```c
// C 语言：需要声明参数类型和返回类型
int add(int a, int b) {
    return a + b;
}

int result = add(3, 5); // 8
```

#### 🐍 Python

```python
# Python：使用 def 定义，无需声明类型
def add(a, b):
    return a + b

result = add(3, 5)  # 8
result_str = add("hello", " world")  # "hello world"
```

#### 对比表格

| 特性 | C 语言 | Python |
|------|--------|--------|
| 定义关键字 | 无 | `def` |
| 参数类型 | 必须声明 | 无需声明 |
| 返回类型 | 必须声明 | 无需声明 |
| 多态性 | 不支持 | 天然支持（鸭子类型） |

---

### 2.2 函数返回值

Python 函数可以返回多个值，实际上是返回一个**元组**。

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

# 返回的是一个元组
result = get_min_max([1, 5, 2, 8, 3])
print(result)  # (1, 8)
print(type(result))  # <class 'tuple'>

# 可以使用元组解包接收
min_val, max_val = get_min_max([1, 5, 2, 8, 3])
print(f"Min: {min_val}, Max: {max_val}")
```

#### 🔵 C 语言对比

```c
// C 语言：只能返回一个值
// 要返回多个值，需要使用指针或结构体
void get_min_max(int arr[], int len, int *min_val, int *max_val) {
    // ...
}
```

---

### 2.3 函数参数

#### 位置参数

```python
def greet(name, message):
    print(f"{message}, {name}!")

greet("Alice", "Hello")  # Hello, Alice!
```

#### 关键字参数

可以指定参数名来传递参数，无需按顺序。

```python
greet(message="Hi", name="Bob")  # Hi, Bob!
```

#### 默认参数值

可以为参数提供默认值。

```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob", "Hi")  # Hi, Bob!
```

**重要规则**：默认参数必须放在非默认参数之后。

```python
# ❌ 错误
# def greet(message="Hello", name):
#     ...

# ✅ 正确
def greet(name, message="Hello"):
    ...
```

#### 可变数量的参数

- `*args`：接收任意数量的位置参数，打包成一个**元组**。
- `**kwargs`：接收任意数量的关键字参数，打包成一个**字典**。

```python
def flexible_function(*args, **kwargs):
    print("位置参数 (args):", args)
    print("关键字参数 (kwargs):", kwargs)

flexible_function(1, 2, 3, name="Alice", age=20)
# 位置参数 (args): (1, 2, 3)
# 关键字参数 (kwargs): {'name': 'Alice', 'age': 20}
```

---

### 2.4 变量作用域

#### 局部变量

在函数内部定义的变量是局部变量，只在函数内部有效。

```python
def my_func():
    x = 10  # 局部变量
    print(x)

my_func()  # 10
# print(x)  # NameError: name 'x' is not defined
```

#### 全局变量

在函数外部定义的变量是全局变量，可以在任何地方访问。

```python
x = 10  # 全局变量

def my_func():
    print(x)  # 可以访问全局变量

my_func()  # 10
```

#### 修改全局变量：`global` 关键字

如果要在函数内部修改全局变量，必须使用 `global` 关键字。

```python
x = 10

def modify_global():
    global x  # 声明要修改的是全局变量 x
    x = 20

modify_global()
print(x)  # 20
```

**最佳实践**：尽量避免在函数中修改全局变量，这会使代码难以理解和维护。推荐通过参数和返回值来传递数据。

---

### 2.5 文档字符串（Docstring）

在函数定义的第一行使用三引号字符串，可以为函数添加文档。

```python
def add(a, b):
    """
    计算两个数的和。

    参数:
    a (int or float): 第一个数。
    b (int or float): 第二个数。

    返回:
    int or float: 两个数的和。
    """
    return a + b

# 查看文档
help(add)
print(add.__doc__)
```

---

## 🎯 本部分小结

### ✅ 你已经掌握了

1. **条件语句**
   - `if-elif-else` 结构
   - Python 的真值判断规则

2. **循环**
   - `while` 循环与 C 类似
   - `for` 循环是 `for-each` 循环，用于遍历可迭代对象
   - `range()` 函数用于数字序列循环
   - `break`, `continue` 和 `else` 子句

3. **函数**
   - 使用 `def` 定义函数
   - 无需声明参数和返回类型
   - 可以返回多个值（元组）
   - 参数类型：位置参数、关键字参数、默认参数、`*args`, `**kwargs`
   - 变量作用域：局部变量、全局变量、`global` 关键字
   - 使用文档字符串（Docstring）

---

## 📝 快速练习

### 练习 1：判断奇偶数

```python
# 任务：编写一个函数 is_even(number)，判断一个数是否为偶数
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
def is_even(number):
    """判断一个数是否为偶数"""
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False
```
</details>

### 练习 2：计算阶乘

```python
# 任务：编写一个函数 factorial(n)，计算 n 的阶乘
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
def factorial(n):
    """计算 n 的阶乘"""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # 120
```
</details>

### 练习 3：查找列表中的最大值和最小值

```python
# 任务：编写一个函数 find_min_max(numbers)，返回列表中的最大值和最小值
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
def find_min_max(numbers):
    """返回列表中的最大值和最小值"""
    if not numbers:  # 处理空列表
        return None, None
    return min(numbers), max(numbers)

min_val, max_val = find_min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {min_val}, Max: {max_val}")
```
</details>

---

## ⏭️ 下一步

恭喜你完成第三部分！休息 10 分钟后，进入最后冲刺：

👉 **[第四部分：文件操作与实战冲刺（60 分钟）](part4_files_practice.md)**

---

## 📚 相关资源

- 📖 [Python-C 语法速查对照表](quick_reference.md)
- ⚠️ [常见错误与陷阱](common_mistakes.md)
- 💻 [第三部分代码示例](examples/part3_examples.py)