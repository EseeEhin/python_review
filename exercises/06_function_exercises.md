# 📝 06_函数练习

> **知识点**：函数定义、参数（位置、默认、可变）、返回值、作用域、lambda表达式

---

## 题目1：函数基本定义 ⭐

**题目**：定义一个函数，计算并返回两个数的和。

```python
# 任务：
# 1. 定义一个名为 `add` 的函数，接收两个参数 `a` 和 `b`
# 2. 函数内部计算 `a + b`
# 3. 返回计算结果
# 4. 调用函数并打印结果
```

<details>
<summary>✅ 答案</summary>

```python
def add(a, b):
    """计算并返回两个数的和"""
    return a + b

# 调用函数
result = add(5, 3)
print(f"5 + 3 = {result}")  # 5 + 3 = 8

result = add(-10, 2)
print(f"-10 + 2 = {result}") # -10 + 2 = -8
```

**知识点**：
- `def` 关键字定义函数
- 函数参数
- `return` 关键字返回值
- 文档字符串 `"""..."""`

</details>

---

## 题目2：默认参数 ⭐⭐

**题目**：定义一个函数，向用户打招呼，如果未提供姓名，则使用默认姓名。

```python
# 任务：
# 1. 定义一个名为 `greet` 的函数，接收一个参数 `name`
# 2. `name` 参数的默认值为 "游客"
# 3. 函数打印 "你好, [姓名]!"
# 4. 测试两种调用方式：提供姓名和不提供姓名
```

<details>
<summary>✅ 答案</summary>

```python
def greet(name="游客"):
    """向用户打招呼"""
    print(f"你好, {name}!")

# 提供姓名
greet("张三")  # 你好, 张三!

# 不提供姓名（使用默认值）
greet()      # 你好, 游客!
```

**知识点**：
- 默认参数 `param=value`
- 默认参数必须放在位置参数之后

**⚠️ 常见错误**：
```python
# 错误：默认参数必须在非默认参数之后
def func(a=10, b):  # SyntaxError: non-default argument follows default argument
    pass

# 正确
def func(b, a=10):
    pass
```
</details>

---

## 题目3：返回多个值 ⭐⭐

**题目**：定义一个函数，接收一个列表，返回列表中的最大值和最小值。

```python
# 任务：
# 1. 定义一个名为 `get_max_min` 的函数，接收一个列表 `numbers`
# 2. 函数内部找出最大值和最小值
# 3. 返回这两个值
# 4. 调用函数并解包返回值
```

<details>
<summary>✅ 答案</summary>

```python
def get_max_min(numbers):
    """返回列表中的最大值和最小值"""
    if not numbers:
        return None, None  # 处理空列表情况
    
    return max(numbers), min(numbers)

# 调用函数
nums = [3, 1, 4, 1, 5, 9, 2, 6]
max_val, min_val = get_max_min(nums)

print(f"列表: {nums}")
print(f"最大值: {max_val}")  # 最大值: 9
print(f"最小值: {min_val}")  # 最小值: 1

# 返回的实际上是一个元组
result_tuple = get_max_min(nums)
print(f"返回的元组: {result_tuple}") # 返回的元组: (9, 1)
```

**知识点**：
- 函数返回多个值（实际上是返回一个元组）
- 元组解包
- 内置函数 `max()` 和 `min()`

</details>

---

## 题目4：可变参数 `*args` ⭐⭐

**题目**：定义一个函数，计算任意多个数字的和。

```python
# 任务：
# 1. 定义一个名为 `calculate_sum` 的函数
# 2. 使用 `*args` 接收任意数量的位置参数
# 3. 函数内部计算所有参数的和并返回
# 4. 测试不同数量的参数
```

<details>
<summary>✅ 答案</summary>

```python
def calculate_sum(*args):
    """计算任意多个数字的和"""
    print(f"接收到的参数 (元组): {args}")
    total = 0
    for num in args:
        total += num
    return total

# 测试
print(f"总和: {calculate_sum(1, 2, 3)}")          # 总和: 6
print(f"总和: {calculate_sum(10, 20, 30, 40)}")   # 总和: 100
print(f"总和: {calculate_sum()}")                 # 总和: 0

# 也可以使用内置的 sum() 函数
def calculate_sum_simple(*args):
    return sum(args)

print(f"总和 (简化版): {calculate_sum_simple(1, 2, 3, 4, 5)}") # 总和 (简化版): 15
```

**知识点**：
- `*args` 接收任意数量的位置参数
- `args` 是一个元组（tuple）

