# examples/part2_examples.py

# --- 1. 列表 (List) ---

print("--- 1.1 创建列表 ---")
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
from_range = list(range(5))
zeros = [0] * 5
print(f"numbers: {numbers}")
print(f"mixed: {mixed}")
print(f"from_range: {from_range}")
print(f"zeros: {zeros}")

print("\n--- 1.2 列表访问与切片 ---")
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-1]: {fruits[-1]}")
print(f"fruits[1:4]: {fruits[1:4]}")
print(f"fruits[::-1]: {fruits[::-1]}")

print("\n--- 1.3 列表方法：添加与删除 ---")
my_list = ["a", "b", "c"]
print(f"原始列表: {my_list}")
my_list.append("d")
print(f"append('d'): {my_list}")
my_list.insert(1, "x")
print(f"insert(1, 'x'): {my_list}")
my_list.extend(["y", "z"])
print(f"extend(['y', 'z']): {my_list}")
popped_item = my_list.pop()
print(f"pop(): {popped_item}, 列表变为: {my_list}")
my_list.remove("b")
print(f"remove('b'): {my_list}")

print("\n--- 1.4 列表方法：排序与查找 ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原始数字列表: {numbers}")
print(f"numbers.count(1): {numbers.count(1)}")
print(f"numbers.index(4): {numbers.index(4)}")
numbers.sort()
print(f"numbers.sort(): {numbers}")
numbers.reverse()
print(f"numbers.reverse(): {numbers}")

print("\n--- 1.5 列表遍历 ---")
for i, fruit in enumerate(fruits):
    print(f"索引 {i}: {fruit}")

print("\n--- 1.6 列表嵌套 ---")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"matrix[1][1]: {matrix[1][1]}")

# --- 2. 字典 (Dictionary) ---

print("\n--- 2.1 创建字典 ---")
student = {"name": "Alice", "age": 20, "score": 95.5}
from_zip = dict(zip(["a", "b", "c"], [1, 2, 3]))
print(f"student: {student}")
print(f"from_zip: {from_zip}")

print("\n--- 2.2 字典访问与修改 ---")
print(f"student['name']: {student['name']}")
print(f"student.get('grade', 'N/A'): {student.get('grade', 'N/A')}")
student["age"] = 21
student["grade"] = "A"
print(f"修改后: {student}")

print("\n--- 2.3 字典方法 ---")
print(f"keys(): {student.keys()}")
print(f"values(): {student.values()}")
print(f"items(): {student.items()}")
age = student.pop("age")
print(f"pop('age'): {age}, 字典变为: {student}")

print("\n--- 2.4 字典遍历 ---")
for key, value in student.items():
    print(f"{key} -> {value}")

# --- 3. 元组 (Tuple) 与集合 (Set) ---

print("\n--- 3.1 元组 ---")
point = (10, 20)
print(f"point: {point}")
x, y = point  # 元组解包
print(f"x={x}, y={y}")
# point[0] = 5  # 这会引发 TypeError

print("\n--- 3.2 集合 ---")
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(numbers_list)
print(f"从列表创建集合 (去重): {unique_numbers}")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"set1 | set2 (并集): {set1 | set2}")
print(f"set1 & set2 (交集): {set1 & set2}")
print(f"set1 - set2 (差集): {set1 - set2}")

print("\n--- Part 2 Examples End ---")