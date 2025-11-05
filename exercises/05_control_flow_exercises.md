# 📝 05_流程控制练习

> **知识点**：if/elif/else、for/while循环、break/continue、enumerate、range

---

## 题目1：条件判断基础 ⭐

**题目**：根据分数判断等级。

```python
# 任务：
# 输入一个分数（0-100），输出对应等级：
# 90-100: 优秀
# 80-89: 良好
# 70-79: 中等
# 60-69: 及格
# 0-59: 不及格
```

<details>
<summary>✅ 答案</summary>

```python
score = int(input("请输入分数："))

if score >= 90 and score <= 100:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 70:
    print("中等")
elif score >= 60:
    print("及格")
elif score >= 0:
    print("不及格")
else:
    print("分数无效")

# 或使用链式比较（更Pythonic）
if 90 <= score <= 100:
    print("优秀")
elif 80 <= score < 90:
    print("良好")
elif 70 <= score < 80:
    print("中等")
elif 60 <= score < 70:
    print("及格")
elif 0 <= score < 60:
    print("不及格")
else:
    print("分数无效")
```

**知识点**：
- `if-elif-else` 结构
- 链式比较：`a <= x <= b`
- 逻辑运算符：`and`, `or`, `not`

**⚠️ 常见错误**：
```python
# 错误：使用多个 if 而不是 elif
if score >= 90:
    print("优秀")
if score >= 80:  # 这会导致90分同时输出"优秀"和"良好"
    print("良好")

# 正确：使用 elif
if score >= 90:
    print("优秀")
elif score >= 80:  # 只有当 score < 90 时才会检查
    print("良好")
```
</details>

---

## 题目2：for循环遍历 ⭐

**题目**：使用for循环遍历不同类型的数据。

```python
# 任务：
# 1. 遍历列表并打印每个元素
# 2. 遍历字符串并打印每个字符
# 3. 遍历字典并打印键值对
# 4. 使用 range() 打印 1 到 10
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 遍历列表
fruits = ["apple", "banana", "orange"]
print("遍历列表：")
for fruit in fruits:
    print(fruit)

# 2. 遍历字符串
text = "Python"
print("\n遍历字符串：")
for char in text:
    print(char)

# 3. 遍历字典
scores = {"语文": 90, "数学": 85, "英语": 92}
print("\n遍历字典：")
for subject, score in scores.items():
    print(f"{subject}: {score}分")

# 4. 使用 range()
print("\n使用 range()：")
for i in range(1, 11):
    print(i, end=" ")
print()  # 换行
# 输出：1 2 3 4 5 6 7 8 9 10
```

**知识点**：
- `for item in iterable:` 语法
- `range(start, stop, step)` 函数
- `dict.items()` 遍历字典
- `end` 参数控制输出结尾

**💡 range() 用法**：
```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
range(10, 0, -1)# 10, 9, 8, ..., 1
```
</details>

---

## 题目3：while循环 ⭐⭐

**题目**：使用while循环实现不同功能。

```python
# 任务：
# 1. 计算 1 到 100 的和
# 2. 猜数字游戏（1-100，最多猜10次）
# 3. 输入验证（要求输入正数，否则重新输入）
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 计算 1 到 100 的和
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(f"1到100的和：{total}")  # 5050

# 2. 猜数字游戏
import random

target = random.randint(1, 100)
attempts = 0
max_attempts = 10

print("猜数字游戏（1-100）")
while attempts < max_attempts:
    guess = int(input(f"第{attempts + 1}次猜测："))
    attempts += 1
    
    if guess == target:
        print(f"恭喜你猜对了！用了{attempts}次")
        break
    elif guess < target:
        print("太小了")
    else:
        print("太大了")
else:
    print(f"游戏结束！答案是{target}")

# 3. 输入验证
while True:
    num = int(input("请输入一个正数："))
    if num > 0:
        print(f"你输入的正数是：{num}")
        break
    else:
        print("错误：必须输入正数，请重新输入")
```

**知识点**：
- `while condition:` 语法
- `break` 跳出循环
- `while-else` 结构
- 无限循环：`while True:`

**⚠️ 注意**：
```python
# 避免无限循环
i = 0
while i < 10:
    print(i)
    # 忘记 i += 1 会导致无限循环！
```
</details>

---

## 题目4：break和continue ⭐⭐

