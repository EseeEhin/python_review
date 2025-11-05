# 📝 第二部分：核心数据结构（90 分钟）⭐ **考试重点**

> **目标**：掌握 Python 最强大、最常用的数据结构——列表和字典

---

## 📋 本部分学习目标

完成本部分后，你将能够：
- ✅ 熟练使用列表（List）进行数据存储和操作
- ✅ 掌握字典（Dictionary）的键值对操作
- ✅ 理解元组（Tuple）和集合（Set）的基本用法
- ✅ 能够选择合适的数据结构解决实际问题

---

## ⏱️ 时间分配

| 内容 | 时间 | 状态 |
|------|------|------|
| 列表（List）详解 | 35 分钟 | ⬜ |
| 字典（Dictionary）详解 | 35 分钟 | ⬜ |
| 元组与集合简介 | 10 分钟 | ⬜ |
| 休息与练习 | 10 分钟 | ⬜ |

---

## 1️⃣ 列表（List）详解（35 分钟）⭐

### 1.1 列表 vs C 数组

#### 🔵 C 语言的数组

```c
// C 语言：固定长度，单一类型
int numbers[5] = {1, 2, 3, 4, 5};
numbers[0] = 10;  // 修改元素

// ❌ 不能改变长度
// ❌ 不能存储不同类型
// ❌ 不能直接添加/删除元素
```

#### 🐍 Python 的列表

```python
# Python：动态长度，可存储不同类型
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10  # 修改元素

# ✅ 可以改变长度
numbers.append(6)  # [10, 2, 3, 4, 5, 6]

# ✅ 可以存储不同类型
mixed = [1, "hello", 3.14, True, [1, 2, 3]]

# ✅ 可以直接添加/删除元素
numbers.remove(2)  # 删除值为 2 的元素
```

#### 对比表格

| 特性 | C 数组 | Python 列表 |
|------|--------|-------------|
| 长度 | 固定 | 动态（可变） |
| 类型 | 单一类型 | 任意类型 |
| 添加元素 | 不支持 | `append()`, `insert()` |
| 删除元素 | 不支持 | `remove()`, `pop()` |
| 切片 | 需手动实现 | 内置支持 `[start:stop]` |
| 内存 | 连续内存 | 引用数组 |

---

### 1.2 创建列表

```python
# 方法 1：直接创建
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", 3.14, True]

# 方法 2：空列表
empty_list = []
empty_list2 = list()

# 方法 3：使用 range() 创建
numbers = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# 方法 4：列表重复
zeros = [0] * 5  # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]

# 方法 5：列表推导式（后面详细讲）
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

### 1.3 访问列表元素

```python
fruits = ["apple", "banana", "orange", "grape", "mango"]

# 正向索引（从 0 开始）
print(fruits[0])   # "apple"
print(fruits[2])   # "orange"

# 负向索引（从 -1 开始，从右往左）
print(fruits[-1])  # "mango" - 最后一个
print(fruits[-2])  # "grape" - 倒数第二个

# 索引越界会报错
# print(fruits[10])  # IndexError: list index out of range
```

#### 🔵 C 语言对比

```c
// C 语言：只支持正向索引
char *fruits[] = {"apple", "banana", "orange"};
printf("%s\n", fruits[0]);  // "apple"

// ❌ 不支持负向索引
// printf("%s\n", fruits[-1]);  // 错误！
```

---

### 1.4 列表切片（Slicing）⭐ **超级强大**

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基本切片：[start:stop]
print(numbers[2:5])    # [2, 3, 4] - 索引 2 到 4
print(numbers[:5])     # [0, 1, 2, 3, 4] - 从开头到索引 4
print(numbers[5:])     # [5, 6, 7, 8, 9] - 从索引 5 到结尾
print(numbers[:])      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - 完整复制

# 带步长：[start:stop:step]
print(numbers[::2])    # [0, 2, 4, 6, 8] - 每隔一个取一个
print(numbers[1::2])   # [1, 3, 5, 7, 9] - 从索引 1 开始，每隔一个
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - 反转列表！

# 负数索引切片
print(numbers[-3:])    # [7, 8, 9] - 最后 3 个元素
print(numbers[:-3])    # [0, 1, 2, 3, 4, 5, 6] - 除了最后 3 个
```

