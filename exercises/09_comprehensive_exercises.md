# 📝 09_综合练习

> **知识点**：全面考察数据结构、流程控制、函数、文件操作和面向对象编程的综合应用能力。

---

## 题目1：学生信息管理系统 (函数版) ⭐⭐⭐

**题目**：实现一个基于命令行的学生信息管理系统，支持增、删、改、查和显示所有学生信息。

**要求**：
- 使用一个**字典**来存储所有学生信息，其中键是学号（字符串），值是另一个包含姓名和年龄的字典。
- 将每个功能（添加、删除、修改、查询、显示）封装成独立的函数。
- 程序主循环持续运行，直到用户选择退出。

**示例数据结构**:
```python
students = {
    "S001": {"name": "张三", "age": 18},
    "S002": {"name": "李四", "age": 19}
}
```

<details>
<summary>✅ 答案</summary>

```python
# 学生信息存储
students = {}

def display_menu():
    """显示主菜单"""
    print("\n--- 学生信息管理系统 ---")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生")
    print("6. 退出系统")
    print("------------------------")

def add_student():
    """添加一个新学生"""
    student_id = input("请输入学号: ")
    if student_id in students:
        print(f"错误：学号 {student_id} 已存在！")
        return
    name = input("请输入姓名: ")
    try:
        age = int(input("请输入年龄: "))
        students[student_id] = {"name": name, "age": age}
        print(f"学生 {name} 添加成功！")
    except ValueError:
        print("错误：年龄必须是数字。")

def delete_student():
    """根据学号删除学生"""
    student_id = input("请输入要删除的学号: ")
    if student_id in students:
        removed_student = students.pop(student_id)
        print(f"学生 {removed_student['name']} 已被删除。")
    else:
        print(f"错误：未找到学号为 {student_id} 的学生。")

def modify_student():
    """修改学生信息"""
    student_id = input("请输入要修改的学号: ")
    if student_id in students:
        new_name = input(f"请输入新的姓名 (原: {students[student_id]['name']}): ")
        try:
            new_age = int(input(f"请输入新的年龄 (原: {students[student_id]['age']}): "))
            students[student_id]['name'] = new_name
            students[student_id]['age'] = new_age
            print("信息修改成功！")
        except ValueError:
            print("错误：年龄必须是数字。")
    else:
        print(f"错误：未找到学号为 {student_id} 的学生。")

def query_student():
    """查询单个学生信息"""
    student_id = input("请输入要查询的学号: ")
    student = students.get(student_id)
    if student:
        print(f"学号: {student_id}, 姓名: {student['name']}, 年龄: {student['age']}")
    else:
        print(f"错误：未找到学号为 {student_id} 的学生。")

def show_all_students():
    """显示所有学生信息"""
    if not students:
        print("当前没有学生信息。")
        return
    print("\n--- 所有学生信息 ---")
    for student_id, info in students.items():
        print(f"学号: {student_id}, 姓名: {info['name']}, 年龄: {info['age']}")
    print("----------------------")

def main():
    """主程序循环"""
    while True:
        display_menu()
        choice = input("请输入您的选择 (1-6): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            modify_student()
        elif choice == '4':
            query_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            print("感谢使用，系统已退出。")
            break
        else:
            print("无效的选择，请输入1到6之间的数字。")

# 运行主程序
if __name__ == "__main__":
    main()
```

**考察知识点**：
- 字典的增删改查
- 函数封装
- `while True` 无限循环与 `break`
- `if/elif/else` 流程控制
- `input()` 用户输入与 `print()` 输出
- `try...except` 异常处理

</details>

---

## 题目2：文件单词频率分析 (高级版) ⭐⭐⭐⭐

**题目**：读取一个文本文件，统计单词频率，并将结果（按频率降序）写入到另一个文件中。

**要求**：
1.  **读取文件**：读取名为 `input.txt` 的文件。
2.  **文本清洗**：将所有单词转为小写，并移除所有标点符号。
3.  **频率统计**：使用字典统计每个单词出现的次数。
4.  **排序**：将统计结果按单词出现的频率进行降序排序。
5.  **写入文件**：将排序后的结果写入到 `output.txt` 文件中，每行格式为 `单词: 次数`。
6.  将整个流程封装在一个函数中。

<details>
<summary>✅ 答案</summary>

