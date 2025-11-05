# 📝 07_文件操作练习

> **知识点**：`with open()` 语句、文件读取 (`read`, `readline`, `readlines`)、文件写入 (`write`, `writelines`)、文件模式 (`r`, `w`, `a`)

---

## 题目1：读取文件 ⭐

**题目**：创建一个名为 `hello.txt` 的文件，内容为 "Hello, Python!"，然后读取并打印其内容。

```python
# 任务：
# 1. (手动或用代码) 创建一个 `hello.txt` 文件，写入 "Hello, Python!"
# 2. 使用 `with open()` 读取文件内容
# 3. 打印文件内容
```

<details>
<summary>✅ 答案</summary>

```python
# 步骤1：先用代码创建文件
with open('hello.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, Python!")

# 步骤2 & 3：读取并打印
try:
    with open('hello.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print("文件内容:")
        print(content)
except FileNotFoundError:
    print("错误：文件未找到！")

# 文件内容:
# Hello, Python!
```

**知识点**：
- `open(filename, mode, encoding)` 函数
- **`'w'` 模式**：写入（如果文件存在则覆盖）
- **`'r'` 模式**：读取（默认模式）
- **`encoding='utf-8'`**：处理中文字符时必须指定
- **`with` 语句**：自动管理文件的打开和关闭，无需手动 `f.close()`
- **`try...except`**：捕获 `FileNotFoundError` 异常，使程序更健壮

</details>

---

## 题目2：写入文件 ⭐⭐

**题目**：将一个字符串列表逐行写入到名为 `lines.txt` 的文件中。

```python
# 任务：
# 1. 定义一个包含多行文本的列表
# 2. 使用 'w' 模式打开 `lines.txt`
# 3. 遍历列表，将每个字符串写入文件，并添加换行符
```

<details>
<summary>✅ 答案</summary>

```python
lines_to_write = [
    "这是第一行。",
    "这是第二行。",
    "这是第三行。"
]

# 方法1：使用 for 循环和 write()
with open('lines.txt', 'w', encoding='utf-8') as f:
    for line in lines_to_write:
        f.write(line + '\n')  # 必须手动添加换行符

print("方法1：写入完成。")

# 方法2：使用 writelines()
# 注意：writelines() 不会自动添加换行符，需要提前处理好
lines_with_newline = [line + '\n' for line in lines_to_write]
with open('lines.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines_with_newline)

print("方法2：写入完成。")

# lines.txt 文件内容:
# 这是第一行。
# 这是第二行。
# 这是第三行。
```

**知识点**：
- **`write(string)`**：写入单个字符串。
- **`writelines(list_of_strings)`**：写入一个字符串列表。
- **换行符 `\n`**：`write()` 和 `writelines()` 都不会自动添加换行符，需要手动处理。

</details>

---

## 题目3：追加内容到文件 ⭐⭐

**题目**：向 `hello.txt` 文件末尾追加一行新内容 "Append a new line."。

```python
# 任务：
# 1. 使用 'a' 模式打开 `hello.txt`
# 2. 写入新内容
# 3. 验证文件内容是否已更新
```

<details>
<summary>✅ 答案</summary>

```python
# 先确保 hello.txt 存在且有内容
with open('hello.txt', 'w', encoding='utf-8') as f:
    f.write("Hello, Python!\n")

# 使用 'a' 模式追加
with open('hello.txt', 'a', encoding='utf-8') as f:
    f.write("Append a new line.\n")

print("追加完成。")

# 验证内容
with open('hello.txt', 'r', encoding='utf-8') as f:
    print(f.read())

# 输出:
# Hello, Python!
# Append a new line.
```

**知识点**：
- **`'a'` 模式 (Append)**：在文件末尾追加内容，如果文件不存在则创建。
- `'w'` vs `'a'`：`'w'` 会清空原有内容，`'a'` 会保留原有内容。

</details>

---

## 题目4：逐行读取文件 ⭐⭐

**题目**：读取 `lines.txt` 文件，并在每行内容前加上行号后打印出来。

```python
# 任务：
# 1. 打开 `lines.txt` 文件
# 2. 遍历文件对象，逐行读取
# 3. 使用 enumerate() 添加行号
# 4. 打印 "行号: 内容"
```

<details>
<summary>✅ 答案</summary>

```python
# 先创建 lines.txt
with open('lines.txt', 'w', encoding='utf-8') as f:
    f.writelines(["第一行\n", "第二行\n", "第三行\n"])

# 逐行读取并添加行号
try:
    with open('lines.txt', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            # line.strip() 用于去除行尾的换行符
            print(f"{i}: {line.strip()}")
except FileNotFoundError:
    print("文件不存在！")

# 输出:
# 1: 第一行
# 2: 第二行
# 3: 第三行
```

**知识点**：
- **遍历文件对象**：`for line in f:` 是最高效、最常用的逐行读取方式。
- **`line.strip()`**：从文件中读取的每一行末尾都包含一个看不见的换行符 `\n`，`strip()` 可以去除它。
- **`enumerate(iterable, start)`**：方便地获取行号。