---

### 1.5 修改列表

```python
fruits = ["apple", "banana", "orange"]

# 修改单个元素
fruits[1] = "grape"
print(fruits)  # ["apple", "grape", "orange"]

# 修改切片（批量修改）
fruits[0:2] = ["kiwi", "mango"]
print(fruits)  # ["kiwi", "mango", "orange"]

# 删除切片
numbers = [0, 1, 2, 3, 4, 5]
del numbers[2:4]
print(numbers)  # [0, 1, 4, 5]
```

---

### 1.6 列表的重要方法 ⭐ **考试必考**

#### 添加元素

```python
fruits = ["apple", "banana"]

# append()：在末尾添加一个元素
fruits.append("orange")
print(fruits)  # ["apple", "banana", "orange"]

# insert()：在指定位置插入元素
fruits.insert(1, "grape")  # 在索引 1 处插入
print(fruits)  # ["apple", "grape", "banana", "orange"]

# extend()：添加多个元素（合并列表）
fruits.extend(["mango", "kiwi"])
print(fruits)  # ["apple", "grape", "banana", "orange", "mango", "kiwi"]

# + 运算符：连接列表（创建新列表）
more_fruits = fruits + ["pear", "peach"]
print(more_fruits)
```

#### 删除元素

```python
fruits = ["apple", "banana", "orange", "grape", "banana"]

# remove()：删除第一个匹配的值
fruits.remove("banana")  # 只删除第一个 "banana"
print(fruits)  # ["apple", "orange", "grape", "banana"]

# pop()：删除并返回指定索引的元素（默认最后一个）
last = fruits.pop()  # 删除最后一个
print(last)    # "banana"
print(fruits)  # ["apple", "orange", "grape"]

second = fruits.pop(1)  # 删除索引 1 的元素
print(second)  # "orange"
print(fruits)  # ["apple", "grape"]

# del：删除指定索引或切片
del fruits[0]
print(fruits)  # ["grape"]

# clear()：清空列表
fruits.clear()
print(fruits)  # []
```

#### 查找与统计

```python
numbers = [1, 2, 3, 2, 4, 2, 5]

# index()：查找元素的索引
pos = numbers.index(3)  # 2
print(pos)

# 查找指定范围内的索引
pos = numbers.index(2, 2)  # 从索引 2 开始查找，返回 3
print(pos)

# count()：统计元素出现次数
count = numbers.count(2)  # 3
print(count)

# in：检查元素是否存在
print(3 in numbers)     # True
print(10 in numbers)    # False
print(10 not in numbers)  # True
```

#### 排序与反转

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort()：原地排序（修改原列表）
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# 降序排序
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted()：返回新的排序列表（不修改原列表）
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] - 未改变
print(sorted_list)  # [1, 1, 3, 4, 5]

# reverse()：原地反转
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# 或使用切片反转（创建新列表）
reversed_list = numbers[::-1]
```

#### 其他常用方法

```python
numbers = [1, 2, 3, 4, 5]

# len()：获取列表长度
print(len(numbers))  # 5

# min() 和 max()：最小值和最大值
print(min(numbers))  # 1
print(max(numbers))  # 5

# sum()：求和
print(sum(numbers))  # 15

# copy()：复制列表
numbers_copy = numbers.copy()
# 或使用切片
numbers_copy2 = numbers[:]
```

---

### 1.7 遍历列表 ⭐ **重要**

```python
fruits = ["apple", "banana", "orange"]

# 方法 1：直接遍历元素（最常用）
for fruit in fruits:
    print(fruit)

# 方法 2：使用索引遍历
for i in range(len(fruits)):
    print(f"索引 {i}: {fruits[i]}")

# 方法 3：同时获取索引和元素（推荐）
for index, fruit in enumerate(fruits):
    print(f"索引 {index}: {fruit}")

