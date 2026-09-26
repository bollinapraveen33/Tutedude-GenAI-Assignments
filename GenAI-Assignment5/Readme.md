# Assignment 5: Importing, Creating Modules & Packages

## 📌 Problem Statement

This assignment focuses on creating and using Python modules and packages. The goal is to understand how Python code can be organized into separate files and packages and then imported and reused in another program.

The assignment covers creating simple modules, importing modules in different ways, creating a package using `__init__.py`, and importing functions directly from the package.

## 📚 Topics Covered

- Creating Python modules (`.py` files)
- Importing modules
- Using `import`
- Using `from ... import ...`
- Creating Python packages
- Using `__init__.py`
- Importing functions from a package
- Organizing Python code into a structured folder
- Keeping functions simple and beginner-friendly

## 📂 Project Structure

Based on the submitted folder structure, the assignment is organized into the following files and folders:

```text
modules_assignment/
│
├── main.py
├── math_utils.py
├── string_utils.py
│
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py
```

### File and Folder Description

| File / Folder | Description |
|---|---|
| `main.py` | Main Python file used to import and test the modules and package functions. |
| `math_utils.py` | Module containing basic mathematical functions such as addition, subtraction, and square. |
| `string_utils.py` | Module containing string-related functions such as capitalization, reversing, and word counting. |
| `shop_package/` | Python package containing discount and billing modules. |
| `shop_package/__init__.py` | Initializes the package and allows selected functions to be imported directly from the package. |
| `shop_package/discount.py` | Contains functions for calculating discounted prices. |
| `shop_package/billing.py` | Contains functions for calculating total bills and tax. |

## 📝 Tasks

### Task 1: Create a Simple Module (`math_utils.py`)

The `math_utils.py` module contains the following functions:

- `add(a, b)` → returns `a + b`
- `subtract(a, b)` → returns `a - b`
- `square(n)` → returns `n²`

These functions are imported and tested in `main.py` in two different ways:

```python
import math_utils
```

and

```python
from math_utils import square
```

### Task 2: Create Another Module (`string_utils.py`)

The `string_utils.py` module contains:

- `capitalize_words(text)` → returns the text with each word capitalized
- `reverse_string(text)` → returns the reversed string
- `word_count(text)` → returns the number of words in the text

The module is imported into `main.py` and all functions are tested.

### Task 3: Create a Simple Package (`shop_package`)

The `shop_package` folder contains two modules.

#### `discount.py`

Functions:

- `apply_discount(price, percent)` → returns the discounted price
- `flat_discount(price)` → subtracts 50 from the given price

#### `billing.py`

Functions:

- `calculate_total(prices)` → returns the total bill
- `apply_tax(amount)` → adds 5% tax

#### `__init__.py`

The `__init__.py` file is used to expose selected functions directly from the package:

```python
from .discount import apply_discount, flat_discount
from .billing import calculate_total, apply_tax
```

This allows the functions to be imported directly from `shop_package`.

### Task 4: Import the Package in `main.py`

The package is imported and tested in `main.py`.

Examples include:

```python
import shop_package.discount as disc
```

and

```python
from shop_package.billing import calculate_total
```

The functions from the package are then called and tested with sample values.

## 🛠️ Restrictions Followed

- No advanced OOP concepts are required.
- No OOP exception handling is used.
- No file I/O beyond creating `.py` files is required.
- The focus is only on modules and packages.
- Function logic is kept simple and beginner-friendly.
- Python's built-in module and package import features are used.

## 🎯 Learning Outcomes

After completing this assignment, the learner should be able to:

- Create reusable Python modules.
- Import modules using different import styles.
- Create a Python package using `__init__.py`.
- Import functions from individual modules.
- Import functions directly from a package.
- Organize Python programs into multiple files.
- Reuse code instead of writing the same functions repeatedly.

## ▶️ How to Run

Open a terminal in the `modules_assignment` folder and run:

```bash
python main.py
```

Make sure the `shop_package` folder and its Python files are in the correct location before running the program.

## 📤 Submission

The complete assignment folder contains all Python code files along with this `README.md` file.

The folder can be converted into a ZIP file and uploaded according to the assignment submission guidelines.
