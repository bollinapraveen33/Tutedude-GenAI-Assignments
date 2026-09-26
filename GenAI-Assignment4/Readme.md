# Assignment 4: File Handling (Read, Write, Append, Modes)

## 📌 Problem Statement

This assignment focuses on Python file handling operations used to store sales data, read existing records, append new records, generate reports, and safely handle file-related errors.

The tasks are implemented using Python's built-in file handling features and `open()` wherever possible.

## 📚 Topics Covered

- File opening modes: `r`, `w`, `a`, `r+`, `w+`
- Reading files using:
  - `read()`
  - `readline()`
  - `readlines()`
- Writing data to files
- Appending new records
- Converting file data into integers
- Calculating sales statistics
- Creating and reading product files
- File existence checking using `os.path.exists()`
- Exception handling for file operations
- Generating a discounted-price report
- Using `with open()` for safe file handling

## 📝 Tasks

### Task 1: Write Sales Records to a File

- Create a list of sales amounts.
- Write each sales amount to `sales_data.txt`.
- Store each sale on a separate line.
- Reopen the file and display its contents.

### Task 2: Read File in Different Ways

Using `sales_data.txt`:

- Read the complete file using `read()`.
- Read the first line using `readline()`.
- Read all remaining lines using `readlines()`.
- Convert the values into integers.

### Task 3: Append New Sales

- Append new sales records to `sales_data.txt`.
- Reopen the file and display the updated contents.
- Calculate the total number of lines after appending.

### Task 4: Generate Summary Report from File

Using only file reading operations:

- Read all sales values from `sales_data.txt`.
- Convert them into integers.
- Calculate and display:
  - Total Sales
  - Highest Sale
  - Lowest Sale
  - Average Sale

### Task 5: Create Product Info File

- Ask the user to enter product names and prices.
- Store the product information in `products.txt`.
- Use the format:

```text
ProductName | Price
```

- Read the file and display each product with proper formatting.

### Task 6: Read File Safely

- Ask the user for a filename.
- Check whether the file exists using `os.path.exists()`.
- If the file exists, read and display its contents.
- If the file does not exist, display:

```text
File not found. Please check the filename.
```

### Task 7: Mini Project – Export Discounted Prices

A dictionary of product prices is used to calculate discounted prices.

The program:

- Stores product names and original prices.
- Asks the user for a discount percentage.
- Calculates the discounted price for each product.
- Writes the results to `discount_report.txt`.
- Uses the format:

```text
Product | Original Price | Discounted Price
```

- Reads the report and displays it in the terminal.
- Optionally calculates:
  - Total Items
  - Average Discounted Price

## 📂 File Structure

```text
Assignment-4/
│
├── all_the_tasks
├── discount_report
├── products
├── sales_data
└── README.md
```

### File Description

| File | Description |
|------|-------------|
| `all_the_tasks` | Contains the Python code for the assignment tasks. |
| `sales_data` | Stores the sales records used in Tasks 1–4. |
| `products` | Stores product names and prices created in Task 5. |
| `discount_report` | Stores the discounted-price report generated in Task 7. |
| `README.md` | Documentation and explanation of the assignment. |

## 🛠️ Requirements

- Python 3.x
- No external libraries are required.
- The assignment uses Python's built-in file handling features.

## 🎯 Learning Outcome

After completing this assignment, the learner should understand how to:

- Create, read, write, and append files in Python.
- Use different file modes.
- Process data stored in text files.
- Perform calculations using data read from files.
- Handle missing files safely.
- Generate useful reports using file handling operations.
- Use context managers such as `with open()` for safe file operations.

## 👨‍💻 Submission

All task code files and generated text files are kept together in a single folder along with this `README.md` file.