# 方法 4：带起始索引的 enumerate
for index, fruit in enumerate(fruits, start=1):
    print(f"第 {index} 个: {fruit}")
```

#### 🔵 C 语言对比

```c
// C 语言：只能用索引遍历
char *fruits[] = {"apple", "banana", "orange"};
int len = 3;

for (int i = 0; i < len; i++) {
    printf("%s\n", fruits[i]);
}
```

---

### 1.8 列表嵌套（二维列表）

```python
# 创建二维列表（类似 C 的二维数组）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 访问元素
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6

# 遍历二维列表
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # 换行

# 使用索引遍历
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
```

---

## 2️⃣ 字典（Dictionary）详解（35 分钟）⭐

### 2.1 字典 vs C 结构体

#### 🔵 C 语言的结构体

```c
// C 语言：固定字段，编译时确定
struct Student {
    char name[50];
    int age;
    float score;
};

struct Student s1;
strcpy(s1.name, "Alice");
s1.age = 20;
s1.score = 95.5;
```

#### 🐍 Python 的字典

```python
# Python：动态键值对，运行时可修改
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5
}

# ✅ 可以动态添加字段
student["grade"] = "A"

# ✅ 可以删除字段
del student["age"]

# ✅ 键和值可以是任意类型
mixed_dict = {
    "name": "Bob",
    42: "answer",
    (1, 2): "tuple key",
    "scores": [90, 85, 88]
}
```

#### 对比表格

| 特性 | C 结构体 | Python 字典 |
|------|----------|-------------|
| 字段 | 固定，编译时确定 | 动态，运行时可变 |
| 访问方式 | `s.field` | `d["key"]` 或 `d.get("key")` |
| 添加字段 | 不支持 | `d["new_key"] = value` |
| 删除字段 | 不支持 | `del d["key"]` |
| 键类型 | 字段名（标识符） | 任意不可变类型 |

---

### 2.2 创建字典

```python
# 方法 1：直接创建
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5
}

# 方法 2：空字典
empty_dict = {}
empty_dict2 = dict()

# 方法 3：使用 dict() 构造函数
student2 = dict(name="Bob", age=21, score=88.0)

# 方法 4：从键值对列表创建
pairs = [("name", "Charlie"), ("age", 22), ("score", 92.0)]
student3 = dict(pairs)

# 方法 5：使用 zip() 创建
keys = ["name", "age", "score"]
values = ["David", 23, 87.5]
student4 = dict(zip(keys, values))

# 方法 6：字典推导式（后面详细讲）
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

### 2.3 访问字典元素

```python
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5
}

# 方法 1：使用 [] 访问（键不存在会报错）
print(student["name"])   # "Alice"
# print(student["grade"])  # KeyError: 'grade'

# 方法 2：使用 get() 方法（推荐，键不存在返回 None 或默认值）
print(student.get("name"))        # "Alice"
print(student.get("grade"))       # None
print(student.get("grade", "N/A"))  # "N/A" - 提供默认值

# 检查键是否存在
if "age" in student:
    print(f"年龄: {student['age']}")

# 检查键不存在
if "grade" not in student:
    print("没有成绩信息")
```

---

### 2.4 修改字典

```python
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5
}

# 修改已有键的值
student["age"] = 21
print(student)  # {"name": "Alice", "age": 21, "score": 95.5}

# 添加新键值对
student["grade"] = "A"
print(student)  # {"name": "Alice", "age": 21, "score": 95.5, "grade": "A"}

# 批量更新（使用 update()）
student.update({"age": 22, "major": "CS"})
print(student)  # 更新 age，添加 major
```

---

### 2.5 删除字典元素

```python
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5,
    "grade": "A"
}

# del：删除指定键
del student["grade"]
print(student)  # {"name": "Alice", "age": 20, "score": 95.5}

# pop()：删除并返回值
age = student.pop("age")
print(age)      # 20
print(student)  # {"name": "Alice", "score": 95.5}

# pop() 提供默认值（键不存在时不报错）
major = student.pop("major", "Unknown")
print(major)  # "Unknown"

# popitem()：删除并返回最后一个键值对（Python 3.7+）
item = student.popitem()
print(item)     # ("score", 95.5)
print(student)  # {"name": "Alice"}

# clear()：清空字典
student.clear()
print(student)  # {}
```

