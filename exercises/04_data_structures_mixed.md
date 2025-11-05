# 📝 04_综合数据结构练习

> **知识点**：列表、字典、元组、集合的综合应用

---

## 题目1：数据结构选择 ⭐⭐

**题目**：为以下场景选择合适的数据结构。

```python
# 场景1：存储班级学生的姓名（不重复，无序）
# 场景2：存储学生的考试成绩（学号 -> 分数）
# 场景3：存储一个坐标点（x, y）（不可修改）
# 场景4：存储待办事项列表（有序，可修改）
```

<details>
<summary>✅ 答案</summary>

```python
# 场景1：存储班级学生的姓名（不重复，无序）
# 使用集合 set
students = {"张三", "李四", "王五"}
students.add("赵六")
print(students)  # {'张三', '李四', '王五', '赵六'}

# 场景2：存储学生的考试成绩（学号 -> 分数）
# 使用字典 dict
scores = {
    "S001": 85,
    "S002": 92,
    "S003": 78
}
print(scores["S001"])  # 85

# 场景3：存储一个坐标点（x, y）（不可修改）
# 使用元组 tuple
point = (10, 20)
print(point[0], point[1])  # 10 20

# 场景4：存储待办事项列表（有序，可修改）
# 使用列表 list
todos = ["写作业", "复习Python", "锻炼身体"]
todos.append("阅读")
print(todos)  # ['写作业', '复习Python', '锻炼身体', '阅读']
```

**数据结构对比**：

| 数据结构 | 有序 | 可变 | 重复 | 用途 |
|---------|------|------|------|------|
| 列表 list | ✅ | ✅ | ✅ | 有序集合 |
| 元组 tuple | ✅ | ❌ | ✅ | 不可变序列 |
| 集合 set | ❌ | ✅ | ❌ | 去重、集合运算 |
| 字典 dict | ✅* | ✅ | ❌ | 键值对映射 |

*Python 3.7+ 字典保持插入顺序
</details>

---

## 题目2：列表与字典转换 ⭐⭐

**题目**：在列表和字典之间进行转换。

```python
# 任务1：将两个列表转换为字典
keys = ["name", "age", "city"]
values = ["张三", 18, "北京"]

# 任务2：将字典转换为两个列表
student = {"name": "李四", "age": 19, "city": "上海"}
```

<details>
<summary>✅ 答案</summary>

```python
# 任务1：将两个列表转换为字典
keys = ["name", "age", "city"]
values = ["张三", 18, "北京"]

# 方法1：使用 zip()
student_dict = dict(zip(keys, values))
print(student_dict)
# {'name': '张三', 'age': 18, 'city': '北京'}

# 方法2：使用字典推导式
student_dict = {keys[i]: values[i] for i in range(len(keys))}
print(student_dict)

# 任务2：将字典转换为两个列表
student = {"name": "李四", "age": 19, "city": "上海"}

# 方法1：使用 keys() 和 values()
keys = list(student.keys())
values = list(student.values())
print(keys)    # ['name', 'age', 'city']
print(values)  # ['李四', 19, '上海']

# 方法2：使用 zip() 和 items()
keys, values = zip(*student.items())
keys = list(keys)
values = list(values)
print(keys)    # ('name', 'age', 'city')
print(values)  # ('李四', 19, '上海')
```

**知识点**：
- `zip()` 函数打包多个序列
- `dict()` 构造函数
- `keys()` 和 `values()` 方法
- `*` 解包运算符
</details>

---

## 题目3：集合运算 ⭐⭐

**题目**：使用集合进行数学运算。

```python
class_a = {"张三", "李四", "王五", "赵六"}
class_b = {"王五", "赵六", "孙七", "周八"}

# 任务：
# 1. 找出两个班都有的学生（交集）
# 2. 找出所有学生（并集）
# 3. 找出只在 A 班的学生（差集）
# 4. 找出只在一个班的学生（对称差集）
```

<details>
<summary>✅ 答案</summary>

