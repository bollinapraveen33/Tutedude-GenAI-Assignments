# Assignment 3: Python - Functions

## Overview

This assignment demonstrates different types of Python functions and functional programming concepts using simple price and product-related examples.

The assignment covers:

-> User-Defined Functions
-> Recursive Functions
-> Lambda Functions
-> map()
-> filter()
-> Default Arguments
-> Function Calls
-> Loops
-> Conditional Statements

## Files Included

### task1.py - Price After Discount

-> Creates a user-defined function to calculate the price after discount.
-> Accepts the price and discount percentage.
-> Uses a default discount percentage of 5%.
-> Applies the discount to the given price.
-> Ensures that the discount percentage does not exceed 60%.
-> Returns the final price after discount.

### task2.py - Factorial Utility

-> Creates a recursive function to calculate the factorial of a number.
-> Handles the base cases when n == 0 and n == 1.
-> Prints an error message if the number is negative.
-> Demonstrates recursive function calls.

### task3.py - GST Calculator

-> Uses a lambda function to calculate the price after adding 18% GST.
-> Calculates the GST amount based on the original price.
-> Returns the final price including GST.
-> Uses another lambda function to calculate the final price after GST and discount.

### task4.py - Apply GST to List of Prices

-> Creates a list of product prices.
-> Uses map() and a lambda function to apply 18% GST to all prices.
-> Generates a new list containing prices after GST.
-> Prints the original prices.
-> Prints the prices after GST.

### task5.py - Filter Expensive Products

-> Creates a list of product prices.
-> Uses filter() to find prices greater than 500.
-> Creates another list containing prices less than or equal to 500.
-> Prints both filtered lists.

### task6.py - Combined Utility Function

-> Creates a function that accepts a list of prices.
-> Uses map() and a lambda function to apply a 10% discount to all prices.
-> Creates a new list containing discounted prices.
-> Uses filter() to keep only discounted prices greater than 300.
-> Returns both the discounted prices and filtered prices.

### task7.py - Menu Using Functions

-> Creates a function to add a price to a list.
-> Creates a function to calculate the average price.
-> Creates a function to find the maximum price.
-> Uses loops and conditional statements to create a simple menu.
-> Allows the user to add prices.
-> Displays the average price.
-> Displays the highest price.
-> Allows the user to quit the program.

## Requirements

-> Python 3
-> No external libraries are required.
-> The programs use basic Python functions and operations only.
-> we used only the statistics module at the 7th task

## How to Run

Open a terminal in this folder and run each file separately:

    python task1.py

    python task2.py

    python task3.py

    python task4.py

    python task5.py

    python task6.py

    python task7.py

## Restrictions Followed

-> No classes are used.
-> No Object-Oriented Programming (OOP) is used.
-> No external packages are used.
-> No file handling is used.
-> No exception handling is used.
-> The programs use simple and readable Python code.
-> The assignment focuses on functions, recursion, lambda functions,map(), and 0filter().
-> Each task is provided in a separate Python file.

## Folder Structure

    GenAI-Task-3-BNagaPraveen
        
        README.md
        task1.py
        task2.py
        task3.py
        task4.py
        task5.py
        task6.py
        task7.py
       