---

### 2.6 字典的重要方法 ⭐ **考试必考**

```python
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5,
    "grade": "A"
}

# keys()：获取所有键
keys = student.keys()
print(keys)  # dict_keys(['name', 'age', 'score', 'grade'])
print(list(keys))  # ['name', 'age', 'score', 'grade']

# values()：获取所有值
values = student.values()
print(values)  # dict_values(['Alice', 20, 95.5, 'A'])
print(list(values))  # ['Alice', 20, 95.5, 'A']

# items()：获取所有键值对
items = student.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 20), ...])
print(list(items))  # [('name', 'Alice'), ('age', 20), ...]

# setdefault()：获取值，如果键不存在则设置默认值
major = student.setdefault("major", "CS")
print(major)    # "CS"
print(student)  # 字典中添加了 "major": "CS"

# copy()：浅复制字典
student_copy = student.copy()

# len()：获取键值对数量
print(len(student))  # 5
```

---

### 2.7 遍历字典 ⭐ **重要**

```python
student = {
    "name": "Alice",
    "age": 20,
    "score": 95.5
}

# 方法 1：遍历键（默认）
for key in student:
    print(key)

# 方法 2：遍历键（显式）
for key in student.keys():
    print(f"{key}: {student[key]}")

# 方法 3：遍历值
for value in student.values():
    print(value)

# 方法 4：遍历键值对（推荐）
for key, value in student.items():
    print(f"{key}: {value}")

# 实际应用：格式化输出
for key, value in student.items():
    print(f"{key:10} : {value}")
```

#### 🔵 C 语言对比

```c
// C 语言：结构体不支持遍历字段
// 需要手动访问每个字段
struct Student s = {"Alice", 20, 95.5};
printf("name: %s\n", s.name);
printf("age: %d\n", s.age);
printf("score: %.2f\n", s.score);
```

---

### 2.8 字典嵌套

```python
# 学生信息系统（字典嵌套）
students = {
    "S001": {
        "name": "Alice",
        "age": 20,
        "scores": {"math": 95, "english": 88, "python": 92}
    },
    "S002": {
        "name": "Bob",
        "age": 21,
        "scores": {"math": 87, "english": 90, "python": 85}
    }
}

# 访问嵌套数据
print(students["S001"]["name"])  # "Alice"
print(students["S001"]["scores"]["math"])  # 95

# 遍历嵌套字典
for student_id, info in students.items():
    print(f"学号: {student_id}")
    print(f"  姓名: {info['name']}")
    print(f"  年龄: {info['age']}")
    print("  成绩:")
    for subject, score in info['scores'].items():
        print(f"    {subject}: {score}")
```

---

## 3️⃣ 元组（Tuple）与集合（Set）简介（10 分钟）

### 3.1 元组（Tuple）：不可变的列表

```python
# 创建元组
point = (3, 4)
colors = ("red", "green", "blue")
single = (42,)  # 单元素元组，注意逗号！

# 访问元素（与列表相同）
print(point[0])   # 3
print(colors[-1])  # "blue"

# 切片（与列表相同）
print(colors[1:])  # ("green", "blue")

# ❌ 不能修改元素
# point[0] = 5  # TypeError: 'tuple' object does not support item assignment

# 遍历元组
for color in colors:
    print(color)

# 元组解包
x, y = point
print(f"x={x}, y={y}")  # x=3, y=4

# 多值返回（实际上返回元组）
def get_min_max(numbers):
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(f"最小值: {min_val}, 最大值: {max_val}")
```

#### 元组 vs 列表

| 特性 | 列表 | 元组 |
|------|------|------|
| 可变性 | 可变 | 不可变 |
| 语法 | `[1, 2, 3]` | `(1, 2, 3)` |
| 性能 | 较慢 | 较快 |
| 用途 | 动态数据 | 固定数据、函数返回值 |

---

