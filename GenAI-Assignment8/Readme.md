# Assignment 8: Streamlit (Basic App Building)

This assignment contains four simple Streamlit applications created
using Python.

## Project Structure

``` text
streamlit_assignment/
│
├── app_basic.py
├── app_discount.py
├── app_product_form.py
├── app_dashboard.py
└── README.md
```

## Tasks

### Task 1: Basic Streamlit App

**File:** `app_basic.py`

-   Displays the title "Welcome to Streamlit"
-   Takes the user's name as input
-   Displays a greeting when the button is clicked

### Task 2: Price Calculator

**File:** `app_discount.py`

-   Takes the product price
-   Takes discount percentage using a slider
-   Calculates the discounted price
-   Displays the result using `st.success()`
-   Shows a simple comparison table

### Task 3: Product Form

**File:** `app_product_form.py`

-   Uses the Streamlit sidebar
-   Takes product name
-   Allows category selection
-   Takes product price
-   Displays the product details after clicking **Add Product**

### Task 4: Mini Dashboard

**File:** `app_dashboard.py`

-   Displays a sales dashboard title and description
-   Allows the user to select a month
-   Uses a static monthly sales dictionary
-   Displays the selected month's sales
-   Displays a bar chart of monthly sales

## Technologies Used

-   Python
-   Streamlit

## How to Run

Install Streamlit:

``` bash
pip install streamlit
```

Run any application using:

``` bash
streamlit run app_basic.py
```

Replace `app_basic.py` with the required file name to run another task.

## Learning Outcomes

Through this assignment, I practiced:

-   Streamlit titles and text
-   Text input and buttons
-   Sliders and selectboxes
-   Sidebar components
-   Number input
-   Success messages
-   Simple calculations
-   Tables
-   Basic charts

## Note

This project uses simple Streamlit components and does not use
databases, APIs, sessions, or advanced features.