```python
import string

def analyze_word_frequency(input_file, output_file):
    """
    读取输入文件，分析单词频率，并将结果写入输出文件。
    """
    try:
        # 1. 读取文件
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"错误: 输入文件 '{input_file}' 未找到。")
        return

    # 2. 文本清洗
    text = text.lower()
    # 创建一个翻译表，将所有标点符号映射为 None (即删除)
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # 3. 频率统计
    words = text.split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # 4. 排序
    # .items() 将字典转为 (key, value) 元组的列表
    # key=lambda item: item[1] 表示按元组的第二个元素（即频率）排序
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

    # 5. 写入文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("--- 单词频率统计结果 ---\n")
            for word, count in sorted_word_counts:
                f.write(f"{word}: {count}\n")
        print(f"分析完成，结果已写入 '{output_file}'。")
    except IOError:
        print(f"错误: 无法写入到文件 '{output_file}'。")


# --- 测试 ---
# 创建输入文件
input_text = """
Python is a great language. Python is versatile and easy to learn.
Learning Python opens up many opportunities.
"""
with open('input.txt', 'w', encoding='utf-8') as f:
    f.write(input_text)

# 执行分析
analyze_word_frequency('input.txt', 'output.txt')

# 查看输出文件内容
with open('output.txt', 'r', encoding='utf-8') as f:
    print("\n--- output.txt 内容 ---")
    print(f.read())

# --- output.txt 内容 ---
# --- 单词频率统计结果 ---
# python: 3
# is: 2
# a: 1
# great: 1
# language: 1
# versatile: 1
# and: 1
# easy: 1
# to: 1
# learn: 1
# learning: 1
# opens: 1
# up: 1
# many: 1
# opportunities: 1
```

**考察知识点**：
- 文件读写 (`with open`)
- 字符串处理 (`lower`, `translate`, `split`)
- 字典统计 (`get` 方法)
- `sorted()` 函数与 `key=lambda` 进行复杂排序
- 函数封装与异常处理

</details>

---

## 题目3：面向对象的购物车 ⭐⭐⭐⭐

**题目**：设计一个简单的电子商务购物车系统。

**要求**：
1.  **`Product` 类**：
    -   属性：`name` (商品名), `price` (价格)。
2.  **`ShoppingCart` 类**：
    -   属性：`items` (一个字典，存储商品和对应的数量，如 `{'苹果': 2}` )。
    -   方法：
        -   `add_item(product, quantity=1)`：添加商品到购物车。
        -   `remove_item(product, quantity=1)`：从购物车移除商品。
        -   `get_total_price()`：计算并返回购物车中所有商品的总价。
        -   `display_cart()`：打印购物车内容和总价。

<details>
<summary>✅ 答案</summary>

```python
class Product:
    """商品类"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        # 用于在容器中打印对象时提供清晰的表示
        return f"Product(name='{self.name}', price={self.price})"

class ShoppingCart:
    """购物车类"""
    def __init__(self):
        # items 字典: {商品名称: {'product': Product对象, 'quantity': 数量}}
        self.items = {}

    def add_item(self, product, quantity=1):
        """添加商品"""
        if not isinstance(product, Product) or quantity <= 0:
            print("错误：无效的商品或数量。")
            return
            
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}
        print(f"已添加 {quantity} 个 '{product.name}' 到购物车。")

    def remove_item(self, product_name, quantity=1):
        """移除商品"""
        if product_name not in self.items:
            print(f"错误：购物车中没有 '{product_name}'。")
            return

        if self.items[product_name]['quantity'] <= quantity:
            # 如果移除数量大于等于现有数量，则直接删除该商品
            del self.items[product_name]
            print(f"已从购物车中移除所有 '{product_name}'。")
        else:
            self.items[product_name]['quantity'] -= quantity
            print(f"已从购物车中移除 {quantity} 个 '{product_name}'。")

    def get_total_price(self):
        """计算总价"""
        total = 0
        for item_info in self.items.values():
            total += item_info['product'].price * item_info['quantity']
        return total

    def display_cart(self):
        """显示购物车内容"""
        print("\n--- 您的购物车 ---")
        if not self.items:
            print("购物车是空的。")
        else:
            for item_info in self.items.values():
                p = item_info['product']
                q = item_info['quantity']
                print(f"商品: {p.name}, 单价: {p.price:.2f}, 数量: {q}, 小计: {p.price * q:.2f}")
        
        print("--------------------")
        print(f"总价: {self.get_total_price():.2f}")
        print("--------------------")


# --- 测试 ---
# 创建商品
apple = Product("苹果", 5.5)
banana = Product("香蕉", 3.0)
python_book = Product("Python编程书", 89.9)

# 创建购物车
cart = ShoppingCart()

# 操作购物车
cart.add_item(apple, 5)
cart.add_item(banana, 10)
cart.add_item(python_book, 1)
cart.display_cart()

cart.remove_item("香蕉", 3)
cart.display_cart()

cart.remove_item("苹果", 10) # 移除所有苹果
cart.display_cart()
```