### 3.2 集合（Set）：不重复的元素集合

```python
# 创建集合
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "orange"}

# 空集合（注意：{} 是空字典，不是空集合）
empty_set = set()

# 从列表创建集合（自动去重）
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_list)
print(unique_numbers)  # {1, 2, 3, 4, 5}

# 添加元素
fruits.add("grape")
print(fruits)

# 删除元素
fruits.remove("banana")  # 不存在会报错
fruits.discard("kiwi")   # 不存在不报错

# 成员检查（非常快！）
print("apple" in fruits)  # True

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 | set2)  # 并集：{1, 2, 3, 4, 5, 6}
print(set1 & set2)  # 交集：{3, 4}
print(set1 - set2)  # 差集：{1, 2}
print(set1 ^ set2)  # 对称差：{1, 2, 5, 6}

# 遍历集合（无序）
for num in numbers:
    print(num)
```

#### 集合的典型应用

```python
# 应用 1：去重
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']（顺序可能不同）

# 应用 2：快速成员检查
large_set = set(range(1000000))
print(999999 in large_set)  # 非常快！

# 应用 3：找出两个列表的共同元素
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)  # [4, 5]
```

---

## 🎯 本部分小结

### ✅ 你已经掌握了

#### 列表（List）
- 创建：`[1, 2, 3]`、`list(range(10))`
- 访问：正负索引、切片 `[start:stop:step]`
- 修改：`append()`, `insert()`, `remove()`, `pop()`
- 查找：`index()`, `count()`, `in`
- 排序：`sort()`, `sorted()`, `reverse()`
- 遍历：`for item in list`、`enumerate()`

#### 字典（Dictionary）
- 创建：`{"key": "value"}`、`dict()`
- 访问：`d["key"]`、`d.get("key", default)`
- 修改：`d["key"] = value`、`update()`
- 删除：`del d["key"]`、`pop()`
- 方法：`keys()`, `values()`, `items()`
- 遍历：`for key, value in d.items()`

#### 元组（Tuple）
- 不可变的列表
- 用于固定数据和函数返回值

#### 集合（Set）
- 不重复的元素集合
- 用于去重和快速成员检查

---

## 📝 综合练习

### 练习 1：学生成绩管理

```python
# 任务：创建一个学生成绩字典，计算平均分
students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 95, 90]
}

# 你的代码：计算每个学生的平均分
```

<details>
<summary>点击查看答案</summary>

```python
students = {
    "Alice": [85, 90, 88],
    "Bob": [78, 82, 80],
    "Charlie": [92, 95, 90]
}

for name, scores in students.items():
    average = sum(scores) / len(scores)
    print(f"{name} 的平均分: {average:.2f}")
```
</details>

### 练习 2：列表去重并排序

```python
# 任务：给定一个包含重复元素的列表，去重并排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_sorted = sorted(set(numbers))
print(unique_sorted)  # [1, 2, 3, 4, 5, 6, 9]
```
</details>

### 练习 3：统计单词出现次数

```python
# 任务：统计一段文本中每个单词出现的次数
text = "python is great python is fun python is powerful"
# 你的代码：使用字典统计每个单词的出现次数
```

<details>
<summary>点击查看答案</summary>

```python
text = "python is great python is fun python is powerful"

# 方法1：使用字典手动统计
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
# 输出: {'python': 3, 'is': 3, 'great': 1, 'fun': 1, 'powerful': 1}

# 方法2：使用 get() 方法（更简洁）
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

# 方法3：使用 Counter（最简单）
from collections import Counter
words = text.split()
word_count = Counter(words)
print(dict(word_count))
```
</details>

---

## 🎓 恭喜完成第二部分！

你已经掌握了 Python 最核心的数据结构：
- ✅ 列表（List）- 动态数组
- ✅ 字典（Dictionary）- 键值对存储
- ✅ 元组（Tuple）- 不可变序列
- ✅ 集合（Set）- 去重和集合运算

这些是 Python 编程的基石，务必熟练掌握！

**下一步**：继续学习 [第三部分：流程控制与函数](part3_control_functions.md)