**题目**：使用break和continue控制循环。

```python
# 任务：
# 1. 找到第一个能被7整除的数（1-100）
# 2. 打印1-20中的所有奇数（跳过偶数）
# 3. 找出列表中第一个负数的位置
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 找到第一个能被7整除的数
print("第一个能被7整除的数：")
for i in range(1, 101):
    if i % 7 == 0:
        print(i)
        break  # 找到后立即退出
# 输出：7

# 2. 打印1-20中的所有奇数
print("\n1-20中的奇数：")
for i in range(1, 21):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
print()
# 输出：1 3 5 7 9 11 13 15 17 19

# 3. 找出列表中第一个负数的位置
numbers = [5, 3, 8, -2, 7, -5, 1]
print("\n查找第一个负数：")
for i, num in enumerate(numbers):
    if num < 0:
        print(f"第一个负数是 {num}，位置是 {i}")
        break
else:
    print("列表中没有负数")
# 输出：第一个负数是 -2，位置是 3
```

**知识点**：
- `break` 跳出整个循环
- `continue` 跳过当前迭代
- `enumerate()` 同时获取索引和值
- `for-else` 结构

**对比**：
```python
# break vs continue
for i in range(5):
    if i == 2:
        break  # 遇到2就停止，输出：0 1
    print(i)

for i in range(5):
    if i == 2:
        continue  # 跳过2，输出：0 1 3 4
    print(i)
```
</details>

---

## 题目5：enumerate()函数 ⭐⭐

**题目**：使用enumerate()同时获取索引和值。

```python
fruits = ["apple", "banana", "orange", "grape"]

# 任务：
# 1. 打印带编号的水果列表（从1开始）
# 2. 找出所有包含字母'a'的水果及其位置
# 3. 修改列表中索引为偶数的元素
```

<details>
<summary>✅ 答案</summary>

```python
fruits = ["apple", "banana", "orange", "grape"]

# 1. 打印带编号的水果列表
print("水果列表：")
for i, fruit in enumerate(fruits, 1):  # 从1开始编号
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. orange
# 4. grape

# 2. 找出所有包含字母'a'的水果
print("\n包含字母'a'的水果：")
for i, fruit in enumerate(fruits):
    if 'a' in fruit:
        print(f"索引{i}: {fruit}")
# 索引0: apple
# 索引1: banana
# 索引2: orange
# 索引3: grape

# 3. 修改列表中索引为偶数的元素
fruits = ["apple", "banana", "orange", "grape"]
for i, fruit in enumerate(fruits):
    if i % 2 == 0:
        fruits[i] = fruit.upper()
print(f"\n修改后：{fruits}")
# ['APPLE', 'banana', 'ORANGE', 'grape']
```

**知识点**：
- `enumerate(iterable, start=0)` 函数
- 同时获取索引和值
- `start` 参数指定起始编号

**💡 对比**：
```python
# 不使用 enumerate（不推荐）
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 使用 enumerate（推荐）
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```
</details>

---

## 题目6：嵌套循环 ⭐⭐⭐

**题目**：使用嵌套循环解决问题。

```python
# 任务：
# 1. 打印九九乘法表
# 2. 打印直角三角形（*号）
# 3. 找出两个列表的所有组合
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 打印九九乘法表
print("九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:2d}", end="  ")
    print()  # 换行

# 输出：
# 1×1= 1
# 1×2= 2  2×2= 4
# 1×3= 3  2×3= 6  3×3= 9
# ...

# 2. 打印直角三角形
print("\n直角三角形：")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# 输出：
# *
# **
# ***
# ****
# *****

# 3. 找出两个列表的所有组合
colors = ["红", "蓝"]
sizes = ["大", "中", "小"]

print("\n所有组合：")
for color in colors:
    for size in sizes:
        print(f"{color}{size}")

# 输出：
# 红大
# 红中
# 红小
# 蓝大
# 蓝中
# 蓝小
```

**知识点**：
- 嵌套循环
- 格式化输出：`{value:2d}`
- `end` 参数控制输出

**💡 扩展**：
```python
# 使用列表推导式生成组合
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)
# [('红', '大'), ('红', '中'), ('红', '小'), ('蓝', '大'), ('蓝', '中'), ('蓝', '小')]
```
</details>

---

## 题目7：循环中的else ⭐⭐⭐

