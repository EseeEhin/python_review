# examples/part4_examples.py
import os

# --- 1. 文件输入输出 (File I/O) ---

# 创建一个用于读取的测试文件
with open("data.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

print("--- 1.1 读取文件 ---")
# 逐行遍历读取
print("逐行遍历读取:")
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# readlines() 读取所有行到列表
print("\nreadlines() 读取:")
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)

print("\n--- 1.2 写入文件 ---")
# 'w' 模式会覆盖文件
with open("output.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is a new line.\n")
print("'output.txt' 已被创建/覆盖。")

# 'a' 模式会追加内容
with open("output.txt", "a") as f:
    f.write("This line is appended.\n")
print("'output.txt' 已被追加内容。")

# --- 2. 列表推导式 (List Comprehension) ---

print("\n--- 2.1 基本列表推导式 ---")
squares = [x**2 for x in range(10)]
print(f"0-9的平方: {squares}")

print("\n--- 2.2 带条件的列表推导式 ---")
evens = [x for x in range(10) if x % 2 == 0]
print(f"0-9中的偶数: {evens}")

print("\n--- 2.3 字典和集合推导式 ---")
squares_dict = {x: x**2 for x in range(5)}
print(f"平方字典: {squares_dict}")

# --- 3. 模拟考试题练习 ---

print("\n--- 3.1 单词频率统计 ---")
# (代码来自 part4_files_practice.md)
import string

def word_count(filename):
    word_freq = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            for p in string.punctuation:
                text = text.replace(p, ' ')
            words = text.split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
        sorted_freq = sorted(word_freq.items(), key=lambda item: item[1], reverse=True)
        print(f"'{filename}' 中频率最高的单词:")
        for i, (word, freq) in enumerate(sorted_freq[:5], 1): # 只显示前5个
            print(f"{i}. '{word}': {freq} 次")
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到。")

with open("sample.txt", "w") as f:
    f.write("Python is a great language. I love Python. Python is easy to learn.")
word_count("sample.txt")


print("\n--- 3.2 计算平均值 ---")
# (代码来自 part4_files_practice.md)
def calculate_average(filename):
    numbers = []
    try:
        with open(filename, 'r+') as f:
            lines = f.readlines()
            for line in lines:
                try:
                    if not line.strip().startswith('-'): # 避免读取自己写入的分隔符
                        numbers.append(float(line.strip()))
                except ValueError:
                    pass # 忽略无法转换的行
            if not numbers: return
            total = sum(numbers)
            average = total / len(numbers)
            f.write("\n---\n")
            f.write(f"总和: {total:.2f}\n")
            f.write(f"平均值: {average:.2f}\n")
        print(f"计算完成，结果已写入 '{filename}'。")
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到。")

with open("numbers.txt", "w") as f:
    f.write("10.5\n20.0\n15.5\n30.0\n")
calculate_average("numbers.txt")


print("\n--- 3.3 筛选偶数 ---")
# (代码来自 part4_files_practice.md)
def filter_even_numbers_comprehension(input_list):
    return [num for num in input_list if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"列表 {numbers} 中的偶数: {filter_even_numbers_comprehension(numbers)}")


# 清理创建的临时文件
print("\n--- 清理临时文件 ---")
os.remove("data.txt")
os.remove("output.txt")
os.remove("sample.txt")
os.remove("numbers.txt")
print("临时文件已删除。")


print("\n--- Part 4 Examples End ---")