</details>

---

## 题目5：`read()`, `readline()`, `readlines()` 的区别 ⭐⭐⭐

**题目**：分别使用这三个方法读取文件，并解释其区别。

```python
# 任务：
# 1. 创建一个多行文件 `methods.txt`
# 2. 使用 read() 读取并打印
# 3. 使用 readline() 读取并打印
# 4. 使用 readlines() 读取并打印
```

<details>
<summary>✅ 答案</summary>

```python
# 创建文件
file_content = "Line 1\nLine 2\nLine 3\n"
with open('methods.txt', 'w', encoding='utf-8') as f:
    f.write(file_content)

# 1. 使用 read()
print("--- read() ---")
with open('methods.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
    print(f"类型: {type(content)}")
# 输出:
# Line 1
# Line 2
# Line 3
# 类型: <class 'str'>

# 2. 使用 readline()
print("\n--- readline() ---")
with open('methods.txt', 'r', encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(line1, end='') # end='' 避免打印多余的换行
    print(line2, end='')
    print(f"\n类型: {type(line1)}")
# 输出:
# Line 1
# Line 2
# 类型: <class 'str'>

# 3. 使用 readlines()
print("\n--- readlines() ---")
with open('methods.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(lines)
    print(f"类型: {type(lines)}")
# 输出:
# ['Line 1\n', 'Line 2\n', 'Line 3\n']
# 类型: <class 'list'>
```

**知识点总结**：

| 方法 | 返回值类型 | 内容 | 内存占用 | 适用场景 |
|---|---|---|---|---|
| `read()` | `str` | 整个文件的所有内容 | 大（一次性加载） | 读取小文件 |
| `readline()` | `str` | 文件中的**一行**（包括 `\n`） | 小 | 逐行处理，内存敏感 |
| `readlines()` | `list` | 包含所有行的**列表** | 大（一次性加载） | 需要对所有行进行列表操作 |
| `for line in f:` | (迭代器) | 逐行返回内容 | **小 (推荐)** | **大多数逐行读取场景** |

</details>

---

## 题目6：文件复制 ⭐⭐⭐

**题目**：编写一个函数，实现文件复制功能。

```python
# 任务：
# 1. 定义一个函数 `copy_file(source_path, dest_path)`
# 2. 在函数内部，打开源文件进行读取
# 3. 打开目标文件进行写入
# 4. 将源文件的内容写入目标文件
# 5. 添加异常处理
```

<details>
<summary>✅ 答案</summary>

```python
def copy_file(source_path, dest_path):
    """将源文件内容复制到目标文件"""
    try:
        with open(source_path, 'r', encoding='utf-8') as src_f:
            content = src_f.read()
        
        with open(dest_path, 'w', encoding='utf-8') as dest_f:
            dest_f.write(content)
            
        print(f"文件 '{source_path}' 已成功复制到 '{dest_path}'")
        return True
        
    except FileNotFoundError:
        print(f"错误：源文件 '{source_path}' 未找到！")
        return False
    except Exception as e:
        print(f"发生未知错误: {e}")
        return False

# 测试
# 先创建一个源文件
with open('source.txt', 'w', encoding='utf-8') as f:
    f.write("这是源文件。\n")
    f.write("This is the source file.\n")

# 执行复制
copy_file('source.txt', 'destination.txt')

# 验证
with open('destination.txt', 'r', encoding='utf-8') as f:
    print("\n目标文件内容：")
    print(f.read())
```

**知识点**：
- 函数封装
- 读写操作结合
- `try...except` 异常处理

**💡 优化**：
对于大文件，一次性 `read()` 会消耗大量内存。可以逐行复制：
```python
def copy_large_file(source_path, dest_path):
    try:
        with open(source_path, 'r', encoding='utf-8') as src_f:
            with open(dest_path, 'w', encoding='utf-8') as dest_f:
                for line in src_f:
                    dest_f.write(line)
        print("大文件复制完成。")
    except Exception as e:
        print(f"错误: {e}")
```

</details>

---

## 题目7：处理CSV文件 ⭐⭐⭐

**题目**：有一个 `scores.csv` 文件，计算每个学生的总分和平均分。

**scores.csv 内容**:
```csv
姓名,语文,数学,英语
张三,85,90,88
李四,92,88,95
王五,78,82,80
```

```python
# 任务：
# 1. 读取 `scores.csv` 文件
# 2. 跳过表头（第一行）
# 3. 对每一行数据进行处理，计算总分和平均分
# 4. 打印结果
```

<details>
<summary>✅ 答案</summary>

