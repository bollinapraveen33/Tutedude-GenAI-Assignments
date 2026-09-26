# Task 4: Combined Operations

# 1-> Using the products list and price_dict, create a list of tuples named catalog where each tuple is (product_name, price, category).
catalog = [
    ("phone", 20000, "Electronics"),
    ("laptop", 75000, "Electronics"),
    ("headphones", 5000, "Electronics"),
    ("smartwatch", 2000, "Electronics"),
    ("shoes", 500, "Footwear"),
    ("bags", 200, "Bags & Accessories")
]


# 2->From catalog, create a new dictionary category_to_products that maps each category to a list of product names in that category.
category_to_products = {}

for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product_name)
print("Category to products:", category_to_products)


# 3->Print all products that belong to the category that has the maximum number of products.
maximum = 0
max_category = ""

for category, products in category_to_products.items():
    if len(products) > maximum:
        maximum = len(products)
        max_category = category

print("Category with maximum products:", max_category)
print("Number of products:", maximum)

print("Products in that category:")
for product in category_to_products[max_category]:
    print(product)