```python
class_a = {"张三", "李四", "王五", "赵六"}
class_b = {"王五", "赵六", "孙七", "周八"}

# 1. 交集（两个班都有的学生）
both = class_a & class_b
# 或 both = class_a.intersection(class_b)
print(both)  # {'王五', '赵六'}

# 2. 并集（所有学生）
all_students = class_a | class_b
# 或 all_students = class_a.union(class_b)
print(all_students)  # {'张三', '李四', '王五', '赵六', '孙七', '周八'}

# 3. 差集（只在 A 班的学生）
only_a = class_a - class_b
# 或 only_a = class_a.difference(class_b)
print(only_a)  # {'张三', '李四'}

# 4. 对称差集（只在一个班的学生）
only_one = class_a ^ class_b
# 或 only_one = class_a.symmetric_difference(class_b)
print(only_one)  # {'张三', '李四', '孙七', '周八'}
```

**集合运算符**：

| 运算 | 符号 | 方法 | 说明 |
|------|------|------|------|
| 交集 | `&` | `intersection()` | 两个集合都有的元素 |
| 并集 | `\|` | `union()` | 两个集合所有元素 |
| 差集 | `-` | `difference()` | A有B没有的元素 |
| 对称差集 | `^` | `symmetric_difference()` | 只在一个集合中的元素 |

**💡 可视化**：
```
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

交集 A & B = {3, 4}
并集 A | B = {1, 2, 3, 4, 5, 6}
差集 A - B = {1, 2}
对称差集 A ^ B = {1, 2, 5, 6}
```
</details>

---

## 题目4：元组解包 ⭐⭐

**题目**：使用元组解包简化代码。

```python
# 任务：
# 1. 交换两个变量的值
# 2. 从函数返回多个值
# 3. 遍历字典时同时获取键和值
# 4. 解包嵌套元组
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 交换两个变量的值
a = 10
b = 20
a, b = b, a
print(a, b)  # 20 10

# 2. 从函数返回多个值
def get_student_info():
    name = "张三"
    age = 18
    score = 85
    return name, age, score  # 返回元组

name, age, score = get_student_info()
print(f"{name}, {age}岁, {score}分")
# 张三, 18岁, 85分

# 3. 遍历字典时同时获取键和值
scores = {"语文": 90, "数学": 85, "英语": 92}
for subject, score in scores.items():
    print(f"{subject}: {score}分")

# 4. 解包嵌套元组
point = ((1, 2), (3, 4))
(x1, y1), (x2, y2) = point
print(f"点1: ({x1}, {y1})")  # 点1: (1, 2)
print(f"点2: ({x2}, {y2})")  # 点2: (3, 4)

# 扩展：使用 * 收集剩余元素
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

**知识点**：
- 元组解包（Tuple Unpacking）
- 多重赋值
- `*` 收集剩余元素
- 函数返回多个值
</details>

---

## 题目5：嵌套数据结构 ⭐⭐⭐

**题目**：处理复杂的嵌套数据结构。

```python
# 学校数据结构
school = {
    "name": "实验中学",
    "classes": [
        {
            "name": "高一1班",
            "students": [
                {"name": "张三", "scores": [85, 90, 88]},
                {"name": "李四", "scores": [92, 88, 95]}
            ]
        },
        {
            "name": "高一2班",
            "students": [
                {"name": "王五", "scores": [78, 82, 80]},
                {"name": "赵六", "scores": [95, 92, 98]}
            ]
        }
    ]
}

# 任务：
# 1. 获取"高一1班"的所有学生姓名
# 2. 计算每个学生的平均分
# 3. 找出全校平均分最高的学生
```

<details>
<summary>✅ 答案</summary>

```python
school = {
    "name": "实验中学",
    "classes": [
        {
            "name": "高一1班",
            "students": [
                {"name": "张三", "scores": [85, 90, 88]},
                {"name": "李四", "scores": [92, 88, 95]}
            ]
        },
        {
            "name": "高一2班",
            "students": [
                {"name": "王五", "scores": [78, 82, 80]},
                {"name": "赵六", "scores": [95, 92, 98]}
            ]
        }
    ]
}

# 1. 获取"高一1班"的所有学生姓名
class_1 = school["classes"][0]
student_names = [student["name"] for student in class_1["students"]]
print(student_names)  # ['张三', '李四']

# 2. 计算每个学生的平均分
print("\n每个学生的平均分：")
for class_info in school["classes"]:
    print(f"\n{class_info['name']}:")
    for student in class_info["students"]:
        avg = sum(student["scores"]) / len(student["scores"])
        print(f"  {student['name']}: {avg:.2f}分")

