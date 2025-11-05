# 📝 01_基础语法练习

> **知识点**：变量、数据类型、运算符、字符串操作

---

## 题目1：变量交换 ⭐

**题目**：不使用第三个变量，交换两个变量的值。

```python
a = 10
b = 20

# 你的代码：交换 a 和 b 的值

print(f"a = {a}, b = {b}")  # 应该输出: a = 20, b = 10
```

<details>
<summary>💡 提示</summary>

Python 支持元组解包，可以一行完成交换。
</details>

<details>
<summary>✅ 答案</summary>

```python
a = 10
b = 20

# 方法1：Python 特有的元组解包（推荐）
a, b = b, a

# 方法2：使用加减法
# a = a + b  # a = 30
# b = a - b  # b = 10
# a = a - b  # a = 20

# 方法3：使用异或（适用于整数）
# a = a ^ b
# b = a ^ b
# a = a ^ b

print(f"a = {a}, b = {b}")  # a = 20, b = 10
```

**知识点**：
- Python 的元组解包
- 多重赋值
</details>

---

## 题目2：类型转换 ⭐

**题目**：将字符串 `"123"` 转换为整数，将整数 `456` 转换为字符串。

```python
str_num = "123"
int_num = 456

# 你的代码：进行类型转换

print(type(converted_int))  # 应该是 <class 'int'>
print(type(converted_str))  # 应该是 <class 'str'>
```

<details>
<summary>✅ 答案</summary>

```python
str_num = "123"
int_num = 456

# 字符串转整数
converted_int = int(str_num)
print(converted_int)  # 123
print(type(converted_int))  # <class 'int'>

# 整数转字符串
converted_str = str(int_num)
print(converted_str)  # "456"
print(type(converted_str))  # <class 'str'>

# 其他常用转换
float_num = float("3.14")  # 字符串转浮点数
bool_val = bool(1)  # 整数转布尔值
```

**知识点**：
- `int()`, `str()`, `float()`, `bool()` 类型转换函数
</details>

---

## 题目3：字符串格式化 ⭐⭐

**题目**：使用三种不同的方法格式化输出学生信息。

```python
name = "Alice"
age = 20
score = 95.5

# 要求输出：姓名: Alice, 年龄: 20, 分数: 95.50
```

<details>
<summary>✅ 答案</summary>

```python
name = "Alice"
age = 20
score = 95.5

# 方法1：f-string（推荐，Python 3.6+）
output1 = f"姓名: {name}, 年龄: {age}, 分数: {score:.2f}"
print(output1)

# 方法2：.format() 方法
output2 = "姓名: {}, 年龄: {}, 分数: {:.2f}".format(name, age, score)
print(output2)

# 方法3：% 格式化
output3 = "姓名: %s, 年龄: %d, 分数: %.2f" % (name, age, score)
print(output3)
```

**知识点**：
- f-string 格式化
- `.format()` 方法
- `%` 格式化
- 浮点数格式化 `:.2f`
</details>

---

## 题目4：字符串切片 ⭐⭐

**题目**：从字符串中提取特定部分。

```python
text = "Python Programming"

# 任务：
# 1. 提取 "Python"
# 2. 提取 "Programming"
# 3. 反转整个字符串
# 4. 提取所有偶数位置的字符
```

<details>
<summary>✅ 答案</summary>

```python
text = "Python Programming"

# 1. 提取 "Python"
python = text[:6]
print(python)  # "Python"

# 或者使用 split
python2 = text.split()[0]
print(python2)  # "Python"

# 2. 提取 "Programming"
programming = text[7:]
print(programming)  # "Programming"

# 或者
programming2 = text.split()[1]
print(programming2)  # "Programming"

# 3. 反转整个字符串
reversed_text = text[::-1]
print(reversed_text)  # "gnimmargorP nohtyP"

# 4. 提取所有偶数位置的字符（索引 0, 2, 4, ...）
even_chars = text[::2]
print(even_chars)  # "Pto rgamn"
```

**知识点**：
- 字符串切片 `[start:stop:step]`
- 负数步长反转字符串
- `split()` 方法
</details>

