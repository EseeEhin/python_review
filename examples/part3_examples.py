# examples/part3_examples.py

# --- 1. 条件与循环 ---

print("--- 1.1 if-elif-else ---")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"分数 {score} 对应的等级是: {grade}")

print("\n--- 1.2 while 循环 ---")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()

print("\n--- 1.3 for 循环 ---")
# 遍历列表
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit, end=" ")
print()

# 使用 range()
for i in range(5):
    print(i, end=" ")
print()

# 使用 enumerate()
for i, fruit in enumerate(fruits):
    print(f"({i}, {fruit})", end=" ")
print()

# --- 2. 函数 (Function) ---

print("\n--- 2.1 函数定义与调用 ---")
def greet(name, message="Hello"):
    """一个简单的问候函数"""
    return f"{message}, {name}!"

print(greet("Alice"))
print(greet("Bob", message="Hi"))

print("\n--- 2.2 多返回值 ---")
def get_min_max(numbers):
    """返回列表中的最小值和最大值"""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 2, 8, 3])
print(f"列表 [1, 5, 2, 8, 3] 的最小值: {min_val}, 最大值: {max_val}")

print("\n--- 2.3 可变参数 ---")
def sum_all(*args):
    """计算所有参数的和"""
    total = 0
    for num in args:
        total += num
    return total

print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

print("\n--- 2.4 变量作用域 ---")
x = 10  # 全局变量

def print_x():
    print(f"函数内部访问全局变量 x: {x}")

def modify_global_x():
    global x
    x = 20
    print(f"函数内部修改全局变量 x 为: {x}")

print(f"原始全局变量 x: {x}")
print_x()
modify_global_x()
print(f"修改后的全局变量 x: {x}")

print("\n--- Part 3 Examples End ---")