**考察知识点**：
- 类的定义与实例化
- `__init__` 和 `__repr__` 特殊方法
- 实例属性和实例方法
- 类之间的协作（`ShoppingCart` 使用 `Product` 对象）
- 字典作为核心数据结构
- 逻辑判断与边界条件处理

</details>

---

## 题目4：递归遍历文件夹 ⭐⭐⭐⭐

**题目**：编写一个函数，递归地遍历指定路径下的所有文件和文件夹，并打印出它们的层级结构。

**要求**：
- 使用 `os` 模块来处理文件和路径。
- 函数接收一个路径和当前的缩进级别作为参数。
- 对每个条目，判断是文件还是文件夹。
- 如果是文件夹，则递归调用自身，并增加缩进。

<details>
<summary>✅ 答案</summary>

```python
import os

def list_directory_tree(path, indent=''):
    """
    递归遍历并打印目录树。
    """
    if not os.path.isdir(path):
        print(f"错误: '{path}' 不是一个有效的目录。")
        return

    try:
        # os.listdir() 返回路径下所有文件和文件夹的名称列表
        items = os.listdir(path)
    except OSError as e:
        print(f"错误: 无法访问 '{path}'. 原因: {e}")
        return

    # 排序以保证输出顺序一致
    items.sort()
    
    for i, name in enumerate(items):
        # 构造完整的路径
        full_path = os.path.join(path, name)
        
        # 判断是最后一个条目，用于打印不同的连接线
        is_last = (i == len(items) - 1)
        
        # 打印连接线
        print(indent, end='')
        if is_last:
            print('└── ', end='')
            new_indent = indent + '    '
        else:
            print('├── ', end='')
            new_indent = indent + '│   '
            
        # 打印名称
        print(name)
        
        # 如果是文件夹，则递归调用
        if os.path.isdir(full_path):
            list_directory_tree(full_path, new_indent)

# --- 测试 ---
# 先创建一些测试用的目录和文件
if not os.path.exists('test_dir'):
    os.makedirs('test_dir/subdir1')
    os.makedirs('test_dir/subdir2')
    with open('test_dir/file1.txt', 'w') as f: f.write('a')
    with open('test_dir/subdir1/file2.txt', 'w') as f: f.write('b')
    with open('test_dir/subdir2/file3.txt', 'w') as f: f.write('c')

# 从 'test_dir' 开始遍历
print("目录树:")
list_directory_tree('test_dir')

# 目录树:
# ├── file1.txt
# ├── subdir1
# │   └── file2.txt
# └── subdir2
#     └── file3.txt
```

**考察知识点**：
- **递归函数**：函数调用自身来解决更小规模的子问题。
- **`os` 模块**：
    - `os.path.isdir(path)`：判断路径是否为文件夹。
    - `os.listdir(path)`：列出路径下的所有条目。
    - `os.path.join(path, name)`：安全地拼接路径。
- 字符串操作（用于打印层级结构）。
- 异常处理 (`try...except OSError`)。

</details>

---

## 🎯 最终挑战

如果你能独立完成以上所有题目，说明你已经具备了非常扎实的Python基础，并且能够综合运用所学知识解决实际问题。

**下一步建议**：
-   **深入标准库**：学习 `collections`, `datetime`, `json`, `re` 等常用模块。
-   **了解第三方库**：尝试使用如 `requests` (网络请求), `pandas` (数据分析), `Flask`/`Django` (Web开发) 等。
-   **参与项目**：将所学知识应用到实际的小项目中，这是最好的学习方式。

恭喜你完成了所有的练习！🎉