```python
# 创建 scores.csv 文件
csv_content = """姓名,语文,数学,英语
张三,85,90,88
李四,92,88,95
王五,78,82,80
"""
with open('scores.csv', 'w', encoding='utf-8') as f:
    f.write(csv_content)

# 处理CSV文件
try:
    with open('scores.csv', 'r', encoding='utf-8') as f:
        # 读取表头
        header = f.readline().strip().split(',')
        print(f"表头: {header}")
        
        print("\n--- 学生成绩统计 ---")
        # 遍历数据行
        for line in f:
            parts = line.strip().split(',')
            name = parts[0]
            # 将分数从字符串转换为整数
            scores = [int(s) for s in parts[1:]]
            
            total_score = sum(scores)
            avg_score = total_score / len(scores)
            
            print(f"{name}: 总分 {total_score}, 平均分 {avg_score:.2f}")
            
except FileNotFoundError:
    print("scores.csv 文件未找到！")

# 输出:
# 表头: ['姓名', '语文', '数学', '英语']
#
# --- 学生成绩统计 ---
# 张三: 总分 263, 平均分 87.67
# 李四: 总分 275, 平均分 91.67
# 王五: 总分 240, 平均分 80.00
```

**知识点**：
- `split(',')` 分割CSV行
- `strip()` 去除空白和换行符
- 列表推导式进行类型转换
- 文件数据解析

**💡 专业处理**：
实际项目中，应使用 Python 内置的 `csv` 模块来处理CSV文件，它能更好地处理特殊字符和引号等问题。
```python
import csv

with open('scores.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader) # 读取表头
    for row in reader:
        # row 是一个列表
        name = row[0]
        scores = [int(s) for s in row[1:]]
        # ... 后续处理
```

</details>

---

## 题目8：综合练习：单词频率统计 ⭐⭐⭐⭐

**题目**：读取一个文本文件 `article.txt`，统计其中每个单词出现的频率，并按频率降序打印前10个单词。

```python
# 任务：
# 1. 读取文件内容
# 2. 将文本转换为小写，并替换掉标点符号
# 3. 使用 split() 分割成单词列表
# 4. 使用字典统计每个单词的频率
# 5. 对字典按值进行降序排序
# 6. 打印前10个结果
```

<details>
<summary>✅ 答案</summary>

```python
import string

# 创建 article.txt 文件
article_text = """
Python is an interpreted, high-level and general-purpose programming language.
Python's design philosophy emphasizes code readability with its notable use of significant indentation.
Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.
Python is dynamically-typed and garbage-collected.
"""
with open('article.txt', 'w', encoding='utf-8') as f:
    f.write(article_text)

# 1. 读取文件
with open('article.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. 文本预处理
# 转为小写
text = text.lower()
# 替换标点符号为空格
for p in string.punctuation:
    text = text.replace(p, ' ')

# 3. 分割成单词
words = text.split()

# 4. 统计频率
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# 5. 按频率排序
# sorted() 返回一个元组列表 [('word', count), ...]
sorted_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

# 6. 打印前10个
print("--- 单词频率 Top 10 ---")
for i, (word, count) in enumerate(sorted_counts[:10], 1):
    print(f"{i}. '{word}': {count} 次")

# --- 单词频率 Top 10 ---
# 1. 'and': 4 次
# 2. 'python': 3 次
# 3. 'is': 2 次
# 4. 'code': 2 次
# 5. 'language': 2 次
# 6. 'an': 1 次
# ... (以此类推)
```

**知识点**：
- 文件读写
- 字符串处理 (`lower`, `replace`, `split`)
- 字典统计模式
- `sorted()` 函数与 `key=lambda`
- 列表切片 `[:10]`

**💡 使用 `collections.Counter` 简化**：
```python
from collections import Counter
import string

# ... (读取和预处理部分同上) ...
words = text.split()

# 使用 Counter 直接统计
word_counts = Counter(words)

# 获取最常见的10个
print("\n--- Counter 版本 Top 10 ---")
for i, (word, count) in enumerate(word_counts.most_common(10), 1):
    print(f"{i}. '{word}': {count} 次")
```

</details>

---

## 🎯 知识点总结

### 必须掌握
- ✅ `with open(...) as f:` 语法
- ✅ 文件模式：`'r'`, `'w'`, `'a'`
- ✅ `encoding='utf-8'`
- ✅ 读取方法：`read()`, `for line in f:`
- ✅ 写入方法：`write()`
- ✅ 字符串处理：`strip()`, `split()`

### 加分项
- `readline()` 和 `readlines()` 的区别
- `writelines()`
- 文件操作的异常处理 `try...except FileNotFoundError`
- `csv` 模块处理CSV文件
- `collections.Counter` 进行快速统计

---

## 📝 自我检测

完成以上题目后，问自己：
- [ ] 能否安全地打开、读取和写入文件？
- [ ] 理解 `'r'`, `'w'`, `'a'` 模式的区别吗？
- [ ] 知道为什么 `with` 语句是推荐的方式吗？
- [ ] 能否逐行处理一个大文件？
- [ ] 能否解析一个简单的文本文件（如CSV）并提取数据？

如果都能做到，恭喜你已经掌握了 Python 文件操作！🎉

**下一步**：[08_类与对象练习](08_oop_exercises.md)