# 输出：
# 高一1班:
#   张三: 87.67分
#   李四: 91.67分
# 高一2班:
#   王五: 80.00分
#   赵六: 95.00分

# 3. 找出全校平均分最高的学生
best_student = None
best_avg = 0

for class_info in school["classes"]:
    for student in class_info["students"]:
        avg = sum(student["scores"]) / len(student["scores"])
        if avg > best_avg:
            best_avg = avg
            best_student = student["name"]

print(f"\n全校平均分最高：{best_student}（{best_avg:.2f}分）")
# 全校平均分最高：赵六（95.00分）
```

**知识点**：
- 多层嵌套访问
- 列表推导式
- 嵌套循环
- 数据聚合计算
</details>

---

## 题目6：数据去重与统计 ⭐⭐⭐

**题目**：处理包含重复数据的列表。

```python
data = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 19},
    {"name": "张三", "age": 18},  # 重复
    {"name": "王五", "age": 18},
    {"name": "李四", "age": 19}   # 重复
]

# 任务：
# 1. 去除重复的字典
# 2. 统计每个年龄有多少人
# 3. 找出所有不重复的姓名
```

<details>
<summary>✅ 答案</summary>

```python
data = [
    {"name": "张三", "age": 18},
    {"name": "李四", "age": 19},
    {"name": "张三", "age": 18},
    {"name": "王五", "age": 18},
    {"name": "李四", "age": 19}
]

# 1. 去除重复的字典
# 方法1：转换为元组（字典不可哈希，元组可以）
unique_data = []
seen = set()

for item in data:
    # 将字典转换为元组
    item_tuple = tuple(sorted(item.items()))
    if item_tuple not in seen:
        seen.add(item_tuple)
        unique_data.append(item)

print("去重后：")
for item in unique_data:
    print(item)
# {'name': '张三', 'age': 18}
# {'name': '李四', 'age': 19}
# {'name': '王五', 'age': 18}

# 方法2：使用 JSON 字符串
import json
unique_data = []
seen = set()

for item in data:
    item_str = json.dumps(item, sort_keys=True)
    if item_str not in seen:
        seen.add(item_str)
        unique_data.append(item)

# 2. 统计每个年龄有多少人
age_count = {}
for item in data:
    age = item["age"]
    age_count[age] = age_count.get(age, 0) + 1

print("\n年龄统计：")
for age, count in age_count.items():
    print(f"{age}岁: {count}人")
# 18岁: 3人
# 19岁: 2人

# 3. 找出所有不重复的姓名
names = [item["name"] for item in data]
unique_names = list(set(names))
print(f"\n不重复的姓名：{unique_names}")
# ['张三', '李四', '王五']
```

**知识点**：
- 字典去重技巧
- 集合的应用
- 数据统计
- `tuple()` 和 `sorted()` 的组合使用
</details>

---

## 题目7：数据转换 ⭐⭐⭐

**题目**：将列表数据转换为字典格式。

```python
# 原始数据（列表格式）
students = [
    ["张三", 18, 85],
    ["李四", 19, 92],
    ["王五", 18, 78]
]

# 目标格式（字典格式）
# [
#     {"name": "张三", "age": 18, "score": 85},
#     {"name": "李四", "age": 19, "score": 92},
#     {"name": "王五", "age": 18, "score": 78}
# ]
```

<details>
<summary>✅ 答案</summary>

```python
students = [
    ["张三", 18, 85],
    ["李四", 19, 92],
    ["王五", 18, 78]
]

# 方法1：使用列表推导式
keys = ["name", "age", "score"]
students_dict = [dict(zip(keys, student)) for student in students]
print(students_dict)

# 方法2：手动构建
students_dict = []
for student in students:
    student_dict = {
        "name": student[0],
        "age": student[1],
        "score": student[2]
    }
    students_dict.append(student_dict)

print(students_dict)

# 输出：
# [
#     {'name': '张三', 'age': 18, 'score': 85},
#     {'name': '李四', 'age': 19, 'score': 92},
#     {'name': '王五', 'age': 18, 'score': 78}
# ]

