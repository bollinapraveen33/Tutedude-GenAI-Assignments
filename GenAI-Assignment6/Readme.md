## Assignment6: exception Handling 

## Problem Statement:
this assignment focuses on handling unexpected user inputs, invalid operations and runtime errors to over come this i used the try -- except

##  In this assignment the Topics Covered:
try and except
Multiple except blocks
else block
finally block
Raising custom exceptions using raise
ValueError
ZeroDivisionError
TypeError
FileNotFoundError
PermissionError

## Restrictions:
Do not use classes
Do not use modules
Do not use OOP concepts
Do not use file handling except where required in Task 4
Focus only on exception handling
Keep the programs simple and readable

## Tasks that are I performed in this assignment:

### Task 1: Safe Division Utility

Take numerator and denominator from the user.
Handle ValueError for invalid input.
Handle ZeroDivisionError when denominator is zero.
Use the else block to display the result when there is no error.
Use finally to print "Operation Complete".

### Task 2: Bill Calculator with Error Handling

 Given a list of product prices.
 Add only valid positive numerical prices.
 Handle TypeError for non-numeric values.
 Raise ValueError for negative prices.
 Continue processing after an error.
 Display the final total.

### Task 3: Custom Exception: Age Validator

 Create a function check_age(age)
 Allow ages between 1 and 120.
 Raise ValueError if the age is outside the valid range.
 Take age as input from the user.
 Handle the custom error message using try-except.

### Task 4: File Reader with Exception Handling
## here i am using the example.txt file 

 Ask the user for a filename.
 Open and read the file.
 Handle FileNotFoundError.
 Handle PermissionError.
 If successful, print the first 3 lines.
 Use finally to print "File operation attempted.

### Task 5: Mini Program: Safe Shopping Cart

 Create an empty shopping cart.
 Allow the user to enter product prices.
 Stop when the user enters q. 
 Convert each price to a float.
 Handle invalid input using ValueError.
 Raise an exception if the price is negative.
 Display the total number of items.
 Display the total bill.

## How to Run
1. Install Python.
2. Open the project folder.
3. Run each codecell separately.

## Conclusion
This assignment helps in understanding Python exception handling using
try, except, else, finally.

## assignment structure
assignment-6(folder)
  --Assignment_6_Exception_Handling_All_the_tasks.  ipynb.
  --example.txt
  --readme.md.

