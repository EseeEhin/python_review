# 📝 03_字典练习

> **知识点**：字典创建、访问、修改、删除、遍历、方法

---

## 题目1：字典基本操作 ⭐

**题目**：创建一个学生信息字典，并完成基本操作。

```python
# 任务：
# 1. 创建字典存储学生信息（姓名、年龄、成绩）
# 2. 访问学生的姓名
# 3. 修改学生的年龄
# 4. 添加新的键值对（班级）
# 5. 删除成绩信息
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 创建字典
student = {
    "name": "张三",
    "age": 18,
    "score": 95
}
print(student)

# 2. 访问学生的姓名
name = student["name"]
print(name)  # 张三

# 或使用 get() 方法（更安全）
name = student.get("name")
print(name)  # 张三

# 3. 修改学生的年龄
student["age"] = 19
print(student)  # {'name': '张三', 'age': 19, 'score': 95}

# 4. 添加新的键值对
student["class"] = "计算机1班"
print(student)  # {'name': '张三', 'age': 19, 'score': 95, 'class': '计算机1班'}

# 5. 删除成绩信息
del student["score"]
print(student)  # {'name': '张三', 'age': 19, 'class': '计算机1班'}

# 或使用 pop()（会返回被删除的值）
student = {"name": "张三", "age": 18, "score": 95}
score = student.pop("score")
print(score)    # 95
print(student)  # {'name': '张三', 'age': 18}
```

**知识点**：
- 字典创建：`{key: value}`
- 访问：`dict[key]` 或 `dict.get(key)`
- 修改/添加：`dict[key] = value`
- 删除：`del dict[key]` 或 `dict.pop(key)`

**⚠️ 常见错误**：
```python
# 错误：访问不存在的键会报错
student = {"name": "张三"}
print(student["age"])  # KeyError: 'age'

# 正确：使用 get() 方法
print(student.get("age"))  # None
print(student.get("age", 18))  # 18（提供默认值）
```
</details>

---

## 题目2：字典遍历 ⭐⭐

**题目**：遍历字典的不同方式。

```python
scores = {
    "语文": 90,
    "数学": 85,
    "英语": 92
}

# 任务：
# 1. 遍历所有的键
# 2. 遍历所有的值
# 3. 遍历所有的键值对
# 4. 打印格式化的成绩单
```

<details>
<summary>✅ 答案</summary>

```python
scores = {
    "语文": 90,
    "数学": 85,
    "英语": 92
}

# 1. 遍历所有的键
print("方法1：直接遍历")
for subject in scores:
    print(subject)
# 语文
# 数学
# 英语

print("\n方法2：使用 keys()")
for subject in scores.keys():
    print(subject)

# 2. 遍历所有的值
print("\n遍历所有的值：")
for score in scores.values():
    print(score)
# 90
# 85
# 92

# 3. 遍历所有的键值对
print("\n遍历键值对：")
for subject, score in scores.items():
    print(f"{subject}: {score}")
# 语文: 90
# 数学: 85
# 英语: 92

# 4. 打印格式化的成绩单
print("\n=== 成绩单 ===")
for subject, score in scores.items():
    print(f"{subject:4s} {score:3d}分")
print(f"总分：{sum(scores.values())}分")
print(f"平均分：{sum(scores.values()) / len(scores):.1f}分")

# === 成绩单 ===
# 语文  90分
# 数学  85分
# 英语  92分
# 总分：267分
# 平均分：89.0分
```

**知识点**：
- `dict.keys()` 返回所有键
- `dict.values()` 返回所有值
- `dict.items()` 返回所有键值对
- 直接遍历字典等同于遍历键

**💡 技巧**：
```python
# 同时获取索引和键值对
for i, (subject, score) in enumerate(scores.items(), 1):
    print(f"{i}. {subject}: {score}分")
# 1. 语文: 90分
# 2. 数学: 85分
# 3. 英语: 92分
```
</details>

---

## 题目3：字典方法 ⭐⭐

**题目**：使用字典的各种方法。

