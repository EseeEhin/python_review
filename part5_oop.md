# 📝 第五部分：面向对象编程（60 分钟）⭐ **第6章重点**

> **目标**：掌握 Python 面向对象编程的核心概念，理解类、对象、继承和特殊方法

---

## 📋 本部分学习目标

完成本部分后，你将能够：
- ✅ 理解类和对象的概念
- ✅ 定义类并创建实例
- ✅ 使用构造函数和实例方法
- ✅ 理解类变量和实例变量的区别
- ✅ 掌握继承机制
- ✅ 使用特殊方法（魔术方法）
- ✅ 理解属性装饰器

---

## ⏱️ 时间分配

| 内容 | 时间 | 状态 |
|------|------|------|
| 类的定义与使用 | 20 分钟 | ⬜ |
| 继承机制 | 15 分钟 | ⬜ |
| 特殊方法与运算符重载 | 15 分钟 | ⬜ |
| 属性装饰器 | 10 分钟 | ⬜ |

---

## 1️⃣ 类的定义与使用（20 分钟）

### 1.1 什么是面向对象编程？

面向对象编程（OOP）是一种编程范式，它将数据和操作数据的方法组织在一起，形成"对象"。

**核心概念**：
- **类（Class）**：对象的蓝图或模板
- **对象（Object）**：类的实例
- **属性（Attribute）**：对象的数据
- **方法（Method）**：对象的行为

### 1.2 定义类

```python
class ClassName:
    """类的文档字符串"""
    
    # 类变量（所有实例共享）
    class_variable = "I am a class variable"
    
    # 构造函数（初始化方法）
    def __init__(self, param1, param2):
        """构造函数，创建对象时自动调用"""
        # 实例变量（每个实例独有）
        self.param1 = param1
        self.param2 = param2
    
    # 实例方法
    def instance_method(self):
        """实例方法，第一个参数必须是 self"""
        return f"param1: {self.param1}, param2: {self.param2}"
    
    # 类方法
    @classmethod
    def class_method(cls):
        """类方法，第一个参数是 cls（类本身）"""
        return f"Class variable: {cls.class_variable}"
    
    # 静态方法
    @staticmethod
    def static_method():
        """静态方法，不需要 self 或 cls"""
        return "I am a static method"
```

### 1.3 创建对象（实例化）

```python
# 创建对象
obj = ClassName("value1", "value2")

# 访问实例变量
print(obj.param1)  # value1

# 调用实例方法
print(obj.instance_method())

# 访问类变量
print(obj.class_variable)
print(ClassName.class_variable)

# 调用类方法
print(ClassName.class_method())

# 调用静态方法
print(ClassName.static_method())
```

### 1.4 `self` 参数详解

`self` 代表类的实例本身，通过它可以访问实例的属性和方法。

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # self.name 是实例变量
        self.age = age
    
    def greet(self):
        # 通过 self 访问实例变量
        return f"Hello, I'm {self.name}, {self.age} years old."

# 创建实例
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.greet())  # Hello, I'm Alice, 25 years old.
print(person2.greet())  # Hello, I'm Bob, 30 years old.
```

**重要**：
- `self` 必须是实例方法的第一个参数
- 调用方法时不需要传递 `self`，Python 会自动传递

### 1.5 类变量 vs 实例变量

```python
class Dog:
    # 类变量（所有实例共享）
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age

# 创建实例
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# 访问类变量
print(dog1.species)  # Canis familiaris
print(dog2.species)  # Canis familiaris

# 修改类变量（影响所有实例）
Dog.species = "Dog"
print(dog1.species)  # Dog
print(dog2.species)  # Dog

# 访问实例变量
print(dog1.name)  # Buddy
print(dog2.name)  # Max
```

**易错点**：
```python
class Counter:
    count = 0  # 类变量
    
    def __init__(self):
        Counter.count += 1  # 正确：修改类变量
        # self.count += 1   # 错误：会创建实例变量

c1 = Counter()
c2 = Counter()
print(Counter.count)  # 2
```

### 1.6 私有成员与公有成员

Python 使用命名约定来表示成员的访问级别：

```python
class MyClass:
    def __init__(self):
        self.public_var = "公有变量"
        self._protected_var = "保护变量（约定：内部使用）"
        self.__private_var = "私有变量（名称改编）"
    
    def public_method(self):
        return "公有方法"
    
    def _protected_method(self):
        return "保护方法"
    
    def __private_method(self):
        return "私有方法"

obj = MyClass()

# 公有成员可以直接访问
print(obj.public_var)
print(obj.public_method())

# 保护成员可以访问，但约定不应该在外部使用
print(obj._protected_var)