# 反向转换：字典转列表
students_list = [[s["name"], s["age"], s["score"]] for s in students_dict]
print(students_list)
# [['张三', 18, 85], ['李四', 19, 92], ['王五', 18, 78]]
```

**知识点**：
- `zip()` 函数
- 列表推导式
- 字典构造
- 数据格式转换
</details>

---

## 题目8：数据过滤与排序 ⭐⭐⭐

**题目**：对学生数据进行过滤和排序。

```python
students = [
    {"name": "张三", "age": 18, "score": 85, "city": "北京"},
    {"name": "李四", "age": 19, "score": 92, "city": "上海"},
    {"name": "王五", "age": 18, "score": 78, "city": "北京"},
    {"name": "赵六", "age": 20, "score": 95, "city": "广州"},
    {"name": "孙七", "age": 19, "score": 88, "city": "上海"}
]

# 任务：
# 1. 筛选出分数大于 85 的学生
# 2. 筛选出北京的 18 岁学生
# 3. 按分数降序排序
# 4. 按年龄升序、分数降序排序
```

<details>
<summary>✅ 答案</summary>

```python
students = [
    {"name": "张三", "age": 18, "score": 85, "city": "北京"},
    {"name": "李四", "age": 19, "score": 92, "city": "上海"},
    {"name": "王五", "age": 18, "score": 78, "city": "北京"},
    {"name": "赵六", "age": 20, "score": 95, "city": "广州"},
    {"name": "孙七", "age": 19, "score": 88, "city": "上海"}
]

# 1. 筛选出分数大于 85 的学生
high_scores = [s for s in students if s["score"] > 85]
print("分数大于85：")
for s in high_scores:
    print(f"  {s['name']}: {s['score']}分")
# 李四: 92分
# 赵六: 95分
# 孙七: 88分

# 2. 筛选出北京的 18 岁学生
beijing_18 = [s for s in students if s["city"] == "北京" and s["age"] == 18]
print("\n北京18岁学生：")
for s in beijing_18:
    print(f"  {s['name']}")
# 张三
# 王五

# 3. 按分数降序排序
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)
print("\n按分数降序：")
for s in sorted_by_score:
    print(f"  {s['name']}: {s['score']}分")
# 赵六: 95分
# 李四: 92分
# 孙七: 88分
# 张三: 85分
# 王五: 78分

# 4. 按年龄升序、分数降序排序
sorted_multi = sorted(students, key=lambda x: (x["age"], -x["score"]))
print("\n按年龄升序、分数降序：")
for s in sorted_multi:
    print(f"  {s['name']}: {s['age']}岁, {s['score']}分")
# 张三: 18岁, 85分
# 王五: 18岁, 78分
# 李四: 19岁, 92分
# 孙七: 19岁, 88分
# 赵六: 20岁, 95分
```

**知识点**：
- 列表推导式过滤
- `sorted()` 函数
- `lambda` 表达式
- 多条件排序（使用元组）

**💡 多条件排序技巧**：
```python
# 年龄升序，分数降序
sorted(students, key=lambda x: (x["age"], -x["score"]))

# 解释：
# 1. 先按年龄升序（x["age"]）
# 2. 年龄相同时，按分数降序（-x["score"]）
```
</details>

---

## 题目9：数据分组与聚合 ⭐⭐⭐

**题目**：对数据进行分组统计。

```python
sales = [
    {"product": "苹果", "category": "水果", "price": 5, "quantity": 10},
    {"product": "香蕉", "category": "水果", "price": 3, "quantity": 15},
    {"product": "白菜", "category": "蔬菜", "price": 2, "quantity": 20},
    {"product": "西红柿", "category": "蔬菜", "price": 4, "quantity": 12}
]

# 任务：
# 1. 按类别分组
# 2. 计算每个类别的总销售额
# 3. 找出每个类别销量最高的产品
```

<details>
<summary>✅ 答案</summary>

```python
sales = [
    {"product": "苹果", "category": "水果", "price": 5, "quantity": 10},
    {"product": "香蕉", "category": "水果", "price": 3, "quantity": 15},
    {"product": "白菜", "category": "蔬菜", "price": 2, "quantity": 20},
    {"product": "西红柿", "category": "蔬菜", "price": 4, "quantity": 12}
]

# 1. 按类别分组
grouped = {}
for item in sales:
    category = item["category"]
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(item)