**题目**：理解并使用循环的else子句。

```python
# 任务：
# 1. 判断一个数是否为质数
# 2. 在列表中查找元素（找到则break，找不到执行else）
# 3. 验证所有元素是否满足条件
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 判断质数
def is_prime(n):
    """判断n是否为质数"""
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # 找到因数，不是质数
    else:
        return True  # 循环正常结束，是质数

print("质数判断：")
for num in [2, 3, 4, 5, 15, 17]:
    print(f"{num}: {'是质数' if is_prime(num) else '不是质数'}")

# 2. 查找元素
numbers = [1, 3, 5, 7, 9]
target = 5

print(f"\n在列表中查找 {target}：")
for i, num in enumerate(numbers):
    if num == target:
        print(f"找到了！位置是 {i}")
        break
else:
    print("没找到")

# 3. 验证所有元素
numbers = [2, 4, 6, 8, 10]
print(f"\n验证是否所有数都是偶数：")
for num in numbers:
    if num % 2 != 0:
        print(f"发现奇数：{num}")
        break
else:
    print("所有数都是偶数")
```

**知识点**：
- `for-else` 和 `while-else`
- `else` 在循环正常结束时执行
- `break` 会跳过 `else` 块

**💡 理解 for-else**：
```python
# else 在循环正常结束时执行
for i in range(5):
    print(i)
else:
    print("循环正常结束")  # 会执行

# break 会跳过 else
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("循环正常结束")  # 不会执行
```
</details>

---

## 题目8：列表推导式与循环 ⭐⭐⭐

**题目**：将循环改写为列表推导式。

```python
# 任务：
# 1. 生成1-10的平方列表
# 2. 筛选出1-20中的偶数
# 3. 将字符串列表转换为大写
# 4. 生成九九乘法表（嵌套列表）
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 生成1-10的平方列表
# 普通循环
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)

# 列表推导式（推荐）
squares = [i ** 2 for i in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. 筛选出1-20中的偶数
# 普通循环
evens = []
for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)

# 列表推导式
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 3. 将字符串列表转换为大写
words = ["hello", "world", "python"]

# 普通循环
upper_words = []
for word in words:
    upper_words.append(word.upper())

# 列表推导式
upper_words = [word.upper() for word in words]
print(upper_words)
# ['HELLO', 'WORLD', 'PYTHON']

# 4. 生成九九乘法表
# 嵌套列表推导式
table = [[f"{j}×{i}={i*j}" for j in range(1, i+1)] for i in range(1, 10)]
for row in table:
    print("  ".join(row))
```

**知识点**：
- 列表推导式：`[expression for item in iterable]`
- 带条件：`[expression for item in iterable if condition]`
- 嵌套推导式

**性能对比**：
```python
import time

# 普通循环
start = time.time()
result = []
for i in range(1000000):
    result.append(i ** 2)
print(f"普通循环：{time.time() - start:.4f}秒")

# 列表推导式（更快）
start = time.time()
result = [i ** 2 for i in range(1000000)]
print(f"列表推导式：{time.time() - start:.4f}秒")
```
</details>

---

## 题目9：循环优化 ⭐⭐⭐

**题目**：优化循环性能。

```python
# 任务：
# 1. 提前终止循环（找到目标后立即退出）
# 2. 避免重复计算
# 3. 使用生成器表达式节省内存
```

<details>
<summary>✅ 答案</summary>

```python
# 1. 提前终止循环
# 不好的做法：遍历整个列表
numbers = list(range(1, 1000001))
target = 500000

found = False
for num in numbers:
    if num == target:
        found = True
print(f"找到了：{found}")

# 好的做法：找到后立即退出
for num in numbers:
    if num == target:
        print(f"找到了：{num}")
        break

# 2. 避免重复计算
# 不好的做法：每次都计算len()
fruits = ["apple", "banana", "orange"]
for i in range(len(fruits)):  # len()在每次迭代时都会被调用
    print(fruits[i])

# 好的做法：提前计算
n = len(fruits)
for i in range(n):
    print(fruits[i])

# 更好的做法：直接遍历
for fruit in fruits:
    print(fruit)

# 3. 使用生成器表达式节省内存
# 列表推导式（占用内存）
squares_list = [i ** 2 for i in range(1000000)]
print(f"列表大小：{squares_list.__sizeof__()} 字节")

# 生成器表达式（节省内存）
squares_gen = (i ** 2 for i in range(1000000))
print(f"生成器大小：{squares_gen.__sizeof__()} 字节")

# 使用生成器
total = sum(i ** 2 for i in range(1000000))
print(f"总和：{total}")
```