# 私有成员被名称改编，不能直接访问
# print(obj.__private_var)  # AttributeError

# 但可以通过改编后的名称访问（不推荐）
print(obj._MyClass__private_var)
```

**命名约定**：
- 无下划线：公有成员
- 单下划线 `_`：保护成员（约定内部使用）
- 双下划线 `__`：私有成员（名称改编）

---

## 2️⃣ 继承机制（15 分钟）

### 2.1 基本继承

```python
# 父类（基类）
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

# 子类（派生类）
class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类的构造函数
        super().__init__(name)
        self.breed = breed
    
    # 重写父类方法
    def speak(self):
        return f"{self.name} barks"

# 使用
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Buddy barks
print(dog.name)     # Buddy
print(dog.breed)    # Golden Retriever
```

### 2.2 `super()` 函数

`super()` 用于调用父类的方法：

```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello from {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        # 调用父类构造函数
        super().__init__(name)
        self.age = age
    
    def greet(self):
        # 调用父类方法并扩展
        parent_greeting = super().greet()
        return f"{parent_greeting}, I'm {self.age} years old"

child = Child("Alice", 10)
print(child.greet())  # Hello from Alice, I'm 10 years old
```

### 2.3 多重继承

Python 支持多重继承（一个类可以继承多个父类）：

```python
class Father:
    def skill_father(self):
        return "Father's skill"

class Mother:
    def skill_mother(self):
        return "Mother's skill"

class Child(Father, Mother):
    def skill_child(self):
        return "Child's skill"

child = Child()
print(child.skill_father())  # Father's skill
print(child.skill_mother())  # Mother's skill
print(child.skill_child())   # Child's skill
```

**方法解析顺序（MRO）**：
```python
print(Child.__mro__)
# (<class '__main__.Child'>, <class '__main__.Father'>, 
#  <class '__main__.Mother'>, <class 'object'>)
```

### 2.4 `isinstance()` 和 `issubclass()`

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# isinstance：检查对象是否是某个类的实例
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, str))     # False

# issubclass：检查一个类是否是另一个类的子类
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

---

## 3️⃣ 特殊方法与运算符重载（15 分钟）⭐ **重要**

特殊方法（也叫魔术方法）以双下划线开头和结尾，用于实现运算符重载和其他特殊行为。

### 3.1 常用特殊方法

| 方法 | 描述 | 触发操作 |
|:---|:---|:---|
| `__init__(self, ...)` | 构造函数 | `obj = MyClass()` |
| `__str__(self)` | 字符串表示（给用户看） | `print(obj)`, `str(obj)` |
| `__repr__(self)` | 字符串表示（给开发者看） | `obj` (在解释器中) |
| `__len__(self)` | 返回长度 | `len(obj)` |
| `__getitem__(self, key)` | 获取项 | `obj[key]` |
| `__setitem__(self, key, val)` | 设置项 | `obj[key] = val` |
| `__delitem__(self, key)` | 删除项 | `del obj[key]` |
| `__iter__(self)` | 返回迭代器 | `for item in obj` |
| `__contains__(self, item)` | 成员检查 | `item in obj` |

### 3.2 算术运算符重载

| 方法 | 运算符 | 示例 |
|:---|:---|:---|
| `__add__(self, other)` | `+` | `obj1 + obj2` |
| `__sub__(self, other)` | `-` | `obj1 - obj2` |
| `__mul__(self, other)` | `*` | `obj1 * obj2` |
| `__truediv__(self, other)` | `/` | `obj1 / obj2` |
| `__floordiv__(self, other)` | `//` | `obj1 // obj2` |
| `__mod__(self, other)` | `%` | `obj1 % obj2` |
| `__pow__(self, other)` | `**` | `obj1 ** obj2` |

### 3.3 比较运算符重载

| 方法 | 运算符 | 示例 |
|:---|:---|:---|
| `__eq__(self, other)` | `==` | `obj1 == obj2` |
| `__ne__(self, other)` | `!=` | `obj1 != obj2` |
| `__lt__(self, other)` | `<` | `obj1 < obj2` |
| `__le__(self, other)` | `<=` | `obj1 <= obj2` |
| `__gt__(self, other)` | `>` | `obj1 > obj2` |
| `__ge__(self, other)` | `>=` | `obj1 >= obj2` |

### 3.4 实战示例：自定义向量类

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """print(obj) 时调用"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """在解释器中直接输入 obj 时调用"""
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        """向量加法：v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """向量减法：v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """标量乘法：v * 3"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """相等比较：v1 == v2"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """len(v) 返回向量的模"""
        return int((self.x**2 + self.y**2)**0.5)

# 使用
v1 = Vector(2, 3)
v2 = Vector(1, 1)

print(v1)           # Vector(2, 3)
print(v1 + v2)      # Vector(3, 4)
print(v1 - v2)      # Vector(1, 2)
print(v1 * 2)       # Vector(4, 6)
print(v1 == v2)     # False
print(len(v1))      # 3
```

### 3.5 实战示例：自定义列表类

```python
class MyList:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        """len(obj)"""
        return len(self.data)
    
    def __getitem__(self, index):
        """obj[index]"""
        return self.data[index]
    
    def __setitem__(self, index, value):
        """obj[index] = value"""
        self.data[index] = value
    
    def __delitem__(self, index):
        """del obj[index]"""
        del self.data[index]
    
    def __contains__(self, item):
        """item in obj"""
        return item in self.data
    
    def __iter__(self):
        """for item in obj"""
        return iter(self.data)
    
    def append(self, item):
        self.data.append(item)
    
    def __str__(self):
        return str(self.data)

# 使用
my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)        # [1, 2, 3]
print(len(my_list))   # 3
print(my_list[1])     # 2
print(2 in my_list)   # True

for item in my_list:
    print(item)       # 1 2 3
```

---

## 4️⃣ 属性装饰器（10 分钟）

### 4.1 `@property` 装饰器

`@property` 可以将方法转换为属性，使其像访问属性一样调用方法。

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """获取半径"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """设置半径"""
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value
    
    @property
    def area(self):
        """计算面积（只读属性）"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """计算周长（只读属性）"""
        return 2 * 3.14159 * self._radius

# 使用
circle = Circle(5)

# 像访问属性一样使用
print(circle.radius)        # 5
print(circle.area)          # 78.53975
print(circle.circumference) # 31.4159

# 设置属性
circle.radius = 10
print(circle.area)          # 314.159

# 尝试设置只读属性会报错
# circle.area = 100  # AttributeError
```

### 4.2 为什么使用 `@property`？

**优点**：
1. **封装**：隐藏内部实现细节
2. **验证**：在设置值时进行验证
3. **计算属性**：动态计算值
4. **向后兼容**：可以将属性改为方法而不影响外部代码

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """摄氏度转华氏度"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """华氏度转摄氏度"""
        self._celsius = (value - 32) * 5/9

# 使用
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 25°C = 77.0°F

temp.fahrenheit = 100
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 37.77°C = 100.0°F
```

---

## 🎯 本部分小结

### ✅ 你已经掌握了

1. **类的定义与使用**
   - 类变量 vs 实例变量
   - `self` 参数
   - 构造函数 `__init__()`
   - 实例方法、类方法、静态方法

2. **继承**
   - 基本继承语法
   - `super()` 函数
   - 方法重写
   - 多重继承

3. **特殊方法**
   - `__str__()`, `__repr__()`
   - `__len__()`, `__getitem__()`, `__setitem__()`
   - 运算符重载：`__add__()`, `__eq__()` 等

4. **属性装饰器**
   - `@property`
   - `@property.setter`
   - 只读属性

---

## 📝 快速练习

### 练习 1：定义学生类

```python
# 任务：创建一个 Student 类
# 要求：
# 1. 有 name 和 score 属性
# 2. 有 get_grade() 方法，根据分数返回等级（A/B/C/D/F）
# 3. 实现 __str__() 方法

# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"Student(name={self.name}, score={self.score}, grade={self.get_grade()})"

# 测试
s = Student("Alice", 85)
print(s)  # Student(name=Alice, score=85, grade=B)
```
</details>

### 练习 2：实现矩形类

```python
# 任务：创建一个 Rectangle 类
# 要求：
# 1. 有 width 和 height 属性
# 2. 使用 @property 实现 area 和 perimeter 只读属性
# 3. 实现 __eq__() 方法比较两个矩形面积是否相等

# 你的代码：
```

<details>
<summary>点击查看答案</summary>

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __eq__(self, other):
        return self.area == other.area
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

# 测试
r1 = Rectangle(4, 5)
r2 = Rectangle(5, 4)
print(r1.area)       # 20
print(r1.perimeter)  # 18
print(r1 == r2)      # True
```
</details>

---

## ⏭️ 下一步

恭喜你完成第五部分！现在你已经掌握了 Python 面向对象编程的核心知识。

👉 **继续学习：[第七部分 - 文件操作与模块](part4_files_practice.md)**

---

## 📚 相关资源

- 📖 [考场速查手册](exam_handbook.txt)
- ⚠️ [常见错误与陷阱](common_mistakes.md)
- 💻 [代码示例](examples/)