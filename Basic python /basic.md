# Python Basics — Step by Step Guide

A beginner-friendly, step-by-step reference for core Python concepts: **keywords**, **data types**, **types of operators**, and everyday syntax.

---

## Index (click to jump)

1. [What is Python?](#1-what-is-python)
2. [Comments](#2-comments)
3. [Variables](#3-variables)
4. [Python Keywords](#4-python-keywords)
5. [Data Types (Core)](#5-data-types-core)
   - [5.1 Numeric Types](#51-numeric-types)
   - [5.2 Text Type — str](#52-text-type--str)
   - [5.2.1 strip() method](#521-strip-method)
   - [5.2.2 Slicing](#522-slicing)
   - [5.2.3 endswith()](#523-endswith)
   - [5.2.4 capitalize()](#524-capitalize)
   - [5.2.5 replace()](#525-replace)
   - [5.2.6 find()](#526-find)
   - [5.2.7 count()](#527-count)
   - [5.3 Boolean Type](#53-boolean-type--bool)
   - [5.4 None Type](#54-none-type--nonetype)
   - [5.5 Sequence Types](#55-sequence-types)
   - [5.5.1 List (quick intro)](#list--list-mutable-ordered)
   - [5.6 Mapping Type — dict](#56-mapping-type--dict)
   - [5.7 Set Types](#57-set-types--set--frozenset)
   - [5.8 Data Type Summary](#58-data-type-summary)
6. [Type Conversion (Casting)](#6-type-conversion-casting)
   - [6.1 Implicit](#61-implicit-type-conversion)
   - [6.2 Explicit](#62-explicit-type-conversion-casting-functions)
   - [6.3 to int](#63-convert-to-int)
   - [6.4 to float](#64-convert-to-float)
   - [6.5 to str](#65-convert-to-str)
   - [6.6 to bool](#66-convert-to-bool)
   - [6.7 Collections](#67-convert-between-collections)
   - [6.8 input()](#68-convert-with-input-very-common)
   - [6.9 Common Mistakes](#69-common-mistakes)
   - [6.10 Quick Practice](#610-quick-practice)
7. [Types of Operators](#7-types-of-operators)
   - [7.1 Arithmetic](#71-arithmetic-operators)
   - [7.2 Comparison](#72-comparison-relational-operators)
   - [7.3 Logical](#73-logical-operators)
   - [7.4 Assignment](#74-assignment-operators)
   - [7.5 Bitwise](#75-bitwise-operators)
   - [7.6 Membership](#76-membership-operators)
   - [7.7 Identity](#77-identity-operators)
   - [7.8 Precedence](#78-operator-precedence-basic-order)
8. [Input and Output](#8-input-and-output)
9. [Conditions](#9-conditions-if--elif--else)
10. [Loops](#10-loops)
   - [10.1 for loop](#101-for-loop)
   - [10.2 while loop](#102-while-loop)
   - [10.3 break and continue](#103-break-and-continue)
   - [10.4 range()](#104-range)
   - [10.5 enumerate()](#105-enumerate)
   - [10.6 enumerate vs range](#106-enumerate-vs-range)
   - [10.7 Nested loops](#107-nested-loops)
11. [Functions](#11-functions)
   - [11.1 Basic function](#111-basic-function)
   - [11.2 Parameters & return](#112-parameters--return)
   - [11.3 Default & keyword args](#113-default--keyword-arguments)
   - [11.4 Lambda](#114-lambda-short-function)
   - [11.5 Recursion](#115-recursion-functions)
   - [11.6 Recursion examples](#116-recursion-examples)
   - [11.7 Recursion vs loop](#117-recursion-vs-loop)
12. [Lists in Python](#12-lists-in-python)
   - [12.1 Create a list](#121-create-a-list)
   - [12.2 Access items](#122-access-items-indexing)
   - [12.3 Change items](#123-change-items)
   - [12.4 Add items](#124-add-items)
   - [12.5 Remove items](#125-remove-items)
   - [12.6 Loop through a list](#126-loop-through-a-list)
   - [12.7 Check & length](#127-check-membership--length)
   - [12.8 Slicing lists](#128-slicing-lists)
   - [12.9 Sort & reverse](#129-sort--reverse)
   - [12.10 Copy a list](#1210-copy-a-list)
   - [12.11 Join lists](#1211-join-lists)
   - [12.12 Useful methods](#1212-useful-list-methods-summary)
   - [12.13 List vs Tuple](#1213-list-vs-tuple)
13. [Tuples in Python](#13-tuples-in-python)
   - [13.1 Create a tuple](#131-create-a-tuple)
   - [13.2 Access items](#132-access-items-indexing)
   - [13.3 Slicing tuples](#133-slicing-tuples)
   - [13.4 Immutable nature](#134-immutable-nature-cannot-change)
   - [13.5 Loop through a tuple](#135-loop-through-a-tuple)
   - [13.6 Check & length](#136-check-membership--length)
   - [13.7 Join tuples](#137-join-tuples)
   - [13.8 Useful methods](#138-useful-tuple-methods)
   - [13.9 Unpacking](#139-tuple-unpacking)
   - [13.10 Convert list ↔ tuple](#1310-convert-list--tuple)
   - [13.11 When to use tuple](#1311-when-to-use-a-tuple)
   - [13.12 Tuple vs List](#1312-tuple-vs-list)
14. [Dictionaries in Python](#14-dictionaries-in-python)
   - [14.1 Create a dictionary](#141-create-a-dictionary)
   - [14.2 Access items](#142-access-items)
   - [14.3 Add / update items](#143-add--update-items)
   - [14.4 Remove items](#144-remove-items)
   - [14.5 Loop through a dict](#145-loop-through-a-dictionary)
   - [14.6 Check & length](#146-check-keys--length)
   - [14.7 Nested dictionaries](#147-nested-dictionaries)
   - [14.8 Useful methods](#148-useful-dictionary-methods)
   - [14.9 Copy a dictionary](#149-copy-a-dictionary)
   - [14.10 Dict vs List](#1410-dict-vs-list)
   - [14.11 When to use](#1411-when-to-use-a-dictionary)
15. [Sets in Python](#15-sets-in-python)
   - [15.1 Create a set](#151-create-a-set)
   - [15.2 Add items](#152-add-items)
   - [15.3 Remove items](#153-remove-items)
   - [15.4 Loop through a set](#154-loop-through-a-set)
   - [15.5 Check & length](#155-check-membership--length)
   - [15.6 Set operations](#156-set-operations)
   - [15.7 Useful methods](#157-useful-set-methods)
   - [15.8 frozenset](#158-frozenset)
   - [15.9 Set vs List vs Dict](#159-set-vs-list-vs-dict)
   - [15.10 When to use](#1510-when-to-use-a-set)
16. [Errors and Exceptions](#16-errors-and-exceptions-basic)
17. [Modules](#17-modules-basic)
18. [Quick Practice Checklist](#18-quick-practice-checklist)
19. [Mini Examples](#19-mini-examples)
20. [Next Steps](#20-next-steps-after-basics)

---

## 1. What is Python?

Python is a high-level, interpreted programming language. It is known for:

- Simple, readable syntax
- Dynamic typing (you do not declare variable types)
- Being used for web, data, AI, scripting, and automation

**Run Python:**

```bash
python3
# or
python3 your_file.py
```

---

## 2. Comments

Comments explain code and are ignored by Python.

```python
# This is a single-line comment

"""
This is a
multi-line comment (docstring style)
"""
```

---

## 3. Variables

A variable stores a value. In Python you assign with `=`.

```python
name = "Amit"
age = 25
height = 5.9
is_student = True
```

**Rules for variable names:**

| Allowed | Not allowed |
|---------|-------------|
| `user_name`, `age2`, `_count` | `2age` (cannot start with number) |
| letters, digits, underscore | spaces or symbols like `@`, `-` |
| case-sensitive (`Age` ≠ `age`) | Python keywords as names |

---

## 4. Python Keywords

Keywords are reserved words. You **cannot** use them as variable names.

| Keyword | Meaning (simple) |
|---------|------------------|
| `False` | Boolean false value |
| `True` | Boolean true value |
| `None` | Represents “no value” |
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |
| `if` | Conditional check |
| `elif` | Else-if condition |
| `else` | Alternate block |
| `for` | Loop over a sequence |
| `while` | Loop while condition is true |
| `break` | Exit a loop early |
| `continue` | Skip to next loop iteration |
| `pass` | Do nothing (placeholder) |
| `def` | Define a function |
| `return` | Return a value from a function |
| `class` | Define a class |
| `import` | Import a module |
| `from` | Import specific parts |
| `as` | Alias for import / exception |
| `try` | Start error handling |
| `except` | Catch an error |
| `finally` | Always run after try/except |
| `raise` | Raise an exception |
| `with` | Context manager (e.g. files) |
| `lambda` | Small anonymous function |
| `global` | Use a global variable inside a function |
| `nonlocal` | Use a variable from outer (non-global) scope |
| `in` | Membership check / for-loop |
| `is` | Identity comparison |
| `del` | Delete object / reference |
| `assert` | Debugging check |
| `yield` | Produce value from a generator |
| `async` | Define async function |
| `await` | Wait for async result |

**Quick check in Python:**

```python
import keyword
print(keyword.kwlist)
```

---

## 5. Data Types (Core)

Every value in Python has a type. Check it with `type()`.

```python
print(type(10))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hi"))      # <class 'str'>
```

### 5.1 Numeric Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `10`, `-5`, `0` | Whole numbers |
| `float` | `3.14`, `-0.5` | Decimal numbers |
| `complex` | `2 + 3j` | Complex numbers |

```python
a = 10          # int
b = 3.5         # float
c = 2 + 3j      # complex

print(a + b)    # 13.5
print(c.real)   # 2.0
print(c.imag)   # 3.0
```

### 5.2 Text Type — `str`

Strings are sequences of characters, written in quotes.

```python
s1 = 'Hello'
s2 = "World"
s3 = """Multi
line
string"""

print(s1 + " " + s2)   # Hello World
print(len(s1))         # 5
print(s1[0])           # H
print(s1.upper())      # HELLO
print(s1.lower())      # hello
print("ell" in s1)     # True
```

**Useful string methods:**

| Method | Example | Result |
|--------|---------|--------|
| `.strip()` | `" hi ".strip()` | `"hi"` |
| `.endswith()` | `"file.txt".endswith(".txt")` | `True` |
| `.capitalize()` | `"hello".capitalize()` | `"Hello"` |
| `.replace()` | `"hi".replace("h", "H")` | `"Hi"` |
| `.find()` | `"hello".find("l")` | `2` |
| `.count()` | `"hello".count("l")` | `2` |
| `.split()` | `"a,b".split(",")` | `['a', 'b']` |
| `.join()` | `"-".join(["a", "b"])` | `"a-b"` |
| `.startswith()` | `"hello".startswith("he")` | `True` |

#### 5.2.1 `strip()` method

In Python, the `strip()` method removes unwanted characters (spaces, newlines, tabs, etc.) from the **beginning and end** of a string.

It does **not** remove spaces in the middle of the string.

##### 1. Basic example

```python
text = "   Hello World   "
clean = text.strip()

print(text)        # "   Hello World   "
print(clean)       # "Hello World"
print(len(text))   # 15
print(len(clean))  # 11
```

##### 2. Removes spaces, tabs, and newlines

```python
msg = "\n\t  Python  \n"
print(msg.strip())   # "Python"
```

##### 3. `lstrip()` and `rstrip()`

| Method | Removes from |
|--------|--------------|
| `strip()` | Both sides (left + right) |
| `lstrip()` | Left side only |
| `rstrip()` | Right side only |

```python
word = "  hello  "

print(word.strip())   # "hello"
print(word.lstrip())  # "hello  "
print(word.rstrip())  # "  hello"
```

##### 4. Remove custom characters

You can pass characters to remove (not only spaces).

```python
data = "***Hello***"
print(data.strip("*"))   # "Hello"

code = "---Python---"
print(code.strip("-"))   # "Python"

mixed = "xxHelloWorldxx"
print(mixed.strip("x"))  # "HelloWorld"
```

##### 5. Useful with `input()`

User input often has extra spaces. Clean it with `strip()`.

```python
name = input("Enter your name: ").strip()
print(f"Hello, {name}!")
```

##### 6. Important notes

- `strip()` returns a **new** string (original is not changed)
- Middle spaces stay: `"a   b".strip()` → `"a   b"`
- Empty result possible: `"   ".strip()` → `""`

```python
s = "  hi  "
print(s.strip())   # "hi"
print(s)           # "  hi  "  (original unchanged)
```

#### 5.2.2 Slicing

Slicing means taking a **part** of a sequence (string, list, or tuple) using indexes.

**Syntax:**

```text
sequence[start : stop : step]
```

| Part | Meaning |
|------|---------|
| `start` | Where to begin (included). Default = `0` |
| `stop` | Where to end (excluded). Default = end |
| `step` | Jump size. Default = `1` |

Index reminder for `"PYTHON"`:

```text
Letter:  P  Y  T  H  O  N
Index:   0  1  2  3  4  5
Neg:    -6 -5 -4 -3 -2 -1
```

##### 1. Basic example

```python
text = "PYTHON"

print(text[0:2])   # "PY"   (index 0 and 1)
print(text[2:5])   # "THO"  (index 2, 3, 4)
print(text[1:4])   # "YTH"
```

Remember: **stop index is not included**.

##### 2. Skip start or stop

```python
text = "PYTHON"

print(text[:3])    # "PYT"   (from start to index 2)
print(text[2:])    # "THON"  (from index 2 to end)
print(text[:])     # "PYTHON" (full copy)
```

##### 3. Using step

```python
text = "PYTHON"

print(text[::2])   # "PTO"   (every 2nd character)
print(text[1::2])  # "YHN"
print(text[0:5:2]) # "PTO"
```

##### 4. Negative indexes

```python
text = "PYTHON"

print(text[-1])      # "N"     (last character)
print(text[-3:])     # "HON"   (last 3 characters)
print(text[:-1])     # "PYTHO" (all except last)
print(text[-4:-1])   # "THO"
```

##### 5. Reverse a string / list

```python
text = "PYTHON"
print(text[::-1])    # "NOHTYP"

nums = [1, 2, 3, 4]
print(nums[::-1])    # [4, 3, 2, 1]
```

##### 6. Slicing on lists and tuples

```python
fruits = ["apple", "banana", "mango", "orange", "grape"]

print(fruits[1:4])    # ['banana', 'mango', 'orange']
print(fruits[:2])     # ['apple', 'banana']
print(fruits[::2])    # ['apple', 'mango', 'grape']

point = (10, 20, 30, 40)
print(point[1:3])     # (20, 30)
```

##### 7. Important notes

- Slicing returns a **new** object (original stays same)
- Out-of-range indexes do **not** crash with slicing (unlike single index)

```python
text = "PYTHON"
print(text[2:100])   # "THON"  (safe)
# print(text[100])   # IndexError (single index can crash)
```

#### 5.2.3 `endswith()`

Checks if a string **ends with** a given value. Returns `True` or `False`.

##### 1. Basic example

```python
file_name = "report.pdf"

print(file_name.endswith(".pdf"))  # True
print(file_name.endswith(".txt"))  # False
```

##### 2. Check multiple endings (tuple)

```python
file_name = "photo.jpg"

print(file_name.endswith((".jpg", ".png", ".gif")))  # True
```

##### 3. Related: `startswith()`

```python
text = "Hello World"
print(text.startswith("Hello"))  # True
print(text.startswith("World"))  # False
```

---

#### 5.2.4 `capitalize()`

Makes the **first character uppercase** and the rest lowercase.

##### 1. Basic example

```python
text = "hello world"
print(text.capitalize())  # "Hello world"
```

##### 2. More examples

```python
print("PYTHON".capitalize())     # "Python"
print("pYTHON code".capitalize()) # "Python code"
print("123abc".capitalize())     # "123abc" (first char is digit)
```

##### 3. Related methods

| Method | What it does | Example | Result |
|--------|--------------|---------|--------|
| `capitalize()` | First letter upper, rest lower | `"hELLO".capitalize()` | `"Hello"` |
| `title()` | First letter of each word upper | `"hello world".title()` | `"Hello World"` |
| `upper()` | All letters upper | `"hello".upper()` | `"HELLO"` |
| `lower()` | All letters lower | `"HELLO".lower()` | `"hello"` |

```python
name = "aMiT kUmAr"
print(name.capitalize())  # "Amit kumar"
print(name.title())       # "Amit Kumar"
print(name.upper())       # "AMIT KUMAR"
print(name.lower())       # "amit kumar"
```

---

#### 5.2.5 `replace()`

Replaces a part of the string with another value.

**Syntax:** `string.replace(old, new, count)`

| Part | Meaning |
|------|---------|
| `old` | Text to find |
| `new` | Text to put instead |
| `count` | Optional — how many times to replace |

##### 1. Basic example

```python
text = "I like Java"
new_text = text.replace("Java", "Python")

print(new_text)  # "I like Python"
print(text)      # "I like Java" (original unchanged)
```

##### 2. Replace all occurrences

```python
msg = "ha ha ha"
print(msg.replace("ha", "hey"))  # "hey hey hey"
```

##### 3. Replace only limited times

```python
msg = "ha ha ha"
print(msg.replace("ha", "hey", 1))  # "hey ha ha"
print(msg.replace("ha", "hey", 2))  # "hey hey ha"
```

##### 4. Remove text using replace

```python
phone = "98-76-54-32-10"
print(phone.replace("-", ""))  # "9876543210"
```

---

#### 5.2.6 `find()`

Finds the **first index** of a value inside a string.

- If found → returns index (starting from `0`)
- If not found → returns `-1`

##### 1. Basic example

```python
text = "hello world"

print(text.find("h"))      # 0
print(text.find("world"))  # 6
print(text.find("o"))      # 4  (first "o" only)
print(text.find("z"))      # -1 (not found)
```

##### 2. Search in a range

```python
text = "hello world"

print(text.find("o", 5))      # 7  (start searching from index 5)
print(text.find("o", 5, 8))   # 7  (search between 5 and 8)
print(text.find("o", 8))      # -1
```

##### 3. `find()` vs `index()`

| Method | If not found |
|--------|--------------|
| `find()` | Returns `-1` (safe) |
| `index()` | Raises `ValueError` (error) |

```python
text = "python"
print(text.find("x"))   # -1
# print(text.index("x"))  # ValueError
```

---

#### 5.2.7 `count()`

Counts how many times a value appears in a string.

##### 1. Basic example

```python
text = "hello world"

print(text.count("l"))     # 3
print(text.count("o"))     # 2
print(text.count("world")) # 1
print(text.count("z"))     # 0
```

##### 2. Count in a range

```python
text = "banana"

print(text.count("a"))        # 3
print(text.count("a", 2))     # 2  (from index 2 to end)
print(text.count("a", 2, 4))  # 1  (index 2 to 3)
```

##### 3. Useful example

```python
sentence = "Python is easy. Python is powerful."
print(sentence.count("Python"))  # 2

password = "Aaa123"
print(password.count("A") + password.count("a"))  # 3
```

---

**f-strings (formatting):**

```python
name = "Amit"
age = 25
print(f"My name is {name} and I am {age}")
```

### 5.3 Boolean Type — `bool`

Only two values: `True` and `False`.

```python
is_active = True
is_done = False

print(10 > 5)     # True
print(10 == 5)    # False
print(bool(0))    # False
print(bool(1))    # True
print(bool(""))   # False (empty string)
print(bool("hi")) # True
```

**Falsy values in Python:** `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`

### 5.4 None Type — `NoneType`

`None` means “no value” / “empty”.

```python
result = None
print(result is None)  # True
```

### 5.5 Sequence Types

#### List — `list` (mutable, ordered)

A list stores multiple items in one variable. Lists are **ordered** and **changeable** (mutable).

```python
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits[0] = "grape"
print(fruits)       # ['grape', 'banana', 'mango', 'orange']
print(len(fruits))  # 4
```

→ Full details: [12. Lists in Python](#12-lists-in-python)

#### Tuple — `tuple` (immutable, ordered)

A tuple stores multiple items like a list, but **cannot be changed** after creation.

```python
point = (10, 20)
# point[0] = 5  # Error! tuples cannot be changed
print(point[1])  # 20
```

→ Full details: [13. Tuples in Python](#13-tuples-in-python)

#### Range — `range`

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1 to 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)
```

### 5.6 Mapping Type — `dict`

A dictionary stores data as **key–value pairs**. Keys must be unique and hashable.

```python
person = {
    "name": "Amit",
    "age": 25,
    "city": "Delhi"
}

print(person["name"])       # Amit
person["age"] = 26          # update
person["email"] = "a@x.com" # add
print(person.keys())
print(person.values())
```

→ Full details: [14. Dictionaries in Python](#14-dictionaries-in-python)

### 5.7 Set Types — `set` / `frozenset`

An unordered collection of **unique** items. Duplicates are removed automatically.

```python
nums = {1, 2, 2, 3, 3}
print(nums)  # {1, 2, 3}

nums.add(4)
nums.remove(1)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # union {1, 2, 3, 4, 5}
print(a & b)  # intersection {3}
print(a - b)  # difference {1, 2}
```

`frozenset` is an immutable set.

→ Full details: [15. Sets in Python](#15-sets-in-python)

### 5.8 Data Type Summary

| Category | Type | Mutable? | Example |
|----------|------|----------|---------|
| Numeric | `int`, `float`, `complex` | No | `10`, `3.14`, `1+2j` |
| Text | `str` | No | `"hello"` |
| Boolean | `bool` | No | `True` |
| Sequence | `list` | Yes | `[1, 2]` |
| Sequence | `tuple` | No | `(1, 2)` |
| Sequence | `range` | No | `range(5)` |
| Mapping | `dict` | Yes | `{"a": 1}` |
| Set | `set` | Yes | `{1, 2}` |
| Set | `frozenset` | No | `frozenset([1, 2])` |
| Null | `NoneType` | No | `None` |

---

## 6. Type Conversion (Casting)

Type conversion means changing a value from one data type to another.

There are **two kinds**:

| Kind | Who does it? | Example |
|------|--------------|---------|
| Implicit (automatic) | Python | `3 + 2.5` → `5.5` (int becomes float) |
| Explicit (manual / casting) | You, using functions | `int("10")` → `10` |

---

### 6.1 Implicit Type Conversion

Python automatically converts a smaller type to a larger type when needed.

```python
a = 5        # int
b = 2.5      # float
c = a + b    # Python converts 5 → 5.0

print(c)         # 5.5
print(type(c))   # <class 'float'>
```

**Rule:** `int` + `float` → result is `float`

---

### 6.2 Explicit Type Conversion (Casting Functions)

You convert types yourself using built-in functions.

| Function | Converts to | Example | Result |
|----------|-------------|---------|--------|
| `int()` | Integer | `int(3.9)` | `3` |
| `float()` | Float | `float(5)` | `5.0` |
| `str()` | String | `str(100)` | `"100"` |
| `bool()` | Boolean | `bool(1)` | `True` |
| `list()` | List | `list("hi")` | `['h', 'i']` |
| `tuple()` | Tuple | `tuple([1, 2])` | `(1, 2)` |
| `set()` | Set | `set([1, 1, 2])` | `{1, 2}` |
| `dict()` | Dictionary | `dict([("a", 1)])` | `{"a": 1}` |
| `complex()` | Complex | `complex(2, 3)` | `(2+3j)` |

---

### 6.3 Convert to `int`

```python
print(int(3.9))      # 3   (decimal part removed, not rounded)
print(int("25"))     # 25
print(int(True))     # 1
print(int(False))    # 0

# int("3.5")         # Error! cannot convert float-string directly
print(int(float("3.5")))  # 3  (correct way)
```

---

### 6.4 Convert to `float`

```python
print(float(10))       # 10.0
print(float("3.14"))   # 3.14
print(float("10"))     # 10.0
print(float(True))     # 1.0
```

---

### 6.5 Convert to `str`

```python
age = 25
print("I am " + str(age) + " years old")

print(str(3.14))     # "3.14"
print(str(True))     # "True"
print(str([1, 2]))   # "[1, 2]"
```

Useful when joining text with numbers.

---

### 6.6 Convert to `bool`

```python
print(bool(1))       # True
print(bool(0))       # False
print(bool(-5))      # True  (any non-zero number)
print(bool(""))      # False (empty string)
print(bool("hi"))    # True
print(bool([]))      # False (empty list)
print(bool([1]))     # True
print(bool(None))    # False
```

**Falsy values** → become `False`:  
`0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`, `None`

Everything else → `True`

---

### 6.7 Convert Between Collections

```python
# string → list / tuple / seť
print(list("ABC"))       # ['A', 'B', 'C']
print(tuple("ABC"))      # ('A', 'B', 'C')
print(set("AABC"))       # {'A', 'B', 'C'}  (duplicates removed)

# list ↔ tuple ↔ set
nums = [1, 2, 2, 3]
print(tuple(nums))       # (1, 2, 2, 3)
print(set(nums))         # {1, 2, 3}
print(list({1, 2, 3}))    # [1, 2, 3]  (order not guaranteed)

# list of pairs → dict
pairs = [("name", "Amit"), ("age", 25)]
print(dict(pairs))       # {'name': 'Amit', 'age': 25}
```

---

### 6.8 Convert with `input()` (Very Common)

`input()` **always returns a string**. Convert it when you need a number.

```python
age = int(input("Enter age: "))
price = float(input("Enter price: "))
name = str(input("Enter name: "))  # already a string, optional

print(type(age))    # <class 'int'>
print(type(price))  # <class 'float'>
```

---

### 6.9 Common Mistakes

```python
# 1) Wrong: adding number to string without conversion
# print("Age: " + 25)        # TypeError
print("Age: " + str(25))     # Correct

# 2) Wrong: converting invalid text to int
# int("hello")               # ValueError
# int("12.5")                # ValueError
print(int(float("12.5")))    # Correct → 12

# 3) Wrong: thinking int() rounds
print(int(3.9))              # 3 (truncates, does not round)
print(round(3.9))            # 4 (use round if needed)
```

---

### 6.10 Quick Practice

```python
# Convert and print type of each result
a = int("100")
b = float(50)
c = str(99)
d = bool("Python")
e = list("Hi")
f = set([1, 1, 2, 3])

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
```

---

## 7. Types of Operators

Operators are symbols that perform operations on values (operands).

### Overview — 7 Types of Operators in Python

| # | Type | Used for | Examples |
|---|------|----------|----------|
| 1 | Arithmetic | Math calculations | `+` `-` `*` `/` `//` `%` `**` |
| 2 | Comparison (Relational) | Compare two values | `==` `!=` `>` `<` `>=` `<=` |
| 3 | Logical | Combine conditions | `and` `or` `not` |
| 4 | Assignment | Store / update values | `=` `+=` `-=` `*=` `/=` |
| 5 | Bitwise | Work on binary bits | `&` `\|` `^` `~` `<<` `>>` |
| 6 | Membership | Check if value exists | `in` `not in` |
| 7 | Identity | Check same object in memory | `is` `is not` |

---

### 7.1 Arithmetic Operators

Used for mathematical operations.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division (float) | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Exponent (power) | `5 ** 2` | `25` |

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

### 7.2 Comparison (Relational) Operators

Compare two values and return `True` or `False`.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `5 <= 3` | `False` |

```python
x = 10
y = 20
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x >= 10) # True
```

---

### 7.3 Logical Operators

Used to combine multiple conditions.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `and` | True if **both** are true | `True and False` | `False` |
| `or` | True if **at least one** is true | `True or False` | `True` |
| `not` | Reverse the result | `not True` | `False` |

```python
age = 20
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False
```

---

### 7.4 Assignment Operators

Used to assign and update values in variables.

| Operator | Meaning | Same as |
|----------|---------|---------|
| `=` | Assign | `x = 5` |
| `+=` | Add and assign | `x = x + 5` |
| `-=` | Subtract and assign | `x = x - 5` |
| `*=` | Multiply and assign | `x = x * 5` |
| `/=` | Divide and assign | `x = x / 5` |
| `//=` | Floor divide and assign | `x = x // 5` |
| `%=` | Modulus and assign | `x = x % 5` |
| `**=` | Power and assign | `x = x ** 5` |

```python
x = 10
x += 5   # 15
x -= 2   # 13
x *= 2   # 26
x /= 2   # 13.0
x //= 2  # 6.0
x %= 4   # 2.0
x **= 3  # 8.0
print(x)
```

---

### 7.5 Bitwise Operators

Work on binary (bit) level of integers.

| Operator | Meaning | Example | Binary idea |
|----------|---------|---------|-------------|
| `&` | AND | `5 & 3` → `1` | both bits 1 |
| `\|` | OR | `5 \| 3` → `7` | at least one bit 1 |
| `^` | XOR | `5 ^ 3` → `6` | bits different |
| `~` | NOT | `~5` → `-6` | invert bits |
| `<<` | Left shift | `5 << 1` → `10` | shift left |
| `>>` | Right shift | `5 >> 1` → `2` | shift right |

```python
a = 5   # binary 101
b = 3   # binary 011

print(a & b)   # 1  (001)
print(a | b)   # 7  (111)
print(a ^ b)   # 6  (110)
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2
```

---

### 7.6 Membership Operators

Check whether a value exists inside a sequence (string, list, tuple, set, dict keys).

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `in` | Present | `"a" in "cat"` | `True` |
| `not in` | Not present | `2 not in [1, 3]` | `True` |

```python
fruits = ["apple", "banana", "mango"]
print("apple" in fruits)       # True
print("grape" not in fruits)   # True

text = "Python"
print("th" in text)            # True

person = {"name": "Amit", "age": 25}
print("name" in person)        # True (checks keys)
```

---

### 7.7 Identity Operators

Check whether two variables point to the **same object** in memory (not just equal values).

| Operator | Meaning | Example |
|----------|---------|---------|
| `is` | Same object | `a is b` |
| `is not` | Different objects | `a is not c` |

```python
a = [1, 2]
b = a          # b points to same list as a
c = [1, 2]     # new list with same values

print(a is b)      # True  (same object)
print(a is c)      # False (different objects)
print(a == c)      # True  (same content)
print(a is not c)  # True

x = None
print(x is None)   # preferred way to check None
```

**Remember:**
- `==` → compares **values**
- `is` → compares **identity** (memory location)

---

### 7.8 Operator Precedence (Basic Order)

When multiple operators appear in one expression, Python follows this order (high → low):

1. `()` parentheses  
2. `**`  
3. `*`, `/`, `//`, `%`  
4. `+`, `-`  
5. Comparison (`==`, `<`, `>`, …)  
6. `not`  
7. `and`  
8. `or`  

```python
print(2 + 3 * 4)      # 14  (multiply first)
print((2 + 3) * 4)    # 20  (parentheses first)
print(True or False and False)  # True (and before or)
```

---

## 8. Input and Output

```python
print("Hello", "World", sep="-")  # Hello-World

name = input("Enter your name: ")
age = int(input("Enter age: "))   # convert string to int
print(f"Hi {name}, you are {age}")
```

---

## 9. Conditions (`if` / `elif` / `else`)

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

**Indentation matters** — Python uses spaces/tabs to define code blocks (usually 4 spaces).

---

## 10. Loops

Loops repeat code again and again until a condition is done.

Python has two main loops:
- `for` → loop over a sequence (list, string, range, …)
- `while` → loop while a condition is `True`

---

### 10.1 `for` loop

Used to go through each item in a collection.

```python
# loop over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# loop over a string
for ch in "Hi":
    print(ch)  # H then i

# loop over a tuple
for n in (10, 20, 30):
    print(n)
```

---

### 10.2 `while` loop

Runs **as long as** the condition is `True`.

```python
count = 0
while count < 3:
    print(count)
    count += 1
# prints: 0 1 2
```

**Important:** always update the condition variable, or it becomes an infinite loop.

```python
# Infinite loop example (avoid unless intentional)
# while True:
#     print("running...")
```

---

### 10.3 `break` and `continue`

| Keyword | Meaning |
|---------|---------|
| `break` | Exit the loop completely |
| `continue` | Skip current iteration, go to next |
| `pass` | Do nothing (placeholder) |

```python
for i in range(5):
    if i == 2:
        continue  # skip 2
    if i == 4:
        break     # stop loop
    print(i)      # 0 1 3
```

```python
# else with loop — runs if loop did NOT break
for i in range(3):
    print(i)
else:
    print("Loop finished normally")
```

---

### 10.4 `range()`

`range()` generates a sequence of numbers. Very common with `for` loops.

**Syntax:** `range(start, stop, step)`

| Form | Meaning | Example result |
|------|---------|----------------|
| `range(5)` | 0 to 4 | `0, 1, 2, 3, 4` |
| `range(1, 6)` | 1 to 5 | `1, 2, 3, 4, 5` |
| `range(0, 10, 2)` | even numbers | `0, 2, 4, 6, 8` |
| `range(5, 0, -1)` | reverse | `5, 4, 3, 2, 1` |

```python
for i in range(5):
    print(i)  # 0 1 2 3 4

for i in range(1, 6):
    print(i)  # 1 2 3 4 5

for i in range(0, 10, 2):
    print(i)  # 0 2 4 6 8
```

**Loop with index using `range(len(...))`:**

```python
fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
    print(i, fruits[i])
# 0 apple
# 1 banana
# 2 mango
```

---

### 10.5 `enumerate()`

`enumerate()` gives **index + value** together while looping. Cleaner than `range(len(...))`.

**Syntax:** `enumerate(sequence, start=0)`

```python
fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 mango
```

**Start index from 1:**

```python
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# 1 apple
# 2 banana
# 3 mango
```

Works with strings too:

```python
for i, ch in enumerate("Python"):
    print(i, ch)
```

---

### 10.6 `enumerate()` vs `range()`

Both can give you an index in a loop — but they are used differently.

#### Side-by-side example

```python
fruits = ["apple", "banana", "mango"]

# Using range(len(...))
for i in range(len(fruits)):
    print(i, fruits[i])

# Using enumerate()  ← preferred when you need index + value
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

Both print the same result.

#### Comparison table

| Point | `range()` | `enumerate()` |
|-------|-----------|---------------|
| Main use | Generate numbers / count | Get index + item together |
| Needs sequence? | Optional | Yes (list, tuple, string…) |
| Access item | Manual: `fruits[i]` | Automatic: `fruit` |
| Code style | Longer | Cleaner / more Pythonic |
| Change item by index | Easy | Also easy (`fruits[i] = ...`) |
| Best when | You only need numbers, or no list | You loop a list/string and need index |

#### When to use `range()`

```python
# 1) Just count / repeat N times
for i in range(5):
    print("Hello", i)

# 2) Numbers with step
for i in range(2, 11, 2):
    print(i)  # 2 4 6 8 10

# 3) Reverse counting
for i in range(5, 0, -1):
    print(i)  # 5 4 3 2 1
```

#### When to use `enumerate()`

```python
# 1) Need both index and value from a list
names = ["Amit", "Neha", "Ravi"]
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# 2) Find index of matching items
nums = [10, 25, 30, 25]
for i, n in enumerate(nums):
    if n == 25:
        print("Found at index:", i)
```

#### When either works — prefer `enumerate()`

```python
colors = ["red", "green", "blue"]

# OK, but less clean
for i in range(len(colors)):
    print(i, colors[i])

# Better
for i, color in enumerate(colors):
    print(i, color)
```

**Rule of thumb:**
- Need only numbers → use `range()`
- Looping a list/string and need index → use `enumerate()`
- Need index to **modify** list items → both work; `enumerate()` is still fine:

```python
nums = [1, 2, 3]
for i, n in enumerate(nums):
    nums[i] = n * 10
print(nums)  # [10, 20, 30]
```

---

### 10.7 Nested loops

A loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

```python
# print a simple pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
```

Output:

```text
*
* *
* * *
* * * *
```

---

### 10.8 Quick practice

```python
# 1) Print numbers 1 to 10 using range()
for i in range(1, 11):
    print(i)

# 2) Print list items with numbers using enumerate()
cities = ["Delhi", "Mumbai", "Pune"]
for i, city in enumerate(cities, start=1):
    print(i, city)

# 3) while loop countdown
n = 5
while n > 0:
    print(n)
    n -= 1
print("Done")
```

---

## 11. Functions

A **function** is a reusable block of code that performs a task.

**Why use functions?**
- Avoid repeating code
- Make programs easier to read
- Break big problems into small parts

---

### 11.1 Basic function

```python
def greet():
    print("Hello!")

greet()  # call the function
greet()  # can call many times
```

---

### 11.2 Parameters & return

```python
def greet(name):
    return f"Hello, {name}"

message = greet("Amit")
print(message)  # Hello, Amit
```

```python
def add(a, b):
    return a + b

print(add(5, 3))  # 8
```

- `return` sends a value back to the caller
- Without `return`, the function returns `None`

---

### 11.3 Default & keyword arguments

```python
def add(a, b=0):      # b has default value
    return a + b

print(add(5))         # 5
print(add(5, 3))      # 8

def intro(name, age):
    print(f"{name} is {age}")

intro(age=25, name="Amit")  # keyword arguments
```

---

### 11.4 Lambda (short function)

```python
square = lambda x: x * x
print(square(4))  # 16

add = lambda a, b: a + b
print(add(2, 3))  # 5
```

Use lambda for small one-line functions.

---

### 11.5 Recursion functions

**Recursion** means a function **calls itself** to solve a smaller version of the same problem.

Every recursive function needs:

1. **Base case** → when to stop (very important)
2. **Recursive case** → function calls itself with a smaller input

Without a base case → infinite recursion → `RecursionError`

```python
def countdown(n):
    if n == 0:             # base case
        print("Done!")
        return
    print(n)
    countdown(n - 1)       # recursive case

countdown(5)
# 5 4 3 2 1 Done!
```

**How it works (simple idea):**

```text
countdown(3)
  print 3
  countdown(2)
    print 2
    countdown(1)
      print 1
      countdown(0)
        print Done!
```

---

### 11.6 Recursion examples

#### 1. Factorial

`5! = 5 × 4 × 3 × 2 × 1 = 120`

```python
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))  # 120
```

Step-by-step:

```text
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

#### 2. Sum of numbers from 1 to n

```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))  # 15  (1+2+3+4+5)
```

#### 3. Fibonacci

`0, 1, 1, 2, 3, 5, 8, 13...`

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8
```

#### 4. Sum of a list

```python
def list_sum(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + list_sum(nums[1:])

print(list_sum([1, 2, 3, 4]))  # 10
```

#### 5. Reverse a string

```python
def reverse(text):
    if len(text) == 0:
        return ""
    return reverse(text[1:]) + text[0]

print(reverse("Python"))  # nohtyP
```

---

### 11.7 Recursion vs loop

Same factorial — two ways:

```python
# Recursion
def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

# Loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_rec(5))   # 120
print(factorial_loop(5))  # 120
```

| Point | Recursion | Loop (`for` / `while`) |
|-------|-----------|------------------------|
| Style | Function calls itself | Repeats with condition |
| Code | Often shorter for tree/divide problems | Often clearer for simple counting |
| Memory | Uses call stack | Usually less memory |
| Risk | `RecursionError` if too deep | Infinite loop if condition never ends |
| Best for | Factorial, Fibonacci, tree, nested data | Counting, lists, simple repeats |

**Python recursion limit:**

```python
import sys
print(sys.getrecursionlimit())  # often 1000

# sys.setrecursionlimit(2000)  # possible, but be careful
```

---

### 11.8 Important notes & mistakes

```python
# 1) Missing base case → RecursionError
# def bad(n):
#     return bad(n - 1)

# 2) Base case never reached
# def bad(n):
#     if n == 0:
#         return
#     return bad(n)   # n never changes!

# 3) Always move toward the base case
def good(n):
    if n == 0:
        return
    print(n)
    good(n - 1)  # n gets smaller
```

---

### 11.9 Quick practice

```python
# 1) Write recursive power: power(2, 3) → 8
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))  # 8

# 2) Count digits recursively: 12345 → 5
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))  # 5

# 3) Print each item of a list using recursion
def print_list(items):
    if len(items) == 0:
        return
    print(items[0])
    print_list(items[1:])

print_list(["a", "b", "c"])
```

---

## 12. Lists in Python

A **list** is a collection used to store multiple items in a single variable.

**Key points:**
- Written with square brackets `[]`
- Ordered (items have an index)
- Mutable (you can change, add, remove items)
- Allows duplicate values
- Can store different data types

```python
# mix of types is allowed
data = [1, "Amit", 3.5, True, [10, 20]]
```

---

### 12.1 Create a list

```python
# empty list
empty = []
empty2 = list()

# list of numbers
nums = [10, 20, 30, 40]

# list of strings
fruits = ["apple", "banana", "mango"]

# from other types
letters = list("ABC")     # ['A', 'B', 'C']
from_tuple = list((1, 2)) # [1, 2]
```

---

### 12.2 Access items (Indexing)

```python
fruits = ["apple", "banana", "mango", "orange"]

#      index:  0        1        2        3
#  neg index: -4       -3       -2       -1

print(fruits[0])    # apple
print(fruits[2])    # mango
print(fruits[-1])   # orange (last item)
print(fruits[-2])   # mango
```

---

### 12.3 Change items

```python
fruits = ["apple", "banana", "mango"]

fruits[1] = "grape"
print(fruits)  # ['apple', 'grape', 'mango']

# change a range
fruits[0:2] = ["kiwi", "pear"]
print(fruits)  # ['kiwi', 'pear', 'mango']
```

---

### 12.4 Add items

| Method | What it does |
|--------|--------------|
| `append(x)` | Add `x` at the **end** |
| `insert(i, x)` | Add `x` at index `i` |
| `extend(iterable)` | Add all items from another list/tuple |

```python
fruits = ["apple", "banana"]

fruits.append("mango")
print(fruits)  # ['apple', 'banana', 'mango']

fruits.insert(1, "orange")
print(fruits)  # ['apple', 'orange', 'banana', 'mango']

fruits.extend(["kiwi", "pear"])
print(fruits)  # ['apple', 'orange', 'banana', 'mango', 'kiwi', 'pear']
```

---

### 12.5 Remove items

| Method | What it does |
|--------|--------------|
| `remove(x)` | Remove first matching **value** |
| `pop()` | Remove and return **last** item |
| `pop(i)` | Remove and return item at index `i` |
| `clear()` | Remove **all** items |
| `del list[i]` | Delete item at index |

```python
nums = [10, 20, 30, 20, 40]

nums.remove(20)      # removes first 20
print(nums)          # [10, 30, 20, 40]

last = nums.pop()    # removes 40
print(last)          # 40
print(nums)          # [10, 30, 20]

item = nums.pop(1)   # removes index 1 → 30
print(item)          # 30

del nums[0]          # delete index 0
print(nums)          # [20]

nums.clear()
print(nums)          # []
```

---

### 12.6 Loop through a list

```python
fruits = ["apple", "banana", "mango"]

# values only
for fruit in fruits:
    print(fruit)

# with index
for i in range(len(fruits)):
    print(i, fruits[i])

# index + value together
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

### 12.7 Check membership & length

```python
fruits = ["apple", "banana", "mango"]

print("apple" in fruits)       # True
print("grape" not in fruits)   # True
print(len(fruits))             # 3
```

---

### 12.8 Slicing lists

```python
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])    # [1, 2, 3]
print(nums[:3])     # [0, 1, 2]
print(nums[3:])     # [3, 4, 5]
print(nums[::2])    # [0, 2, 4]
print(nums[::-1])   # [5, 4, 3, 2, 1, 0]
```

→ More on slicing: [5.2.2 Slicing](#522-slicing)

---

### 12.9 Sort & reverse

```python
nums = [3, 1, 4, 2]

nums.sort()              # sort ascending (changes list)
print(nums)              # [1, 2, 3, 4]

nums.sort(reverse=True)  # descending
print(nums)              # [4, 3, 2, 1]

nums.reverse()           # reverse current order
print(nums)              # [1, 2, 3, 4]

# sorted() returns a NEW list (original stays same)
a = [3, 1, 2]
b = sorted(a)
print(a)  # [3, 1, 2]
print(b)  # [1, 2, 3]
```

```python
# sort strings
names = ["Amit", "Ravi", "Neha"]
names.sort()
print(names)  # ['Amit', 'Neha', 'Ravi']
```

---

### 12.10 Copy a list

```python
a = [1, 2, 3]

# WRONG way (both point to same list)
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]  ← a also changed!

# CORRECT ways
a = [1, 2, 3]
c = a.copy()
d = list(a)
e = a[:]

c.append(9)
print(a)  # [1, 2, 3]  ← original safe
print(c)  # [1, 2, 3, 9]
```

---

### 12.11 Join lists

```python
a = [1, 2]
b = [3, 4]

print(a + b)       # [1, 2, 3, 4]

a.extend(b)
print(a)           # [1, 2, 3, 4]

print([0] * 3)     # [0, 0, 0]
```

---

### 12.12 Useful list methods (summary)

| Method | Description | Example |
|--------|-------------|---------|
| `append(x)` | Add at end | `[1].append(2)` → `[1, 2]` |
| `insert(i, x)` | Insert at index | `[1, 3].insert(1, 2)` → `[1, 2, 3]` |
| `extend(iter)` | Add many items | `[1].extend([2, 3])` → `[1, 2, 3]` |
| `remove(x)` | Remove by value | `[1, 2].remove(1)` → `[2]` |
| `pop(i)` | Remove by index | `[1, 2].pop()` → `2` |
| `clear()` | Empty the list | `[1, 2].clear()` → `[]` |
| `index(x)` | First index of value | `[10, 20].index(20)` → `1` |
| `count(x)` | Count occurrences | `[1, 1, 2].count(1)` → `2` |
| `sort()` | Sort in place | `[3, 1].sort()` → `[1, 3]` |
| `reverse()` | Reverse in place | `[1, 2].reverse()` → `[2, 1]` |
| `copy()` | Shallow copy | `[1, 2].copy()` → `[1, 2]` |

```python
nums = [10, 20, 10, 30]
print(nums.index(20))  # 1
print(nums.count(10))  # 2
print(min(nums))       # 10
print(max(nums))       # 30
print(sum(nums))       # 70
```

---

### 12.13 List vs Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Yes | No |
| Add/remove | Yes | No |
| Speed | Slightly slower | Slightly faster |
| Use when | Data will change | Data should stay fixed |

```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0] = 99     # OK
# my_tuple[0] = 99  # TypeError
```

---

### 12.14 Quick practice

```python
# 1) Create a list of 5 cities
# 2) Add one city with append()
# 3) Insert one city at index 0
# 4) Remove one city
# 5) Print length and sorted list

cities = ["Delhi", "Mumbai", "Pune", "Chennai", "Kolkata"]
cities.append("Jaipur")
cities.insert(0, "Goa")
cities.remove("Pune")
print(len(cities))
print(sorted(cities))
```

---

## 13. Tuples in Python

A **tuple** is a collection used to store multiple items in one variable — like a list, but **immutable** (cannot be changed).

**Key points:**
- Written with round brackets `()`
- Ordered (items have an index)
- Immutable (cannot change, add, or remove items)
- Allows duplicate values
- Can store different data types
- Faster than lists and safer for fixed data

```python
# mix of types is allowed
person = ("Amit", 25, 5.9, True)
```

---

### 13.1 Create a tuple

```python
# empty tuple
empty = ()
empty2 = tuple()

# tuple of numbers
nums = (10, 20, 30, 40)

# tuple of strings
fruits = ("apple", "banana", "mango")

# without parentheses (also a tuple)
colors = "red", "green", "blue"
print(type(colors))  # <class 'tuple'>

# single-item tuple — MUST have a comma
one = ("hello",)     # tuple
not_tuple = ("hello")  # string! (no comma)
print(type(one))       # <class 'tuple'>
print(type(not_tuple)) # <class 'str'>

# from other types
letters = tuple("ABC")      # ('A', 'B', 'C')
from_list = tuple([1, 2])   # (1, 2)
```

---

### 13.2 Access items (Indexing)

```python
fruits = ("apple", "banana", "mango", "orange")

#      index:  0        1        2        3
#  neg index: -4       -3       -2       -1

print(fruits[0])    # apple
print(fruits[2])    # mango
print(fruits[-1])   # orange (last item)
print(fruits[-2])   # mango
```

---

### 13.3 Slicing tuples

```python
nums = (0, 1, 2, 3, 4, 5)

print(nums[1:4])    # (1, 2, 3)
print(nums[:3])     # (0, 1, 2)
print(nums[3:])     # (3, 4, 5)
print(nums[::2])    # (0, 2, 4)
print(nums[::-1])   # (5, 4, 3, 2, 1, 0)
```

→ More on slicing: [5.2.2 Slicing](#522-slicing)

---

### 13.4 Immutable nature (cannot change)

```python
point = (10, 20)

# point[0] = 99      # TypeError — cannot change item
# point.append(30)   # AttributeError — no append
# point.remove(10)   # AttributeError — no remove
```

**Workaround:** convert to list → change → convert back to tuple

```python
point = (10, 20)
temp = list(point)
temp[0] = 99
temp.append(30)
point = tuple(temp)
print(point)  # (99, 20, 30)
```

**Note:** If a tuple contains a list, that list **can** still be changed.

```python
data = (1, 2, [3, 4])
data[2].append(5)
print(data)  # (1, 2, [3, 4, 5])
```

---

### 13.5 Loop through a tuple

```python
fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

### 13.6 Check membership & length

```python
fruits = ("apple", "banana", "mango")

print("apple" in fruits)       # True
print("grape" not in fruits)   # True
print(len(fruits))             # 3
```

---

### 13.7 Join tuples

```python
a = (1, 2)
b = (3, 4)

print(a + b)       # (1, 2, 3, 4)
print(("hi",) * 3) # ('hi', 'hi', 'hi')
```

---

### 13.8 Useful tuple methods

Tuples have only **2** built-in methods:

| Method | Description | Example | Result |
|--------|-------------|---------|--------|
| `count(x)` | Count how many times `x` appears | `(1, 2, 1).count(1)` | `2` |
| `index(x)` | First index of `x` | `(10, 20, 30).index(20)` | `1` |

```python
nums = (10, 20, 10, 30)

print(nums.count(10))  # 2
print(nums.index(20))  # 1

print(min(nums))       # 10
print(max(nums))       # 30
print(sum(nums))       # 70
```

---

### 13.9 Tuple unpacking

Assign each item to a variable in one step.

```python
point = (10, 20)
x, y = point
print(x)  # 10
print(y)  # 20

person = ("Amit", 25, "Delhi")
name, age, city = person
print(name, age, city)  # Amit 25 Delhi

# swap values easily
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1

# unpack with *
nums = (1, 2, 3, 4, 5)
first, *middle, last = nums
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

---

### 13.10 Convert list ↔ tuple

```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3)

back_to_list = list(my_tuple)
print(back_to_list)  # [1, 2, 3]
```

---

### 13.11 When to use a tuple

Use a **tuple** when:
- Data should not change (coordinates, RGB colors, days of week)
- You want slightly faster / safer storage
- You need a dictionary key (lists cannot be keys)

```python
# coordinates
location = (28.61, 77.20)

# RGB color
red = (255, 0, 0)

# days
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# tuple as dict key
scores = {("Math", "Amit"): 95}
print(scores[("Math", "Amit")])  # 95
```

---

### 13.12 Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Mutable | No | Yes |
| Methods | `count`, `index` only | Many (`append`, `remove`, …) |
| Speed | Faster | Slightly slower |
| As dict key | Yes | No |
| Use when | Fixed data | Data that changes |

```python
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

my_list[0] = 99     # OK
# my_tuple[0] = 99  # TypeError
```

---

### 13.13 Quick practice

```python
# 1) Create a tuple of 5 subjects
# 2) Print first and last subject
# 3) Count how many times a subject appears
# 4) Unpack into variables (or use slicing)
# 5) Convert to list, add one item, convert back

subjects = ("Math", "Science", "English", "Math", "History")
print(subjects[0])
print(subjects[-1])
print(subjects.count("Math"))

first, *rest = subjects
print(first, rest)

temp = list(subjects)
temp.append("CS")
subjects = tuple(temp)
print(subjects)
```

---

## 14. Dictionaries in Python

A **dictionary** stores data in **key : value** pairs.

**Key points:**
- Written with curly braces `{}`
- Keys must be **unique**
- Keys must be **immutable** types (`str`, `int`, `tuple`, …) — not lists
- Values can be any type
- Mutable (you can add, change, remove items)
- Ordered (Python 3.7+) — keeps insertion order

```python
person = {
    "name": "Amit",
    "age": 25,
    "city": "Delhi"
}
```

---

### 14.1 Create a dictionary

```python
# empty dict
empty = {}
empty2 = dict()

# normal way
student = {
    "name": "Amit",
    "age": 25,
    "course": "Python"
}

# using dict()
student2 = dict(name="Amit", age=25, course="Python")

# from list of pairs
pairs = [("name", "Amit"), ("age", 25)]
student3 = dict(pairs)

print(student)
print(type(student))  # <class 'dict'>
```

---

### 14.2 Access items

```python
student = {"name": "Amit", "age": 25, "city": "Delhi"}

# using key
print(student["name"])   # Amit

# using get() — safer if key may be missing
print(student.get("age"))           # 25
print(student.get("email"))         # None (no error)
print(student.get("email", "N/A"))  # N/A (default value)

# student["email"]  # KeyError if key does not exist
```

**Get keys, values, and items:**

```python
print(student.keys())    # dict_keys(['name', 'age', 'city'])
print(student.values())  # dict_values(['Amit', 25, 'Delhi'])
print(student.items())   # dict_items([('name', 'Amit'), ...])
```

---

### 14.3 Add / update items

```python
student = {"name": "Amit", "age": 25}

# add new key
student["city"] = "Delhi"

# update existing key
student["age"] = 26

# update multiple keys
student.update({"course": "Python", "age": 27})

print(student)
# {'name': 'Amit', 'age': 27, 'city': 'Delhi', 'course': 'Python'}
```

---

### 14.4 Remove items

| Method / way | What it does |
|--------------|--------------|
| `pop(key)` | Remove key and return its value |
| `popitem()` | Remove and return the **last** inserted item |
| `del dict[key]` | Delete a key |
| `clear()` | Remove all items |

```python
student = {"name": "Amit", "age": 25, "city": "Delhi", "course": "Python"}

age = student.pop("age")
print(age)       # 25
print(student)   # {'name': 'Amit', 'city': 'Delhi', 'course': 'Python'}

last = student.popitem()
print(last)      # ('course', 'Python')

del student["city"]
print(student)   # {'name': 'Amit'}

student.clear()
print(student)   # {}
```

---

### 14.5 Loop through a dictionary

```python
student = {"name": "Amit", "age": 25, "city": "Delhi"}

# keys only (default)
for key in student:
    print(key)

# keys
for key in student.keys():
    print(key)

# values
for value in student.values():
    print(value)

# key + value
for key, value in student.items():
    print(key, "→", value)
```

---

### 14.6 Check keys & length

```python
student = {"name": "Amit", "age": 25}

print("name" in student)       # True  (checks keys)
print("Amit" in student)       # False (not checking values)
print("Amit" in student.values())  # True

print(len(student))            # 2
```

---

### 14.7 Nested dictionaries

A dictionary inside another dictionary.

```python
students = {
    "s1": {"name": "Amit", "age": 25},
    "s2": {"name": "Neha", "age": 22}
}

print(students["s1"]["name"])  # Amit
print(students["s2"]["age"])   # 22

students["s1"]["city"] = "Delhi"
print(students["s1"])
# {'name': 'Amit', 'age': 25, 'city': 'Delhi'}
```

---

### 14.8 Useful dictionary methods

| Method | Description | Example idea |
|--------|-------------|--------------|
| `get(k, default)` | Get value safely | `d.get("x", 0)` |
| `keys()` | All keys | `d.keys()` |
| `values()` | All values | `d.values()` |
| `items()` | All key-value pairs | `d.items()` |
| `update(...)` | Add/update many items | `d.update({"a": 1})` |
| `pop(k)` | Remove key, return value | `d.pop("a")` |
| `popitem()` | Remove last item | `d.popitem()` |
| `clear()` | Empty dictionary | `d.clear()` |
| `copy()` | Shallow copy | `d.copy()` |
| `setdefault(k, v)` | Get key; set if missing | `d.setdefault("x", 0)` |

```python
marks = {"Math": 90, "Science": 85}

print(marks.get("English", 0))  # 0

marks.setdefault("English", 70)
print(marks)
# {'Math': 90, 'Science': 85, 'English': 70}

# setdefault does nothing if key already exists
marks.setdefault("Math", 100)
print(marks["Math"])  # 90 (unchanged)
```

---

### 14.9 Copy a dictionary

```python
a = {"x": 1, "y": 2}

# WRONG — both point to same dict
b = a
b["z"] = 3
print(a)  # {'x': 1, 'y': 2, 'z': 3}

# CORRECT
a = {"x": 1, "y": 2}
c = a.copy()
d = dict(a)

c["z"] = 3
print(a)  # {'x': 1, 'y': 2}
print(c)  # {'x': 1, 'y': 2, 'z': 3}
```

---

### 14.10 Dict vs List

| Feature | Dictionary | List |
|---------|------------|------|
| Syntax | `{"a": 1}` | `[1, 2, 3]` |
| Access by | Key | Index (0, 1, 2…) |
| Best for | Labeled data | Ordered collection |
| Lookup | Fast by key | Fast by position |
| Example | Student details | List of scores |

```python
# list — position based
scores = [90, 85, 88]

# dict — meaning based
scores = {"Math": 90, "Science": 85, "English": 88}
print(scores["Math"])  # 90
```

---

### 14.11 When to use a dictionary

Use a **dictionary** when:
- Data has labels (name, age, city)
- You need fast lookup by key
- You store related info about one object (user, product, config)

```python
# user profile
user = {
    "id": 101,
    "name": "Amit",
    "email": "amit@example.com",
    "is_active": True
}

# product
product = {
    "name": "Laptop",
    "price": 45000,
    "in_stock": True
}

# simple config
config = {
    "theme": "dark",
    "language": "en"
}
```

---

### 14.12 Quick practice

```python
# 1) Create a dict for a student (name, age, course, marks)
# 2) Add city
# 3) Update marks
# 4) Print all keys and values
# 5) Remove course and print final dict

student = {
    "name": "Amit",
    "age": 25,
    "course": "Python",
    "marks": 90
}

student["city"] = "Delhi"
student["marks"] = 95

for key, value in student.items():
    print(key, "→", value)

student.pop("course")
print(student)
```

---

## 15. Sets in Python

A **set** is a collection of **unique** items. Duplicates are removed automatically.

**Key points:**
- Written with curly braces `{}` (like dict, but **no key:value**)
- Unordered (no index like `s[0]`)
- Mutable (you can add/remove items)
- No duplicate values
- Items must be immutable (`int`, `str`, `tuple` — not `list` or `dict`)
- Fast for membership checks (`in`)

```python
nums = {1, 2, 2, 3, 3}
print(nums)  # {1, 2, 3}
```

---

### 15.1 Create a set

```python
# empty set — MUST use set()
empty = set()
# empty = {}   # This creates a DICT, not a set!

# set of numbers
nums = {1, 2, 3, 4}

# set of strings
fruits = {"apple", "banana", "mango"}

# from a list (duplicates removed)
nums2 = set([1, 2, 2, 3, 3, 3])
print(nums2)  # {1, 2, 3}

# from a string
letters = set("hello")
print(letters)  # {'h', 'e', 'l', 'o'}

print(type(nums))  # <class 'set'>
```

---

### 15.2 Add items

| Method | What it does |
|--------|--------------|
| `add(x)` | Add one item |
| `update(iterable)` | Add multiple items |

```python
fruits = {"apple", "banana"}

fruits.add("mango")
print(fruits)  # {'apple', 'banana', 'mango'}

fruits.add("apple")  # already exists — ignored
print(fruits)  # same set

fruits.update(["orange", "kiwi"])
print(fruits)

fruits.update(("grape", "pear"))
print(fruits)
```

---

### 15.3 Remove items

| Method | What it does |
|--------|--------------|
| `remove(x)` | Remove `x` — **error** if missing |
| `discard(x)` | Remove `x` — **no error** if missing |
| `pop()` | Remove and return a random item |
| `clear()` | Remove all items |

```python
nums = {10, 20, 30, 40}

nums.remove(20)
print(nums)  # {10, 30, 40}

nums.discard(100)  # safe — no error
nums.discard(30)
print(nums)  # {10, 40}

item = nums.pop()
print(item)
print(nums)

nums.clear()
print(nums)  # set()
```

---

### 15.4 Loop through a set

```python
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)
```

Note: order is not guaranteed.

---

### 15.5 Check membership & length

```python
fruits = {"apple", "banana", "mango"}

print("apple" in fruits)       # True
print("grape" not in fruits)   # True
print(len(fruits))             # 3
```

---

### 15.6 Set operations

Very useful for comparing groups of data.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

| Operation | Operator | Method | Result idea |
|-----------|----------|--------|-------------|
| Union | `a \| b` | `a.union(b)` | All items from both |
| Intersection | `a & b` | `a.intersection(b)` | Common items |
| Difference | `a - b` | `a.difference(b)` | In `a` but not in `b` |
| Symmetric difference | `a ^ b` | `a.symmetric_difference(b)` | In either, but not both |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # {1, 2, 3, 4, 5, 6}  union
print(a & b)  # {3, 4}              intersection
print(a - b)  # {1, 2}              difference
print(b - a)  # {5, 6}
print(a ^ b)  # {1, 2, 5, 6}        symmetric difference

# same using methods
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
```

**Subset / Superset / Disjoint:**

```python
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))      # True   (x is inside y)
print(y.issuperset(x))    # True   (y contains x)
print(x.isdisjoint({5}))  # True   (no common items)
print(x.isdisjoint({2}))  # False
```

---

### 15.7 Useful set methods

| Method | Description |
|--------|-------------|
| `add(x)` | Add one item |
| `update(iter)` | Add many items |
| `remove(x)` | Remove item (error if missing) |
| `discard(x)` | Remove item (safe) |
| `pop()` | Remove random item |
| `clear()` | Empty the set |
| `union()` | Combine sets |
| `intersection()` | Common items |
| `difference()` | Items only in first set |
| `symmetric_difference()` | Items in one set only |
| `issubset()` | Check subset |
| `issuperset()` | Check superset |
| `isdisjoint()` | Check no common items |
| `copy()` | Shallow copy |

```python
a = {1, 2, 3}
b = a.copy()
b.add(4)
print(a)  # {1, 2, 3}
print(b)  # {1, 2, 3, 4}
```

---

### 15.8 `frozenset`

An **immutable** set — cannot add or remove items.

```python
fs = frozenset([1, 2, 2, 3])
print(fs)  # frozenset({1, 2, 3})

# fs.add(4)     # AttributeError
# fs.remove(1)  # AttributeError

# can be used as a dict key (normal set cannot)
data = {frozenset([1, 2]): "group A"}
print(data)
```

---

### 15.9 Set vs List vs Dict

| Feature | Set | List | Dict |
|---------|-----|------|------|
| Syntax | `{1, 2}` | `[1, 2]` | `{"a": 1}` |
| Duplicates | No | Yes | Keys unique |
| Ordered / index | No | Yes | Keys (3.7+) |
| Mutable | Yes | Yes | Yes |
| Best for | Unique items, math ops | Ordered data | Key-value data |

```python
# remove duplicates from a list using set
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
print(unique)  # [1, 2, 3]  (order may change)
```

---

### 15.10 When to use a set

Use a **set** when:
- You need unique values only
- You want to remove duplicates
- You need fast `in` checks
- You compare groups (common items, differences)

```python
# unique visitors
visitors = {"Amit", "Neha", "Amit", "Ravi"}
print(visitors)  # {'Amit', 'Neha', 'Ravi'}

# common friends
my_friends = {"Amit", "Neha", "Ravi"}
your_friends = {"Neha", "Karan", "Ravi"}
common = my_friends & your_friends
print(common)  # {'Neha', 'Ravi'}

# fast membership
allowed = {"admin", "editor", "viewer"}
role = "editor"
print(role in allowed)  # True
```

---

### 15.11 Quick practice

```python
# 1) Create a set of cities (with a duplicate)
# 2) Add one city
# 3) Remove one city safely with discard()
# 4) Find common cities with another set
# 5) Print length

cities = {"Delhi", "Mumbai", "Pune", "Delhi"}
print(cities)

cities.add("Jaipur")
cities.discard("Pune")

other = {"Mumbai", "Chennai", "Jaipur"}
print(cities & other)
print(len(cities))
```

---

## 16. Errors and Exceptions (Basic)

```python
try:
    number = int("abc")
except ValueError:
    print("Invalid number")
finally:
    print("Always runs")
```

---

## 17. Modules (Basic)

```python
import math
print(math.sqrt(16))  # 4.0

from math import pi
print(pi)

import math as m
print(m.ceil(3.2))    # 4
```

---

## 18. Quick Practice Checklist

- [ ] Create variables of each basic type (`int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`)
- [ ] Print `type()` for each
- [ ] List / use Python keywords (do not use them as variable names)
- [ ] Try all 7 operator types: arithmetic, comparison, logical, assignment, bitwise, membership, identity
- [ ] Use `if` / `elif` / `else`
- [ ] Write a `for` and a `while` loop
- [ ] Write a function that returns a value
- [ ] Convert types with `int()`, `str()`, `float()`
- [ ] Use `in`, `and`, `or`, `not`, `is`, `is not`

---

## 19. Mini Examples

### Example 1 — Simple calculator idea

```python
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Cannot divide by zero")
else:
    print("Unknown operator")
```

### Example 2 — Count word length

```python
word = input("Enter a word: ")
print(f"Length = {len(word)}")
print(f"Upper = {word.upper()}")
```

---

## 20. Next Steps (After Basics)

1. File handling (`open`, `read`, `write`)
2. List/dict comprehensions
3. Object-oriented programming (`class`)
4. Virtual environments and packages (`pip`)
5. Standard library (`datetime`, `os`, `json`, `random`)

---

*Keep this file as your beginner reference. Practice each section in the Python interpreter or a `.py` file.*