```python
info = {"name": "李四", "age": 20}

# 任务：
# 1. 获取 "city" 键的值，如果不存在返回 "未知"
# 2. 获取 "hobby" 键的值，如果不存在则设置为 "阅读"
# 3. 更新多个键值对
# 4. 清空字典
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 获取键的值，提供默认值
info = {"name": "李四", "age": 20}
city = info.get("city", "未知")
print(city)  # 未知
print(info)  # {'name': '李四', 'age': 20}（字典未改变）

# 2. 获取键的值，如果不存在则设置
info = {"name": "李四", "age": 20}
hobby = info.setdefault("hobby", "阅读")
print(hobby)  # 阅读
print(info)   # {'name': '李四', 'age': 20, 'hobby': '阅读'}（字典被修改）

# 如果键已存在，返回原值
hobby = info.setdefault("hobby", "运动")
print(hobby)  # 阅读（不会改变）
print(info)   # {'name': '李四', 'age': 20, 'hobby': '阅读'}

# 3. 更新多个键值对
info = {"name": "李四", "age": 20}
new_info = {"age": 21, "city": "北京", "hobby": "编程"}
info.update(new_info)
print(info)
# {'name': '李四', 'age': 21, 'city': '北京', 'hobby': '编程'}

# 4. 清空字典
info.clear()
print(info)  # {}
```

**知识点**：
- `get(key, default)` 安全获取值
- `setdefault(key, default)` 获取或设置默认值
- `update(dict)` 批量更新
- `clear()` 清空字典

**对比表**：

| 方法 | 键不存在时 | 是否修改字典 |
|------|-----------|-------------|
| `dict[key]` | 报错 KeyError | - |
| `get(key)` | 返回 None | ❌ 否 |
| `get(key, default)` | 返回 default | ❌ 否 |
| `setdefault(key, default)` | 返回并设置 default | ✅ 是 |
</details>

---

## 题目4：字典推导式 ⭐⭐⭐

**题目**：使用字典推导式创建字典。

```python
# 任务：
# 1. 创建 1-5 的平方字典 {1: 1, 2: 4, 3: 9, ...}
# 2. 将列表转换为字典（索引为键，元素为值）
# 3. 筛选出分数大于 80 的科目
# 4. 交换字典的键和值
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 创建平方字典
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2. 列表转字典
fruits = ["apple", "banana", "orange"]
fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
print(fruit_dict)  # {0: 'apple', 1: 'banana', 2: 'orange'}

# 3. 筛选分数大于 80 的科目
scores = {"语文": 90, "数学": 75, "英语": 85, "物理": 70}
high_scores = {subject: score for subject, score in scores.items() if score > 80}
print(high_scores)  # {'语文': 90, '英语': 85}

# 4. 交换键和值
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
```

**知识点**：
- 字典推导式：`{key: value for ... in ...}`
- 带条件的字典推导式
- `enumerate()` 的应用

**⚠️ 注意**：
```python
# 交换键值时，如果值有重复，后面的会覆盖前面的
original = {"a": 1, "b": 1, "c": 2}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'b', 2: 'c'}（'a' 被 'b' 覆盖）
```
</details>

---

## 题目5：嵌套字典 ⭐⭐⭐

**题目**：操作嵌套字典（字典中包含字典）。

```python
students = {
    "S001": {"name": "张三", "age": 18, "scores": {"语文": 90, "数学": 85}},
    "S002": {"name": "李四", "age": 19, "scores": {"语文": 88, "数学": 92}},
    "S003": {"name": "王五", "age": 18, "scores": {"语文": 95, "数学": 87}}
}

# 任务：
# 1. 获取 S002 的姓名
# 2. 获取 S001 的数学成绩
# 3. 计算每个学生的总分
# 4. 找出数学成绩最高的学生
```

<details>
<summary>✅ 答案</summary>

