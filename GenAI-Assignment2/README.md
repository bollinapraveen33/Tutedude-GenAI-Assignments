# Assignment 2: Python - Control Flow

## Overview

This assignment demonstrates Python control flow concepts using simple order-processing examples.

The main topics are:
- if / elif / else
- for loop
- while loop
- break
- continue
- try / except
- Lists
- Basic arithmetic

## Files Included

### task1.py - Discount Rules
- Gets an order amount from the user using `input()`.
- Applies the required discount rules using `if`, `elif`, and `else`.
- Calculates the subtotal, 5% tax, and final total.
- Handles invalid numeric input using `try` and `except`.

### task2.py - Process Multiple Orders
- Uses the given order list:
  `[1200, 2500, 800, 1750, 3000]`
- Processes every order using a `for` loop.
- Applies the same discount rules as Task 1.
- Displays the order amount, discount, and final amount.
- Calculates total revenue after discounts.
- Counts orders that received a discount.

### task3.py - User Menu
- Uses a `while` loop to repeatedly display a menu.
- Option `1` adds an order amount to a list.
- Option `2` displays all orders and totals after applying discounts.
- Option `q` exits the program using `break`.
- Invalid input uses `continue` to show the menu again.

### task5.py - Loop Control with Conditions
- Uses the given daily sales list:
  `[200, 150, 0, 400, 50, -1, 300]`
- Uses `break` when corrupted data (`-1`) is found.
- Uses `continue` when sales are `0`.
- Adds valid positive sales to `total_sales`.
- Displays the running total and final total.

## Requirements

- Python 3
- No external libraries are required.
- No functions or classes are used.
- No file operations are used.

## How to Run

Open a terminal inside this folder and run each Python file separately:

    python task1.py
    python task2.py
    python task3.py
    python task5.py

## Folder Structure

    GenAI-Task-2-BNagaPraveen/
    ├── task1.py
    ├── task2.py
    ├── task3.py
    ├── task5.py
    └── README.md

## Restrictions Followed

- Solutions use control flow concepts only.
- No external libraries are used.
- No advanced topics are introduced.
- No functions or classes are used.
- No file input/output operations are used.

## Conclusion

This assignment demonstrates how conditional statements and loops can be used to process orders, create a simple menu, and control loop execution using `break` and `continue`.
