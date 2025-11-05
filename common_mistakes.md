# ⚠️ 常见错误与陷阱总结

> **专为 C 语言背景学习者设计，助你提前避坑！**

---

### 陷阱 1：缩进错误 (`IndentationError`)

这是从 C 语言转到 Python 最常见的错误。

- **C 习惯**：缩进仅为美观，代码块由 `{}` 定义。
- **Python 规则**：缩进是语法的一部分，用于定义代码块。

```python
# ❌ 错误示例
def my_func():
print("Hello")  # IndentationError: expected an indented block

# ❌ 错误示例
if True:
    print("Line 1")
  print("Line 2")  # IndentationError: unindent does not match any outer indentation level

# ✅ 正确示例
def my_func():
    print("Hello")  # 使用 4 个空格缩进

if True:
    print("Line 1")
    print("Line 2")  # 保持缩进一致
```

**解决方案**：
1. 始终使用 4 个空格进行缩进。
2. 确保同一代码块内的所有语句缩进级别相同。
3. 在 VSCode 等现代编辑器中，`Tab` 键通常会自动转换为空格。

---

### 陷阱 2：忘记 `self` 参数

在 C 语言中，结构体没有类似 `self` 的概念。但在 Python 的类方法中，第一个参数必须是 `self`。

```python
class MyClass:
    # ❌ 错误示例：忘记 self
    # def greet(name):
    #     print(f"Hello, {name}")

    # ✅ 正确示例
    def greet(self, name):
        print(f"Hello, {name}")

# 调用时不需要传递 self
obj = MyClass()
obj.greet("Alice")
```

**解决方案**：记住类中的每个方法（非静态）都必须以 `self` 作为第一个参数。

---

### 陷阱 3：混淆可变与不可变类型

- **不可变类型**：`int`, `float`, `str`, `tuple`。对它们的操作会创建新对象。
- **可变类型**：`list`, `dict`, `set`。对它们的操作会修改对象本身。

#### 字符串的不可变性

```python
# C 语言中，字符数组是可变的
# char s[] = "hello"; s[0] = 'H';

# ❌ Python 中，字符串是不可变的
s = "hello"
# s[0] = "H"  # TypeError: 'str' object does not support item assignment

# ✅ 正确做法：创建新字符串
s = "H" + s[1:]
```

#### 列表作为函数默认参数的陷阱

```python
# ❌ 错误示例：默认参数在多次调用之间共享
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] (不是预期的 [2])
print(add_item(3))  # [1, 2, 3]

# ✅ 正确做法：使用 None 作为默认值
def add_item_correct(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

print(add_item_correct(1))  # [1]
print(add_item_correct(2))  # [2]
```

**解决方案**：
1. 牢记字符串和元组是不可变的。
2. 永远不要使用可变类型（如 `list`, `dict`）作为函数的默认参数。

---

### 陷阱 4：`for` 循环的思维定式

C 语言的 `for` 循环是基于计数器的，而 Python 的是 `for-each`。

```python
my_list = [10, 20, 30]

# ❌ C 风格的错误尝试
# for i in range(len(my_list)):
#     my_list[i] += 5  # 可以工作，但不 Pythonic

# ✅ Pythonic 的方式
for item in my_list:
    print(item)

# 如果需要索引，使用 enumerate
for i, item in enumerate(my_list):
    print(f"Index {i}: {item}")
```

**解决方案**：拥抱 `for-each` 循环。当你需要数字索引时，才考虑使用 `range(len(...))` 或 `enumerate()`。

---

### 陷阱 5：`input()` 返回的是字符串

所有从 `input()` 函数读取的内容都是字符串，即使你输入的是数字。

```python
# ❌ 错误示例
age_str = input("Enter your age: ") # 用户输入 25
# age_next = age_str + 1 # TypeError: can only concatenate str (not "int") to str

# ✅ 正确做法
age = int(input("Enter your age: "))
age_next = age + 1
print(f"Next year you will be {age_next}")
```

**解决方案**：在使用 `input()` 的返回值进行数学运算前，务必使用 `int()` 或 `float()` 进行类型转换。

---

### 陷阱 6：列表复制的误解

在 Python 中，变量是引用。直接赋值 `new_list = old_list` 并不会创建新列表。

```python
old_list = [1, 2, 3]
new_list = old_list  # 只是创建了一个新引用，指向同一个列表

new_list.append(4)

print(f"New list: {new_list}")  # [1, 2, 3, 4]
print(f"Old list: {old_list}")  # [1, 2, 3, 4] (也被修改了!)

# ✅ 正确的复制方法
old_list = [1, 2, 3]
# 方法 1: 使用 copy()
new_list_1 = old_list.copy()
# 方法 2: 使用切片
new_list_2 = old_list[:]

new_list_1.append(4)
print(f"Old list: {old_list}")        # [1, 2, 3] (未改变)
print(f"New list 1: {new_list_1}")  # [1, 2, 3, 4]
```

**解决方案**：需要复制列表时，使用 `list.copy()` 或 `list[:]`。

---

### 陷阱 7：整数除法 vs 浮点数除法

- 在 C 语言中，`5 / 2` 的结果是 `2`（整数除法）。
- 在 Python 3 中，`/` 总是执行浮点数除法，`//` 执行整数除法。

```python
print(f"5 / 2 = {5 / 2}")    # 2.5 (浮点数除法)
print(f"5 // 2 = {5 // 2}")  # 2   (整数除法)
```

**解决方案**：需要整数结果时，使用 `//`。

---

### 陷阱 8：逻辑运算符 `and`, `or` vs `&&`, `||`

C 语言使用 `&&` 和 `||`，而 Python 使用 `and` 和 `or`。

```python
x = 5
y = 10

# ❌ 错误示例
# if (x > 0 && y > 0):
#     ...

# ✅ 正确示例
if x > 0 and y > 0:
    print("Both are positive")
```

**解决方案**：记住 Python 的逻辑运算符是英文单词。

---

### 陷阱 9：`elif` vs `else if`

C 语言使用 `else if`，而 Python 使用 `elif`。

```python
# ❌ 错误示例
# else if score >= 80:
#     ...

# ✅ 正确示例
elif score >= 80:
    print("B")
```

**解决方案**：这是一个纯粹的语法记忆点。

---

### 陷阱 10：`switch` 语句的缺失

Python 没有 `switch-case` 语句。

```c
// C 语言
switch (day) {
    case 1: printf("Monday"); break;
    // ...
}
```

```python
# ✅ Python 替代方案 1: if-elif-else
day = 1
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
# ...

# ✅ Python 替代方案 2: 字典
def get_day_name(day_num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        # ...
    }
    return days.get(day_num, "Unknown day")

print(get_day_name(1)) # Monday
```

**解决方案**：使用 `if-elif-else` 结构或字典映射来替代 `switch`。