---

## 题目5：字符串方法 ⭐⭐

**题目**：使用字符串方法完成以下任务。

```python
text = "  Hello, World!  "

# 任务：
# 1. 去除首尾空格
# 2. 转换为大写
# 3. 转换为小写
# 4. 替换 "World" 为 "Python"
# 5. 检查是否以 "Hello" 开头
# 6. 统计 "l" 出现的次数
```

<details>
<summary>✅ 答案</summary>

```python
text = "  Hello, World!  "

# 1. 去除首尾空格
clean = text.strip()
print(repr(clean))  # 'Hello, World!'

# 2. 转换为大写
upper = text.strip().upper()
print(upper)  # "HELLO, WORLD!"

# 3. 转换为小写
lower = text.strip().lower()
print(lower)  # "hello, world!"

# 4. 替换 "World" 为 "Python"
replaced = text.strip().replace("World", "Python")
print(replaced)  # "Hello, Python!"

# 5. 检查是否以 "Hello" 开头
starts = text.strip().startswith("Hello")
print(starts)  # True

# 6. 统计 "l" 出现的次数
count = text.count("l")
print(count)  # 3
```

**知识点**：
- `strip()`, `upper()`, `lower()`
- `replace()`, `startswith()`, `count()`
</details>

---

## 题目6：运算符优先级 ⭐⭐

**题目**：计算以下表达式的结果。

```python
# 不使用计算器，写出结果
result1 = 2 + 3 * 4
result2 = (2 + 3) * 4
result3 = 10 / 2 * 3
result4 = 10 // 3
result5 = 10 % 3
result6 = 2 ** 3
result7 = 5 > 3 and 2 < 4
result8 = 5 > 3 or 2 > 4
```

<details>
<summary>✅ 答案</summary>

```python
result1 = 2 + 3 * 4      # 14 (先乘后加)
result2 = (2 + 3) * 4    # 20 (括号优先)
result3 = 10 / 2 * 3     # 15.0 (从左到右)
result4 = 10 // 3        # 3 (整除)
result5 = 10 % 3         # 1 (取余)
result6 = 2 ** 3         # 8 (幂运算)
result7 = 5 > 3 and 2 < 4  # True (两个都为真)
result8 = 5 > 3 or 2 > 4   # True (至少一个为真)

print(result1)  # 14
print(result2)  # 20
print(result3)  # 15.0
print(result4)  # 3
print(result5)  # 1
print(result6)  # 8
print(result7)  # True
print(result8)  # True
```

**运算符优先级（从高到低）**：
1. `**` (幂)
2. `*`, `/`, `//`, `%` (乘除)
3. `+`, `-` (加减)
4. `<`, `>`, `<=`, `>=`, `==`, `!=` (比较)
5. `not` (逻辑非)
6. `and` (逻辑与)
7. `or` (逻辑或)
</details>

---

## 题目7：输入输出 ⭐

**题目**：编写程序，接收用户输入的姓名和年龄，然后输出问候语。

```python
# 要求：
# 输入：姓名和年龄
# 输出：你好，[姓名]！你今年 [年龄] 岁了。
```

<details>
<summary>✅ 答案</summary>

```python
# 接收输入
name = input("请输入你的姓名: ")
age_str = input("请输入你的年龄: ")

# 类型转换
age = int(age_str)

# 输出
print(f"你好，{name}！你今年 {age} 岁了。")

# 或者一行完成
# age = int(input("请输入你的年龄: "))
```

**知识点**：
- `input()` 函数返回字符串
- 需要手动类型转换
- f-string 格式化输出
</details>

---

## 题目8：字符串拼接 ⭐⭐

**题目**：将列表中的单词拼接成一个句子。

```python
words = ["Python", "is", "awesome"]

# 要求输出：Python is awesome
```

<details>
<summary>✅ 答案</summary>