**知识点**：
- 提前终止循环
- 避免重复计算
- 生成器表达式：`(expression for item in iterable)`
- 内存优化

**💡 生成器 vs 列表**：
```python
# 列表推导式：一次性生成所有元素
squares_list = [i ** 2 for i in range(10)]
print(type(squares_list))  # <class 'list'>

# 生成器表达式：按需生成元素
squares_gen = (i ** 2 for i in range(10))
print(type(squares_gen))  # <class 'generator'>

# 遍历生成器
for square in squares_gen:
    print(square)
```
</details>

---

## 题目10：综合练习 ⭐⭐⭐⭐

**题目**：实现一个简单的菜单系统。

```python
# 要求：
# 1. 显示菜单选项
# 2. 根据用户输入执行不同操作
# 3. 输入验证
# 4. 循环直到用户选择退出
```

<details>
<summary>✅ 答案</summary>

```python
def show_menu():
    """显示菜单"""
    print("\n=== 学生管理系统 ===")
    print("1. 添加学生")
    print("2. 查看所有学生")
    print("3. 查找学生")
    print("4. 删除学生")
    print("5. 退出")
    print("=" * 20)

def add_student(students):
    """添加学生"""
    name = input("请输入学生姓名：")
    while True:
        try:
            age = int(input("请输入年龄："))
            if age > 0:
                break
            print("年龄必须大于0")
        except ValueError:
            print("请输入有效的数字")
    
    students[name] = age
    print(f"已添加：{name}（{age}岁）")

def show_all_students(students):
    """查看所有学生"""
    if not students:
        print("暂无学生记录")
        return
    
    print("\n所有学生：")
    for i, (name, age) in enumerate(students.items(), 1):
        print(f"{i}. {name}（{age}岁）")

def find_student(students):
    """查找学生"""
    name = input("请输入要查找的学生姓名：")
    if name in students:
        print(f"{name}（{students[name]}岁）")
    else:
        print(f"未找到学生：{name}")

def delete_student(students):
    """删除学生"""
    name = input("请输入要删除的学生姓名：")
    if name in students:
        age = students.pop(name)
        print(f"已删除：{name}（{age}岁）")
    else:
        print(f"未找到学生：{name}")

def main():
    """主程序"""
    students = {}
    
    while True:
        show_menu()
        
        try:
            choice = input("请选择操作（1-5）：")
            
            if choice == '1':
                add_student(students)
            elif choice == '2':
                show_all_students(students)
            elif choice == '3':
                find_student(students)
            elif choice == '4':
                delete_student(students)
            elif choice == '5':
                print("感谢使用，再见！")
                break
            else:
                print("无效的选择，请输入1-5")
        
        except KeyboardInterrupt:
            print("\n\n程序被中断")
            break
        except Exception as e:
            print(f"发生错误：{e}")

# 运行程序
if __name__ == "__main__":
    main()
```

**知识点**：
- 菜单驱动程序
- 函数封装
- 异常处理
- 输入验证
- 无限循环与退出

**💡 程序结构**：
```
1. 显示菜单
2. 获取用户输入
3. 验证输入
4. 执行对应操作
5. 返回步骤1（直到用户选择退出）
```
</details>

---

## 🎯 知识点总结

### 必须掌握
- ✅ 条件判断：`if-elif-else`
- ✅ for循环：`for item in iterable:`
- ✅ while循环：`while condition:`
- ✅ 循环控制：`break`, `continue`
- ✅ `range()` 函数
- ✅ `enumerate()` 函数

### 加分项
- 列表推导式
- 嵌套循环
- `for-else` 和 `while-else`
- 生成器表达式
- 循环优化技巧

---

## 📝 自我检测

完成以上题目后，问自己：
- [ ] 能否正确使用if-elif-else？
- [ ] 理解for和while的区别？
- [ ] 知道何时使用break和continue？
- [ ] 能否使用enumerate()？
- [ ] 理解for-else的执行逻辑？

如果都能做到，恭喜你已经掌握了Python流程控制！🎉

**下一步**：[06_函数练习](06_function_exercises.md)