</details>

---

## 题目5：可变关键字参数 `**kwargs` ⭐⭐⭐

**题目**：定义一个函数，打印用户的个人信息。

```python
# 任务：
# 1. 定义一个名为 `print_profile` 的函数
# 2. 使用 `**kwargs` 接收任意数量的关键字参数
# 3. 函数内部遍历并打印所有信息
# 4. 测试不同的个人信息
```

<details>
<summary>✅ 答案</summary>

```python
def print_profile(**kwargs):
    """打印用户的个人信息"""
    print(f"接收到的参数 (字典): {kwargs}")
    if not kwargs:
        print("未提供任何信息")
        return
        
    print("\n--- 用户信息 ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("----------------")

# 测试
print_profile(name="张三", age=20, city="北京")
# --- 用户信息 ---
# name: 张三
# age: 20
# city: 北京
# ----------------

print_profile(name="李四", job="工程师", hobby=["编程", "阅读"])
# --- 用户信息 ---
# name: 李四
# job: 工程师
# hobby: ['编程', '阅读']
# ----------------
```

**知识点**：
- `**kwargs` 接收任意数量的关键字参数
- `kwargs` 是一个字典（dict）

</details>

---

## 题目6：参数组合 ⭐⭐⭐

**题目**：定义一个复杂的函数，演示所有参数类型的组合。

```python
# 任务：
# 1. 定义一个名为 `complex_func` 的函数
# 2. 参数顺序为：位置参数, 默认参数, *args, **kwargs
# 3. 在函数内部打印所有接收到的参数
```

<details>
<summary>✅ 答案</summary>

```python
def complex_func(a, b, c=100, *args, **kwargs):
    """演示所有参数类型的组合"""
    print(f"位置参数 a: {a}")
    print(f"位置参数 b: {b}")
    print(f"默认参数 c: {c}")
    print(f"可变参数 *args: {args}")
    print(f"可变关键字参数 **kwargs: {kwargs}")

# 调用
complex_func(1, 2, 3, 4, 5, x=10, y=20)
# 位置参数 a: 1
# 位置参数 b: 2
# 默认参数 c: 3
# 可变参数 *args: (4, 5)
# 可变关键字参数 **kwargs: {'x': 10, 'y': 20}

print("-" * 20)

# 使用默认参数 c
complex_func(1, 2, 4, 5, x=10, y=20)
# 位置参数 a: 1
# 位置参数 b: 2
# 默认参数 c: 4
# 可变参数 *args: (5,)
# 可变关键字参数 **kwargs: {'x': 10, 'y': 20}
```

**知识点**：
- **参数顺序**：`位置参数` -> `默认参数` -> `*args` -> `**kwargs`
- 这是Python函数定义的标准顺序。

</details>

---

## 题目7：变量作用域 ⭐⭐⭐

**题目**：理解局部作用域、全局作用域和 `global` 关键字。

```python
# 任务：
# 1. 定义一个全局变量 `count`
# 2. 定义一个函数，尝试修改全局变量（不使用 global）
# 3. 定义另一个函数，使用 `global` 关键字修改全局变量
```

<details>
<summary>✅ 答案</summary>

```python
# 全局变量
count = 10

def attempt_modify():
    # 尝试修改会创建一个新的局部变量 count
    count = 20
    print(f"函数内部 (局部变量): {count}")

def modify_global():
    # 使用 global 关键字声明要修改全局变量
    global count
    count = 30
    print(f"函数内部 (修改全局): {count}")

print(f"初始全局变量: {count}")  # 10

attempt_modify()
print(f"调用 attempt_modify 后 (全局变量不变): {count}") # 10

modify_global()
print(f"调用 modify_global 后 (全局变量已修改): {count}") # 30
```

**知识点**：
- **局部作用域 (Local)**：函数内部定义的变量。
- **全局作用域 (Global)**：在所有函数外部定义的变量。
- **`global` 关键字**：在函数内部修改全局变量时必须使用。
- **LEGB 规则**：Python查找变量的顺序：`Local` -> `Enclosing` -> `Global` -> `Built-in`

</details>

---

## 题目8：Lambda 表达式 ⭐⭐

**题目**：使用 lambda 表达式简化代码。