```python
words = ["Python", "is", "awesome"]

# 方法1：使用 join()（推荐）
sentence = " ".join(words)
print(sentence)  # "Python is awesome"

# 方法2：使用循环
sentence2 = ""
for i, word in enumerate(words):
    if i > 0:
        sentence2 += " "
    sentence2 += word
print(sentence2)  # "Python is awesome"

# 方法3：使用 + 运算符
sentence3 = words[0] + " " + words[1] + " " + words[2]
print(sentence3)  # "Python is awesome"
```

**知识点**：
- `join()` 方法是最高效的字符串拼接方式
- 避免在循环中使用 `+` 拼接字符串（效率低）
</details>

---

## 题目9：布尔值判断 ⭐⭐

**题目**：判断以下值的布尔值。

```python
# 哪些值为 False？
values = [0, "", [], {}, None, False, "0", " "]

# 你的代码：判断每个值的布尔值
```

<details>
<summary>✅ 答案</summary>

```python
values = [0, "", [], {}, None, False, "0", " "]

for value in values:
    print(f"{repr(value):10} -> {bool(value)}")

# 输出:
# 0          -> False
# ''         -> False
# []         -> False
# {}         -> False
# None       -> False
# False      -> False
# '0'        -> True  (非空字符串)
# ' '        -> True  (非空字符串)
```

**Python 中为 False 的值**：
- `False`
- `None`
- 数字 `0`, `0.0`
- 空序列：`""`, `[]`, `()`
- 空字典：`{}`
- 空集合：`set()`

**其他所有值都为 True！**
</details>

---

## 题目10：综合练习 ⭐⭐⭐

**题目**：编写程序，验证密码强度。

```python
# 要求：
# 1. 密码长度至少 8 位
# 2. 包含至少一个大写字母
# 3. 包含至少一个小写字母
# 4. 包含至少一个数字

password = "Abc12345"

# 你的代码：判断密码是否符合要求
```

<details>
<summary>✅ 答案</summary>

```python
def check_password(password):
    """检查密码强度"""
    # 1. 检查长度
    if len(password) < 8:
        return False, "密码长度至少 8 位"
    
    # 2. 检查是否包含大写字母
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return False, "密码必须包含至少一个大写字母"
    
    # 3. 检查是否包含小写字母
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return False, "密码必须包含至少一个小写字母"
    
    # 4. 检查是否包含数字
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False, "密码必须包含至少一个数字"
    
    return True, "密码强度合格"

# 测试
passwords = ["Abc12345", "abc12345", "ABC12345", "Abcdefgh", "Ab1"]

for pwd in passwords:
    valid, message = check_password(pwd)
    print(f"{pwd:15} -> {message}")
```

**更简洁的写法（使用 any()）**：
```python
def check_password_v2(password):
    """检查密码强度（简洁版）"""
    if len(password) < 8:
        return False, "密码长度至少 8 位"
    
    if not any(c.isupper() for c in password):
        return False, "密码必须包含至少一个大写字母"
    
    if not any(c.islower() for c in password):
        return False, "密码必须包含至少一个小写字母"
    
    if not any(c.isdigit() for c in password):
        return False, "密码必须包含至少一个数字"
    
    return True, "密码强度合格"
```

**知识点**：
- 字符串方法：`isupper()`, `islower()`, `isdigit()`
- `any()` 函数
- 生成器表达式
</details>

---

## 🎯 知识点总结

### 必须掌握
- ✅ 变量赋值和交换
- ✅ 类型转换：`int()`, `str()`, `float()`
- ✅ 字符串格式化：f-string
- ✅ 字符串切片：`[start:stop:step]`
- ✅ 常用字符串方法：`strip()`, `split()`, `join()`, `replace()`
- ✅ 运算符优先级
- ✅ `input()` 和 `print()`
- ✅ 布尔值判断

### 加分项
- 元组解包
- `any()` 和 `all()` 函数
- 生成器表达式
- 字符串方法：`isupper()`, `islower()`, `isdigit()`

---

## 📝 自我检测

完成以上题目后，问自己：
- [ ] 能否独立完成所有题目？
- [ ] 理解每道题的解题思路？
- [ ] 能否举一反三，修改题目条件？

如果都能做到，恭喜你已经掌握了 Python 基础语法！🎉

**下一步**：[02_列表练习](02_list_exercises.md)