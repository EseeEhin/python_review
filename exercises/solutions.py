# exercises/solutions.py
import os

# --- 题目 1：个人信息格式化输出 ---
def solve_q1():
    print("--- 解答 1：个人信息格式化输出 ---")
    # name = input("请输入你的名字: ")
    # age = int(input("请输入你的年龄: "))
    # city = input("请输入你的城市: ")
    # 模拟输入
    name, age, city = "Alice", 25, "上海"
    print(f"你好，我叫{name}，今年{age}岁，来自{city}。")
    print("-" * 20)

# --- 题目 2：字符串切片与方法 ---
def solve_q2():
    print("--- 解答 2：字符串切片与方法 ---")
    email = "user@example.com"
    
    # 方法 1: 使用 find 和切片
    at_pos = email.find('@')
    username = email[:at_pos]
    domain = email[at_pos + 1:]
    print(f"方法 1 -> 用户名: {username}, 域名: {domain}")

    # 方法 2: 使用 split
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    print(f"方法 2 -> 用户名: {username}, 域名: {domain}")
    print("-" * 20)

# --- 题目 3：列表操作与统计 ---
def solve_q3():
    print("--- 解答 3：列表操作与统计 ---")
    scores = [85, 92, 78, 65, 95, 88, 72, 95]
    print(f"原始分数: {scores}")
    
    highest = max(scores)
    lowest = min(scores)
    average = sum(scores) / len(scores)
    
    passing_count = 0
    for score in scores:
        if score >= 60:
            passing_count += 1
            
    print(f"最高分: {highest}, 最低分: {lowest}")
    print(f"平均分: {average:.2f}")
    print(f"及格人数: {passing_count}")
    
    # 删除低于 60 分的成绩
    # 注意：在遍历列表时删除元素是不安全的，推荐使用列表推导式创建新列表
    passing_scores = [score for score in scores if score >= 60]
    print(f"及格分数列表: {passing_scores}")
    print("-" * 20)

# --- 题目 4：字典与数据聚合 ---
def solve_q4():
    print("--- 解答 4：字典与数据聚合 ---")
    sales = [
        {"name": "Apple", "price": 5}, 
        {"name": "Banana", "price": 2}, 
        {"name": "Apple", "price": 5},
        {"name": "Orange", "price": 3},
        {"name": "Banana", "price": 2},
        {"name": "Apple", "price": 5},
    ]
    
    total_sales = {}
    for sale in sales:
        product_name = sale["name"]
        price = sale["price"]
        total_sales[product_name] = total_sales.get(product_name, 0) + price
        
    print(f"总销售额: {total_sales}")
    print("-" * 20)

# --- 题目 5：列表去重并保持顺序 ---
def solve_q5():
    print("--- 解答 5：列表去重并保持顺序 ---")
    items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    
    unique_ordered = []
    seen = set()
    for item in items:
        if item not in seen:
            unique_ordered.append(item)
            seen.add(item)
            
    print(f"原始列表: {items}")
    print(f"去重并保持顺序: {unique_ordered}")
    print("-" * 20)

# --- 题目 6：斐波那契数列 ---
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    while len(result) < n:
        next_fib = result[-1] + result[-2]
        result.append(next_fib)
    return result

def solve_q6():
    print("--- 解答 6：斐波那契数列 ---")
    print(f"fibonacci(10): {fibonacci(10)}")
    print("-" * 20)

# --- 题目 7：质数判断 ---
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve_q7():
    print("--- 解答 7：质数判断 ---")
    print(f"7 是质数吗? {is_prime(7)}")
    print(f"10 是质数吗? {is_prime(10)}")
    print(f"2 是质数吗? {is_prime(2)}")
    print("-" * 20)

# --- 题目 8：CSV 文件解析 ---
def solve_q8():
    print("--- 解答 8：CSV 文件解析 ---")
    csv_content = "Name,Age,City\nAlice,25,New York\nBob,30,London\nCharlie,22,Paris"
    with open("data.csv", "w") as f:
        f.write(csv_content)
        
    data_list = []
    with open("data.csv", "r") as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            row_dict = dict(zip(header, values))
            data_list.append(row_dict)
            
    print(data_list)
    os.remove("data.csv")
    print("-" * 20)

# --- 题目 9：批量重命名文件 ---
def solve_q9():
    print("--- 解答 9：批量重命名文件 ---")
    # 创建临时目录和文件
    if not os.path.exists("temp_files"):
        os.mkdir("temp_files")
    
    for i in range(1, 6):
        with open(os.path.join("temp_files", f"file{i}.txt"), "w") as f:
            f.write("dummy")
    print(f"创建了文件: {os.listdir('temp_files')}")
    
    # 重命名
    for filename in os.listdir("temp_files"):
        if filename.startswith("file") and filename.endswith(".txt"):
            num_str = filename[4:-4] # 提取数字部分
            new_name = f"report_{int(num_str):02d}.txt"
            os.rename(
                os.path.join("temp_files", filename),
                os.path.join("temp_files", new_name)
            )
    print(f"重命名后: {os.listdir('temp_files')}")
    
    # 清理
    for f in os.listdir("temp_files"):
        os.remove(os.path.join("temp_files", f))
    os.rmdir("temp_files")
    print("临时文件和目录已删除。")
    print("-" * 20)

# --- 题目 10：简易通讯录 ---
# 这个题目比较复杂，作为一个独立的脚本运行更合适
def solve_q10():
    print("--- 解答 10：简易通讯录 ---")
    print("这个解答比较复杂，请参考独立的 contact_book.py 脚本。")
    # 这里只提供核心逻辑
    contacts = {}
    filename = "contacts.txt"

    def load_contacts():
        if os.path.exists(filename):
            with open(filename, "r") as f:
                for line in f:
                    name, phone = line.strip().split(',')
                    contacts[name] = phone
    
    def save_contacts():
        with open(filename, "w") as f:
            for name, phone in contacts.items():
                f.write(f"{name},{phone}\n")

    # 模拟运行
    load_contacts()
    contacts["TestUser"] = "1234567890"
    save_contacts()
    print("通讯录已加载，添加了 TestUser 并已保存。")
    if os.path.exists(filename):
        os.remove(filename)
    print("-" * 20)


if __name__ == "__main__":
    solve_q1()
    solve_q2()
    solve_q3()
    solve_q4()
    solve_q5()
    solve_q6()
    solve_q7()
    solve_q8()
    solve_q9()
    solve_q10()