```python
students = {
    "S001": {"name": "张三", "age": 18, "scores": {"语文": 90, "数学": 85}},
    "S002": {"name": "李四", "age": 19, "scores": {"语文": 88, "数学": 92}},
    "S003": {"name": "王五", "age": 18, "scores": {"语文": 95, "数学": 87}}
}

# 1. 获取 S002 的姓名
name = students["S002"]["name"]
print(name)  # 李四

# 2. 获取 S001 的数学成绩
math_score = students["S001"]["scores"]["数学"]
print(math_score)  # 85

# 3. 计算每个学生的总分
print("\n学生总分：")
for student_id, info in students.items():
    total = sum(info["scores"].values())
    print(f"{info['name']}: {total}分")
# 张三: 175分
# 李四: 180分
# 王五: 182分

# 4. 找出数学成绩最高的学生
max_math_score = 0
best_student = ""

for student_id, info in students.items():
    math_score = info["scores"]["数学"]
    if math_score > max_math_score:
        max_math_score = math_score
        best_student = info["name"]

print(f"\n数学成绩最高：{best_student}（{max_math_score}分）")
# 数学成绩最高：李四（92分）

# 或使用 max() 函数
best = max(students.items(), key=lambda x: x[1]["scores"]["数学"])
print(f"数学最高：{best[1]['name']}（{best[1]['scores']['数学']}分）")
```

**知识点**：
- 多层字典访问
- 嵌套字典遍历
- `max()` 函数与 `key` 参数
- `lambda` 表达式

**💡 安全访问**：
```python
# 使用 get() 避免 KeyError
name = students.get("S004", {}).get("name", "未知")
print(name)  # 未知
```
</details>

---

## 题目6：字典统计 ⭐⭐

**题目**：统计字符串中每个字符出现的次数。

```python
text = "hello world"

# 任务：
# 1. 统计每个字符出现的次数（包括空格）
# 2. 统计每个字母出现的次数（忽略空格）
# 3. 找出出现次数最多的字符
```

<details>
<summary>✅ 答案</summary>

```python
text = "hello world"

# 1. 统计每个字符出现的次数
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# 或使用 setdefault
char_count = {}
for char in text:
    char_count.setdefault(char, 0)
    char_count[char] += 1

# 2. 统计每个字母出现的次数（忽略空格）
letter_count = {}
for char in text:
    if char != ' ':
        letter_count[char] = letter_count.get(char, 0) + 1
print(letter_count)
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# 3. 找出出现次数最多的字符
max_char = max(char_count, key=char_count.get)
max_count = char_count[max_char]
print(f"出现最多的字符：'{max_char}'，出现 {max_count} 次")
# 出现最多的字符：'l'，出现 3 次

# 或使用 max() 直接获取键值对
max_item = max(char_count.items(), key=lambda x: x[1])
print(f"出现最多：'{max_item[0]}'，{max_item[1]} 次")
```

**知识点**：
- 字典统计模式
- `get()` 方法提供默认值
- `max()` 函数的 `key` 参数

**💡 使用 Counter（标准库）**：
```python
from collections import Counter

text = "hello world"
char_count = Counter(text)
print(char_count)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 获取最常见的 3 个字符
print(char_count.most_common(3))
# [('l', 3), ('o', 2), ('h', 1)]
```
</details>

---

## 题目7：字典合并 ⭐⭐

**题目**：合并多个字典。

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

# 任务：
# 1. 合并字典（后面的覆盖前面的）
# 2. 合并字典（保留所有值，冲突时创建列表）
```

<details>
<summary>✅ 答案</summary>

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"c": 5, "d": 6}

# 1. 合并字典（后面的覆盖前面的）
# 方法1：使用 update()
merged = dict1.copy()
merged.update(dict2)
merged.update(dict3)
print(merged)  # {'a': 1, 'b': 3, 'c': 5, 'd': 6}

# 方法2：使用 ** 解包（Python 3.5+）
merged = {**dict1, **dict2, **dict3}
print(merged)  # {'a': 1, 'b': 3, 'c': 5, 'd': 6}

# 方法3：使用 | 运算符（Python 3.9+）
merged = dict1 | dict2 | dict3
print(merged)  # {'a': 1, 'b': 3, 'c': 5, 'd': 6}

# 2. 合并字典（保留所有值）
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {}
for d in [dict1, dict2]:
    for key, value in d.items():
        if key in merged:
            # 键已存在，转换为列表
            if not isinstance(merged[key], list):
                merged[key] = [merged[key]]
            merged[key].append(value)
        else:
            merged[key] = value

print(merged)  # {'a': 1, 'b': [2, 3], 'c': 4}
```

