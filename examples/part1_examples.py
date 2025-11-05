# examples/part1_examples.py

# --- 1. 核心差异 ---

print("--- 1.1 动态类型 ---")
age = 25
print(f"age 的值: {age}, 类型: {type(age)}")
age = "Bob"
print(f"age 的值: {age}, 类型: {type(age)}")
age = 19.99
print(f"age 的值: {age}, 类型: {type(age)}")

print("\n--- 1.2 代码块与缩进 ---")
x = 10
if x > 0:
    print("x 是正数")
    if x > 5:
        print("x 大于 5")
else:
    print("x 不是正数")

# --- 2. 基本数据类型与字符串 ---

print("\n--- 2.1 基本数据类型 ---")
my_int = 999999999999999999999999999999
my_float = 3.14159
my_bool = True
print(f"大整数: {my_int}, 类型: {type(my_int)}")
print(f"浮点数: {my_float}, 类型: {type(my_float)}")
print(f"布尔值: {my_bool}, 类型: {type(my_bool)}")

print("\n--- 2.2 字符串不可变性 ---")
name = "Alice"
# name[0] = 'B'  # 这会引发 TypeError
new_name = "B" + name[1:]
print(f"原字符串: {name}")
print(f"新字符串: {new_name}")

print("\n--- 2.3 字符串切片 ---")
s = "Hello, World!"
print(f"s[0:5]: {s[0:5]}")
print(f"s[7:]: {s[7:]}")
print(f"s[-6:]:{s[-6:]}")
print(f"s[::2]: {s[::2]}")
print(f"s[::-1]: {s[::-1]}")

print("\n--- 2.4 字符串常用方法 ---")
text = "  Python is Fun!  "
print(f"原文本: '{text}'")
print(f"upper(): {text.upper()}")
print(f"lower(): {text.lower()}")
print(f"strip(): '{text.strip()}'")
print(f"replace('Fun', 'Great'): {text.replace('Fun', 'Great')}")
print(f"split(' '): {text.split()}")

words = ["Python", "is", "Great"]
print(f"join(['Python', 'is', 'Great']): {'-'.join(words)}")

# --- 3. 基本输入输出 ---

print("\n--- 3.1 print() 函数 ---")
name = "Alice"
age = 25
# 使用 f-string
print(f"姓名: {name}, 年龄: {age}")
# 使用 sep 和 end 参数
print("apple", "banana", "orange", sep=", ", end="... done\n")

print("\n--- 3.2 input() 函数与类型转换 ---")
# 为了避免在自动运行中暂停，我们将 input() 注释掉
# user_name = input("请输入你的名字: ")
# user_age_str = input("请输入你的年龄: ")
# user_age = int(user_age_str)
# print(f"你好, {user_name}! 你明年就 {user_age + 1} 岁了。")

# 模拟输入
user_name = "Bob"
user_age_str = "30"
user_age = int(user_age_str)
print(f"你好, {user_name}! 你明年就 {user_age + 1} 岁了。")

print("\n--- Part 1 Examples End ---")