print("按类别分组：")
for category, items in grouped.items():
    print(f"\n{category}:")
    for item in items:
        print(f"  {item['product']}")

# 2. 计算每个类别的总销售额
print("\n每个类别的总销售额：")
for category, items in grouped.items():
    total = sum(item["price"] * item["quantity"] for item in items)
    print(f"{category}: {total}元")
# 水果: 95元
# 蔬菜: 88元

# 3. 找出每个类别销量最高的产品
print("\n每个类别销量最高的产品：")
for category, items in grouped.items():
    best = max(items, key=lambda x: x["quantity"])
    print(f"{category}: {best['product']}（{best['quantity']}件）")
# 水果: 香蕉（15件）
# 蔬菜: 白菜（20件）
```

**知识点**：
- 数据分组
- 聚合计算
- `max()` 函数
- 生成器表达式
</details>

---

## 题目10：综合练习 ⭐⭐⭐⭐

**题目**：实现一个简单的图书管理系统。

```python
# 要求：
# 1. 使用字典存储图书信息（书名、作者、价格、库存）
# 2. 使用列表存储借阅记录（借阅人、书名、日期）
# 3. 实现以下功能：
#    - 添加图书
#    - 借阅图书（库存-1）
#    - 归还图书（库存+1）
#    - 查询某本书的借阅历史
#    - 统计最受欢迎的图书（借阅次数最多）
```

<details>
<summary>✅ 答案</summary>

```python
# 图书管理系统
books = {}  # {书名: {"author": 作者, "price": 价格, "stock": 库存}}
records = []  # [{"borrower": 借阅人, "book": 书名, "date": 日期, "action": "借出/归还"}]

def add_book(title, author, price, stock):
    """添加图书"""
    books[title] = {
        "author": author,
        "price": price,
        "stock": stock
    }
    print(f"已添加：《{title}》- {author}，库存{stock}本")

def borrow_book(borrower, title, date):
    """借阅图书"""
    if title not in books:
        print(f"错误：图书《{title}》不存在")
        return False
    
    if books[title]["stock"] <= 0:
        print(f"错误：《{title}》库存不足")
        return False
    
    books[title]["stock"] -= 1
    records.append({
        "borrower": borrower,
        "book": title,
        "date": date,
        "action": "借出"
    })
    print(f"{borrower} 借阅了《{title}》，剩余库存{books[title]['stock']}本")
    return True

def return_book(borrower, title, date):
    """归还图书"""
    if title not in books:
        print(f"错误：图书《{title}》不存在")
        return False
    
    books[title]["stock"] += 1
    records.append({
        "borrower": borrower,
        "book": title,
        "date": date,
        "action": "归还"
    })
    print(f"{borrower} 归还了《{title}》，当前库存{books[title]['stock']}本")
    return True

def query_history(title):
    """查询借阅历史"""
    history = [r for r in records if r["book"] == title]
    if not history:
        print(f"《{title}》暂无借阅记录")
        return
    
    print(f"\n《{title}》借阅历史：")
    for record in history:
        print(f"  {record['date']} - {record['borrower']} {record['action']}")

def most_popular():
    """统计最受欢迎的图书"""
    borrow_count = {}
    for record in records:
        if record["action"] == "借出":
            book = record["book"]
            borrow_count[book] = borrow_count.get(book, 0) + 1
    
    if not borrow_count:
        print("暂无借阅记录")
        return
    
    most_borrowed = max(borrow_count.items(), key=lambda x: x[1])
    print(f"\n最受欢迎的图书：《{most_borrowed[0]}》，借阅{most_borrowed[1]}次")

# 测试
print("=== 图书管理系统 ===\n")

# 添加图书
add_book("Python编程", "张三", 59.9, 5)
add_book("数据结构", "李四", 49.9, 3)
add_book("算法导论", "王五", 89.9, 2)

print("\n--- 借阅操作 ---")
borrow_book("小明", "Python编程", "2024-01-01")
borrow_book("小红", "Python编程", "2024-01-02")
borrow_book("小刚", "数据结构", "2024-01-03")
borrow_book("小明", "算法导论", "2024-01-04")

print("\n--- 归还操作 ---")
return_book("小明", "Python编程", "2024-01-10")

print("\n--- 查询历史 ---")
query_history("Python编程")

print("\n--- 统计信息 ---")
most_popular