**知识点**：
- `update()` 方法
- `**` 解包运算符
- `|` 合并运算符（Python 3.9+）
- 字典合并策略

**版本对比**：
```python
# Python 3.5+
merged = {**dict1, **dict2}

# Python 3.9+
merged = dict1 | dict2

# 所有版本
merged = dict1.copy()
merged.update(dict2)
```
</details>

---

## 题目8：字典排序 ⭐⭐⭐

**题目**：对字典进行排序。

```python
scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 95}

# 任务：
# 1. 按键（姓名）排序
# 2. 按值（分数）升序排序
# 3. 按值（分数）降序排序
# 4. 获取分数前 2 名的学生
```

<details>
<summary>✅ 答案</summary>

```python
scores = {"张三": 85, "李四": 92, "王五": 78, "赵六": 95}

# 1. 按键（姓名）排序
sorted_by_name = dict(sorted(scores.items()))
print(sorted_by_name)
# {'张三': 85, '李四': 92, '王五': 78, '赵六': 95}

# 2. 按值（分数）升序排序
sorted_by_score = dict(sorted(scores.items(), key=lambda x: x[1]))
print(sorted_by_score)
# {'王五': 78, '张三': 85, '李四': 92, '赵六': 95}

# 3. 按值（分数）降序排序
sorted_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_desc)
# {'赵六': 95, '李四': 92, '张三': 85, '王五': 78}

# 4. 获取分数前 2 名的学生
top_2 = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2])
print(top_2)
# {'赵六': 95, '李四': 92}

# 或使用列表形式
top_2_list = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:2]
print(top_2_list)
# [('赵六', 95), ('李四', 92)]

for name, score in top_2_list:
    print(f"{name}: {score}分")
# 赵六: 95分
# 李四: 92分
```

**知识点**：
- `sorted()` 函数
- `lambda` 表达式
- `key` 参数指定排序依据
- `reverse` 参数控制升降序

**💡 记忆技巧**：
```python
# sorted() 返回列表，需要转回字典
sorted_items = sorted(dict.items(), key=lambda x: x[1])
sorted_dict = dict(sorted_items)

# 或一行搞定
sorted_dict = dict(sorted(dict.items(), key=lambda x: x[1]))
```
</details>

---

## 题目9：字典分组 ⭐⭐⭐

**题目**：将学生按年龄分组。

```python
students = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 19},
    {"name": "王五", "age": 18},
    {"name": "赵六", "age": 20},
    {"name": "孙七", "age": 19}
]

# 任务：
# 将学生按年龄分组，结果如下：
# {
#     18: ["张三", "王五"],
#     19: ["李四", "孙七"],
#     20: ["赵六"]
# }
```

<details>
<summary>✅ 答案</summary>

```python
students = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 19},
    {"name": "王五", "age": 18},
    {"name": "赵六", "age": 20},
    {"name": "孙七", "age": 19}
]

# 方法1：手动实现
grouped = {}
for student in students:
    age = student["age"]
    name = student["name"]
    
    if age not in grouped:
        grouped[age] = []
    grouped[age].append(name)

print(grouped)
# {18: ['张三', '王五'], 19: ['李四', '孙七'], 20: ['赵六']}

# 方法2：使用 setdefault
grouped = {}
for student in students:
    age = student["age"]
    grouped.setdefault(age, []).append(student["name"])

print(grouped)

# 方法3：使用 defaultdict（标准库）
from collections import defaultdict

grouped = defaultdict(list)
for student in students:
    grouped[student["age"]].append(student["name"])

print(dict(grouped))
```