```python
# 任务：
# 1. 使用 lambda 定义一个计算平方的函数
# 2. 使用 lambda 对一个字典列表按年龄排序
# 3. 使用 lambda 筛选出列表中的偶数
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 计算平方
square = lambda x: x ** 2
print(f"5的平方: {square(5)}")  # 25

# 2. 按年龄排序
students = [
    {"name": "张三", "age": 20},
    {"name": "李四", "age": 18},
    {"name": "王五", "age": 22}
]
sorted_students = sorted(students, key=lambda s: s["age"])
print(f"按年龄排序后: {sorted_students}")
# [{'name': '李四', 'age': 18}, {'name': '张三', 'age': 20}, {'name': '王五', 'age': 22}]

# 3. 筛选偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"列表中的偶数: {evens}") # [2, 4, 6, 8]
```

**知识点**：
- `lambda arguments: expression`
- lambda 是一个匿名函数，通常用于需要一个简单函数的地方。
- 常与 `sorted()`, `map()`, `filter()` 等函数结合使用。

</details>

---

## 题目9：递归函数 ⭐⭐⭐

**题目**：使用递归函数计算阶乘。

```python
# 任务：
# 1. 定义一个名为 `factorial` 的递归函数
# 2. 递归的基线条件是 n=0 或 n=1
# 3. 递归步骤是 n * factorial(n-1)
```

<details>
<summary>✅ 答案</summary>

```python
def factorial(n):
    """使用递归计算阶乘"""
    # 基线条件
    if n == 0 or n == 1:
        return 1
    # 递归步骤
    else:
        return n * factorial(n - 1)

# 测试
print(f"5! = {factorial(5)}")  # 5! = 120
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1 = 120

print(f"0! = {factorial(0)}")  # 0! = 1
```

**知识点**：
- **递归函数**：一个调用自身的函数。
- **基线条件 (Base Case)**：停止递归的条件。
- **递归步骤 (Recursive Step)**：将问题分解并调用自身。

**⚠️ 注意**：
- 必须有基线条件，否则会导致无限递归和栈溢出错误。

</details>

---

## 题目10：综合练习 ⭐⭐⭐⭐

**题目**：创建一个简单的计算器函数，支持多种运算。

```python
# 任务：
# 1. 定义一个名为 `calculate` 的函数
# 2. 第一个参数是运算符字符串（如 '+', '-', '*', '/'）
# 3. 后续参数是任意数量的操作数
# 4. 函数根据运算符执行相应的计算
# 5. 如果运算符无效，返回 "无效的运算符"
```

<details>
<summary>✅ 答案</summary>

```python
def calculate(operator, *args):
    """一个简单的计算器函数"""
    if not args:
        return 0  # 没有操作数则返回0

    if operator == '+':
        return sum(args)
    
    elif operator == '-':
        # 从第一个数开始减
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
        
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result
        
    elif operator == '/':
        result = args[0]
        for num in args[1:]:
            if num == 0:
                return "错误：除数不能为0"
            result /= num
        return result
        
    else:
        return "无效的运算符"

# 测试
print(f"1+2+3 = {calculate('+', 1, 2, 3)}")             # 6
print(f"10-2-3 = {calculate('-', 10, 2, 3)}")           # 5
print(f"2*3*4 = {calculate('*', 2, 3, 4)}")             # 24
print(f"100/5/2 = {calculate('/', 100, 5, 2)}")         # 10.0
print(f"10/0 = {calculate('/', 10, 0)}")               # 错误：除数不能为0
print(f"求模运算: {calculate('%', 10, 3)}")            # 无效的运算符
```

**知识点**：
- 函数设计与封装
- `*args` 的灵活应用
- `if/elif/else` 结构
- 边界条件处理（如空参数、除以0）

</details>

---

## 🎯 知识点总结

### 必须掌握
- ✅ 函数定义：`def` 和 `return`
- ✅ 参数：位置参数、默认参数
- ✅ 返回值：单个和多个（元组）
- ✅ 变量作用域：局部 vs 全局

### 加分项
- 可变参数：`*args` 和 `**kwargs`
- `lambda` 表达式
- 递归函数
- 函数作为参数传递（如 `sorted` 的 `key`）

---

## 📝 自我检测

完成以上题目后，问自己：
- [ ] 能否清晰地定义一个函数并调用它？
- [ ] 理解不同参数类型（位置、默认、可变）的区别和顺序？
- [ ] 知道 `global` 关键字的用途吗？
- [ ] 能否用 `lambda` 表达式写一个简单的匿名函数？
- [ ] 理解递归函数的基本原理（基线条件和递归步骤）？

如果都能做到，恭喜你已经掌握了 Python 函数！🎉

**下一步**：[07_文件操作练习](07_file_exercises.md)