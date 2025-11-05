# 🎯 Python 核心知识点速查手册

> **目标**：系统梳理所有核心知识点，避免遗漏和混淆

---

## 📋 目录

1. [基础语法](#1-基础语法)
2. [数据类型](#2-数据类型)
3. [运算符](#3-运算符)
4. [字符串操作](#4-字符串操作)
5. [列表 List](#5-列表-list)
6. [字典 Dictionary](#6-字典-dictionary)
7. [元组 Tuple](#7-元组-tuple)
8. [集合 Set](#8-集合-set)
9. [流程控制](#9-流程控制)
10. [函数](#10-函数)
11. [文件操作](#11-文件操作)
12. [面向对象](#12-面向对象)
13. [常见易混淆点](#13-常见易混淆点)

---

## 1. 基础语法

### 1.1 变量与赋值

```python
# 变量命名规则
name = "张三"          # 字母、数字、下划线，不能以数字开头
_age = 18             # 可以下划线开头
student_name = "李四"  # 推荐使用下划线命名法

# 多重赋值
a, b, c = 1, 2, 3
x = y = z = 0

# 交换变量
a, b = b, a  # Python特有，无需临时变量
```

### 1.2 注释

```python
# 单行注释

"""
多行注释
可以跨越多行
"""

'''
也可以用单引号
'''
```

### 1.3 缩进

```python
# Python 使用缩进表示代码块（通常4个空格）
if True:
    print("缩进4个空格")
    if True:
        print("嵌套缩进8个空格")
```

---

## 2. 数据类型

### 2.1 基本类型对比

| 类型 | 示例 | 可变性 | 说明 |
|------|------|--------|------|
| `int` | `42` | 不可变 | 整数，无大小限制 |
| `float` | `3.14` | 不可变 | 浮点数 |
| `bool` | `True`, `False` | 不可变 | 布尔值 |
| `str` | `"hello"` | 不可变 | 字符串 |
| `list` | `[1, 2, 3]` | 可变 | 列表 |
| `tuple` | `(1, 2, 3)` | 不可变 | 元组 |
| `dict` | `{"a": 1}` | 可变 | 字典 |
| `set` | `{1, 2, 3}` | 可变 | 集合 |

### 2.2 类型转换

```python
# 转整数
int("123")      # 123
int(3.14)       # 3
int(True)       # 1

# 转浮点数
float("3.14")   # 3.14
float(3)        # 3.0

# 转字符串
str(123)        # "123"
str([1, 2])     # "[1, 2]"

# 转布尔值
bool(0)         # False
bool("")        # False
bool([])        # False
bool(1)         # True
bool("hello")   # True
```

### 2.3 类型检查

```python
type(123)           # <class 'int'>
isinstance(123, int)  # True
```

---

## 3. 运算符

### 3.1 算术运算符

```python
+    # 加法：5 + 3 = 8
-    # 减法：5 - 3 = 2
*    # 乘法：5 * 3 = 15
/    # 除法：5 / 2 = 2.5（总是返回浮点数）
//   # 整除：5 // 2 = 2
%    # 取模：5 % 2 = 1
**   # 幂运算：2 ** 3 = 8
```

### 3.2 比较运算符

```python
==   # 等于
!=   # 不等于
>    # 大于
<    # 小于
>=   # 大于等于
<=   # 小于等于

# 链式比较（Python特有）
1 < x < 10  # 等价于 1 < x and x < 10
```

### 3.3 逻辑运算符

```python
and  # 与：True and False = False
or   # 或：True or False = True
not  # 非：not True = False

# 短路求值
x > 0 and y / x > 2  # 如果 x <= 0，不会计算 y / x
```

### 3.4 成员运算符

```python
in      # 在序列中：'a' in 'abc' = True
not in  # 不在序列中：'d' not in 'abc' = True
```

---

## 4. 字符串操作

### 4.1 字符串创建

```python
s1 = 'hello'
s2 = "world"
s3 = '''多行
字符串'''
s4 = """也可以
用双引号"""
```

### 4.2 字符串索引与切片

```python
s = "Python"

# 索引
s[0]     # 'P'（第一个字符）
s[-1]    # 'n'（最后一个字符）

# 切片 [start:stop:step]
s[0:3]   # 'Pyt'
s[:3]    # 'Pyt'（省略start）
s[3:]    # 'hon'（省略stop）
s[::-1]  # 'nohtyP'（反转）
s[::2]   # 'Pto'（每隔一个）
```

### 4.3 字符串方法（重要）

```python
# 大小写
s.upper()        # 转大写
s.lower()        # 转小写
s.capitalize()   # 首字母大写
s.title()        # 每个单词首字母大写

# 查找
s.find('th')     # 返回索引，找不到返回-1
s.index('th')    # 返回索引，找不到抛异常
s.count('o')     # 统计出现次数

# 判断
s.startswith('Py')  # 是否以...开头
s.endswith('on')    # 是否以...结尾
s.isdigit()         # 是否全是数字
s.isalpha()         # 是否全是字母

# 修改
s.replace('o', '0')  # 替换
s.strip()            # 去除两端空白
s.split(',')         # 分割成列表
','.join(['a', 'b']) # 列表合并成字符串
```

### 4.4 字符串格式化

```python
name = "张三"
age = 18

# 方法1：f-string（推荐，Python 3.6+）
f"我是{name}，{age}岁"
f"{age:3d}"      # 右对齐，宽度3
f"{3.14:.2f}"    # 保留2位小数

# 方法2：format()
"我是{}，{}岁".format(name, age)
"我是{0}，{1}岁".format(name, age)
"我是{name}，{age}岁".format(name=name, age=age)

# 方法3：% 格式化（旧式）
"我是%s，%d岁" % (name, age)
```

---

## 5. 列表 List

### 5.1 列表创建

```python
# 直接创建
lst = [1, 2, 3]
lst = []  # 空列表

# 使用 list()
lst = list(range(5))  # [0, 1, 2, 3, 4]

# 列表推导式
lst = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

### 5.2 列表索引与切片

```python
lst = [10, 20, 30, 40, 50]

# 索引
lst[0]      # 10
lst[-1]     # 50

# 切片
lst[1:3]    # [20, 30]
lst[:3]     # [10, 20, 30]
lst[::2]    # [10, 30, 50]
lst[::-1]   # [50, 40, 30, 20, 10]（反转）
```

### 5.3 列表方法（重要）

```python
lst = [1, 2, 3]

# 添加元素
lst.append(4)        # 末尾添加：[1, 2, 3, 4]
lst.insert(0, 0)     # 指定位置插入：[0, 1, 2, 3, 4]
lst.extend([5, 6])   # 批量添加：[0, 1, 2, 3, 4, 5, 6]

# 删除元素
lst.remove(2)        # 删除第一个值为2的元素
lst.pop()            # 删除并返回最后一个元素
lst.pop(0)           # 删除并返回索引0的元素
del lst[0]           # 删除索引0的元素
lst.clear()          # 清空列表

# 查找
lst.index(3)         # 返回值3的索引
lst.count(2)         # 统计值2出现的次数
3 in lst             # 判断3是否在列表中

# 排序
lst.sort()           # 原地升序排序
lst.sort(reverse=True)  # 原地降序排序
sorted(lst)          # 返回新的排序列表（不修改原列表）

# 反转
lst.reverse()        # 原地反转
lst[::-1]            # 返回新的反转列表
```

### 5.4 列表 vs 元组 vs 集合

| 特性 | 列表 `[]` | 元组 `()` | 集合 `{}` |
|------|----------|----------|----------|
| 可变性 | ✅ 可变 | ❌ 不可变 | ✅ 可变 |
| 有序性 | ✅ 有序 | ✅ 有序 | ❌ 无序 |
| 重复元素 | ✅ 允许 | ✅ 允许 | ❌ 不允许 |
| 索引访问 | ✅ 支持 | ✅ 支持 | ❌ 不支持 |

---

## 6. 字典 Dictionary

### 6.1 字典创建

```python
# 直接创建
d = {"name": "张三", "age": 18}
d = {}  # 空字典

# 使用 dict()
d = dict(name="张三", age=18)
d = dict([("name", "张三"), ("age", 18)])

# 字典推导式
d = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### 6.2 字典访问

```python
d = {"name": "张三", "age": 18}

# 访问
d["name"]           # "张三"（键不存在会报错）
d.get("name")       # "张三"（键不存在返回None）
d.get("city", "北京")  # "北京"（键不存在返回默认值）
```

### 6.3 字典方法（重要）

```python
d = {"name": "张三", "age": 18}

# 添加/修改
d["city"] = "北京"   # 添加新键值对
d["age"] = 19       # 修改已有键的值
d.update({"age": 20, "score": 90})  # 批量更新

# 删除
del d["age"]        # 删除键
d.pop("age")        # 删除并返回值
d.clear()           # 清空字典

# 查询
"name" in d         # 判断键是否存在
d.keys()            # 所有键
d.values()          # 所有值
d.items()           # 所有键值对

# 特殊方法
d.setdefault("hobby", "阅读")  # 获取值，不存在则设置默认值
```

### 6.4 字典遍历

```python
d = {"语文": 90, "数学": 85, "英语": 92}

# 遍历键
for key in d:
    print(key)

# 遍历值
for value in d.values():
    print(value)

# 遍历键值对
for key, value in d.items():
    print(f"{key}: {value}")
```

---

## 7. 元组 Tuple

### 7.1 元组特点

```python
# 不可变序列
t = (1, 2, 3)
t[0] = 10  # ❌ 错误：元组不可修改

# 单元素元组需要逗号
t = (1,)   # ✅ 正确
t = (1)    # ❌ 错误：这是整数1，不是元组
```

### 7.2 元组解包

```python
# 基本解包
a, b, c = (1, 2, 3)

# 交换变量
a, b = b, a

# * 收集剩余元素
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5

# 函数返回多个值
def get_info():
    return "张三", 18, 90

name, age, score = get_info()
```

---

## 8. 集合 Set

### 8.1 集合创建

```python
# 直接创建
s = {1, 2, 3}
s = set()  # 空集合（不能用{}，那是空字典）

# 从列表创建
s = set([1, 2, 2, 3])  # {1, 2, 3}（自动去重）
```

### 8.2 集合运算

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 交集（两个都有）
a & b           # {3, 4}
a.intersection(b)

# 并集（所有元素）
a | b           # {1, 2, 3, 4, 5, 6}
a.union(b)

# 差集（a有b没有）
a - b           # {1, 2}
a.difference(b)

# 对称差集（只在一个集合中）
a ^ b           # {1, 2, 5, 6}
a.symmetric_difference(b)
```

### 8.3 集合方法

```python
s = {1, 2, 3}

# 添加
s.add(4)        # 添加单个元素
s.update([5, 6])  # 添加多个元素

# 删除
s.remove(2)     # 删除元素（不存在会报错）
s.discard(2)    # 删除元素（不存在不报错）
s.pop()         # 随机删除并返回一个元素
```

---

## 9. 流程控制

### 9.1 条件判断

```python
# if-elif-else
if condition1:
    # 代码块1
elif condition2:
    # 代码块2
else:
    # 代码块3

# 三元表达式
result = value1 if condition else value2

# 链式比较
if 0 < x < 10:
    print("x在0到10之间")
```

### 9.2 for循环

```python
# 遍历序列
for item in [1, 2, 3]:
    print(item)

# 使用 range()
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# 使用 enumerate()（同时获取索引和值）
for i, item in enumerate(['a', 'b', 'c']):
    print(f"{i}: {item}")
# 0: a
# 1: b
# 2: c

# for-else（循环正常结束时执行else）
for i in range(5):
    if i == 10:
        break
else:
    print("循环正常结束")  # 会执行
```

### 9.3 while循环

```python
# 基本语法
while condition:
    # 代码块

# while-else
while condition:
    # 代码块
else:
    # 循环正常结束时执行

# 无限循环
while True:
    if condition:
        break
```

### 9.4 循环控制

```python
# break：跳出整个循环
for i in range(10):
    if i == 5:
        break  # 遇到5就停止
    print(i)  # 输出：0 1 2 3 4

# continue：跳过当前迭代
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)  # 输出：1 3 5 7 9

# pass：空语句（占位符）
for i in range(10):
    pass  # 什么都不做
```

### 9.5 列表推导式

```python
# 基本语法
[expression for item in iterable]

# 带条件
[expression for item in iterable if condition]

# 示例
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 嵌套
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

---

## 10. 函数

### 10.1 函数定义

```python
# 基本语法
def function_name(parameters):
    """文档字符串"""
    # 函数体
    return value

# 示例
def add(a, b):
    """计算两数之和"""
    return a + b

result = add(3, 5)  # 8
```

### 10.2 参数类型

```python
# 位置参数
def func(a, b):
    return a + b

func(1, 2)  # a=1, b=2

# 默认参数
def func(a, b=10):
    return a + b

func(5)     # a=5, b=10
func(5, 20) # a=5, b=20

# 关键字参数
def func(a, b):
    return a + b

func(a=1, b=2)  # 明确指定参数名
func(b=2, a=1)  # 顺序可以改变

# 可变参数 *args（元组）
def func(*args):
    print(args)  # 元组

func(1, 2, 3)  # (1, 2, 3)

# 可变关键字参数 **kwargs（字典）
def func(**kwargs):
    print(kwargs)  # 字典

func(a=1, b=2)  # {'a': 1, 'b': 2}

# 混合使用
def func(a, b=10, *args, **kwargs):
    pass

func(1, 2, 3, 4, x=5, y=6)
# a=1, b=2, args=(3,4), kwargs={'x':5, 'y':6}
```

### 10.3 返回值

```python
# 单个返回值
def func():
    return 42

# 多个返回值（实际返回元组）
def func():
    return 1, 2, 3

a, b, c = func()  # 元组解包

# 无返回值（返回None）
def func():
    print("hello")

result = func()  # None
```

### 10.4 Lambda表达式

```python
# 基本语法
lambda parameters: expression

# 示例
add = lambda a, b: a + b
print(add(3, 5))  # 8

# 常用于排序
students = [("张三", 85), ("李四", 92), ("王五", 78)]
students.sort(key=lambda x: x[1])  # 按分数排序
```

---

## 11. 文件操作

### 11.1 打开文件

```python
# 基本语法
file = open('filename.txt', 'mode', encoding='utf-8')

# 模式
'r'   # 只读（默认）
'w'   # 写入（覆盖）
'a'   # 追加
'r+'  # 读写
'b'   # 二进制模式（如 'rb', 'wb'）
```

### 11.2 读取文件

```python
# 方法1：read()（读取全部）
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 方法2：readline()（读取一行）
with open('file.txt', 'r', encoding='utf-8') as f:
    line = f.readline()

# 方法3：readlines()（读取所有行，返回列表）
with open('file.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 方法4：遍历文件对象（推荐）
with open('file.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

### 11.3 写入文件

```python
# 写入（覆盖）
with open('file.txt', 'w', encoding='utf-8') as f:
    f.write("Hello\n")
    f.write("World\n")

# 追加
with open('file.txt', 'a', encoding='utf-8') as f:
    f.write("New line\n")

# 写入多行
lines = ["line1\n", "line2\n", "line3\n"]
with open('file.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
```

### 11.4 with语句（推荐）

```python
# 自动关闭文件
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
# 文件自动关闭

# 等价于
f = open('file.txt', 'r', encoding='utf-8')
try:
    content = f.read()
finally:
    f.close()
```

---

## 12. 面向对象

### 12.1 类的定义

```python
class ClassName:
    """类的文档字符串"""
    
    # 类属性
    class_var = "类属性"
    
    # 构造方法
    def __init__(self, param1, param2):
        """初始化方法"""
        self.param1 = param1  # 实例属性
        self.param2 = param2
    
    # 实例方法
    def method(self):
        """实例方法"""
        return self.param1
    
    # 类方法
    @classmethod
    def class_method(cls):
        """类方法"""
        return cls.class_var
    
    # 静态方法
    @staticmethod
    def static_method():
        """静态方法"""
        return "静态方法"
```

### 12.2 创建对象

```python
# 创建实例
obj = ClassName("value1", "value2")

# 访问属性
print(obj.param1)

# 调用方法
result = obj.method()
```

### 12.3 继承

```python
# 单继承
class Parent:
    def __init__(self, name):
        self.name = name
    
    def method(self):
        print(f"Parent: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 调用父类构造方法
        self.age = age
    
    def method(self):
        super().method()  # 调用父类方法
        print(f"Child: {self.age}")

# 多继承
class Child(Parent1, Parent2):
    pass
```

### 12.4 特殊方法

```python
class MyClass:
    def __init__(self):
        """构造方法"""
        pass
    
    def __str__(self):
        """字符串表示（print时调用）"""
        return "MyClass instance"
    
    def __repr__(self):
        """官方字符串表示"""
        return "MyClass()"
    
    def __len__(self):
        """len()函数调用"""
        return 10
    
    def __getitem__(self, key):
        """索引访问 obj[key]"""
        return key
    
    def __setitem__(self, key, value):
        """索引赋值 obj[key] = value"""
        pass
    
    def __eq__(self, other):
        """相等比较 =="""
        return True
    
    def __lt__(self, other):
        """小于比较 <"""
        return False
```

---

## 13. 常见易混淆点

### 13.1 `==` vs `is`

```python
# == 比较值是否相等
# is 比较是否是同一个对象（内存地址）

a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b  # True（值相等）
a is b  # False（不是同一个对象）
a is c  # True（是同一个对象）
```

### 13.2 `append()` vs `extend()`

```python
lst = [1, 2, 3]

# append()：添加单个元素（整体添加）
lst.append([4, 5])
print(lst)  # [1, 2, 3, [4, 5]]

# extend()：添加多个元素（逐个添加）
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)  # [1, 2, 3, 4, 5]
```

### 13.3 `remove()` vs `pop()` vs `del`

```python
lst = [1, 2, 3, 2, 4]

# remove()：删除第一个匹配的值
lst.remove(2)  # [1, 3, 2, 4]

# pop()：删除并返回指定索引的元素
lst = [1, 2, 3, 2, 4]
value = lst.pop(1)  # value=2, lst=[1, 3, 2, 4]

# del：删除指定索引或切片
lst = [1, 2, 3, 2, 4]
del lst[1]  # [1, 3, 2, 4]
```

### 13.4 `sort()` vs `sorted()`

```python
lst = [3, 1, 4, 1, 5]

# sort()：原地排序（修改原列表，返回None）
lst.sort()
print(lst)  # [1, 1, 3, 4, 5]

# sorted()：返回新列表（不修改原列表）
lst = [3, 1, 4, 1, 5]
new_lst = sorted(lst)
print(lst)      # [3, 1, 4, 1, 5]（原列表不变）
print(new_lst)  # [1, 1, 3, 4, 5]
```

### 13.5 `break` vs `continue` vs `pass`

```python
# break：跳出整个循环
for i in range(5):
    if i == 3:
        break
    print(i)  # 0 1 2

# continue：跳过当前迭代
for i in range(5):
    if i == 3:
        continue
    print(i)  # 0 1 2 4

# pass：什么都不做（占位符）
for i in range(5):
    if i == 3:
        pass
    print(i)  # 0 1 2 3 4
```

### 13.6 可变对象 vs 不可变对象

```python
# 不可变对象：int, float, str, tuple
a = 10
b = a
a = 20
print(b)  # 10（b不受影响）

# 可变对象：