**知识点**：
- 字典分组模式
- `setdefault()` 的应用
- `defaultdict` 的使用

**💡 扩展**：
```python
# 按多个条件分组（年龄和性别）
students = [
    {"name": "张三", "age": 18, "gender": "男"},
    {"name": "李四", "age": 18, "gender": "女"},
    {"name": "王五", "age": 19, "gender": "男"}
]

grouped = {}
for student in students:
    key = (student["age"], student["gender"])
    grouped.setdefault(key, []).append(student["name"])

print(grouped)
# {(18, '男'): ['张三'], (18, '女'): ['李四'], (19, '男'): ['王五']}
```
</details>

---

## 题目10：综合练习 ⭐⭐⭐

**题目**：实现一个简单的学生成绩管理系统。

```python
# 任务：
# 1. 添加学生成绩
# 2. 查询学生成绩
# 3. 修改学生成绩
# 4. 删除学生记录
# 5. 显示所有学生的平均分
# 6. 显示成绩排名
```

<details>
<summary>✅ 答案</summary>

```python
# 学生成绩管理系统
students = {}

def add_student(name, score):
    """添加学生成绩"""
    students[name] = score
    print(f"已添加：{name} - {score}分")

def query_student(name):
    """查询学生成绩"""
    score = students.get(name)
    if score is not None:
        print(f"{name}的成绩：{score}分")
    else:
        print(f"未找到学生：{name}")
    return score

def update_student(name, score):
    """修改学生成绩"""
    if name in students:
        old_score = students[name]
        students[name] = score
        print(f"已修改：{name} {old_score}分 → {score}分")
    else:
        print(f"未找到学生：{name}")

def delete_student(name):
    """删除学生记录"""
    if name in students:
        score = students.pop(name)
        print(f"已删除：{name}（{score}分）")
    else:
        print(f"未找到学生：{name}")

def show_average():
    """显示平均分"""
    if students:
        avg = sum(students.values()) / len(students)
        print(f"平均分：{avg:.2f}分")
    else:
        print("暂无学生记录")

def show_ranking():
    """显示成绩排名"""
    if students:
        print("\n=== 成绩排名 ===")
        sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)
        for rank, (name, score) in enumerate(sorted_students, 1):
            print(f"{rank}. {name}: {score}分")
    else:
        print("暂无学生记录")

# 测试
add_student("张三", 85)
add_student("李四", 92)
add_student("王五", 78)
add_student("赵六", 95)

print("\n查询成绩：")
query_student("李四")
query_student("孙七")

print("\n修改成绩：")
update_student("张三", 90)

print("\n删除记录：")
delete_student("王五")

print("\n统计信息：")
show_average()
show_ranking()

print("\n当前所有学生：")
print(students)
```

**输出**：
```
已添加：张三 - 85分
已添加：李四 - 92分
已添加：王五 - 78分
已添加：赵六 - 95分

查询成绩：
李四的成绩：92分
未找到学生：孙七

修改成绩：
已修改：张三 85分 → 90分

删除记录：
已删除：王五（78分）

统计信息：
平均分：92.33分

=== 成绩排名 ===
1. 赵六: 95分
2. 李四: 92分
3. 张三: 90分

当前所有学生：
{'张三': 90, '李四': 92, '赵六': 95}
```

**知识点**：
- 字典的增删改查
- 函数封装
- 字典排序
- 统计计算
</details>

---

## 🎯 知识点总结

### 必须掌握
- ✅ 字典创建：`{}`, `dict()`
- ✅ 访问：`dict[key]`, `dict.get(key)`
- ✅ 修改/添加：`dict[key] = value`
- ✅ 删除：`del dict[key]`, `dict.pop(key)`
- ✅ 遍历：`keys()`, `values()`, `items()`
- ✅ 方法：`get()`, `setdefault()`, `update()`, `clear()`

### 加分项
- 字典推导式
- 嵌套字典操作
- 字典排序
- 字典分组
- `defaultdict