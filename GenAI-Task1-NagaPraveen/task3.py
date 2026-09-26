# Task 3: Product Pricing (Dictionaries)

# 1->Create a dictionary price_dict where keys are product names and values are prices (integers or floats). Include at least 6 entries.
price_dict = {
    "phone": 20000,
    "laptop": 75000,
    "headphones": 5000,
    "smartwatch": 2000,
    "shoes": 500,
    "bags": 200
}
print("Original price dictionary:", price_dict)

'''Write small code blocks to:
Add a new product with price to price_dict.
Update the price of an existing product.
Remove a product by name (handle the case when the product does not exist).'''
price_dict["pen"] = 10
print("After adding pen:", price_dict)

# 3->Print the average price of all products (use only dictionary operations and basic arithmetic).
price_dict["phone"] = 25000
print("After updating phone:", price_dict)
# Remove a product by name
if "pen" in price_dict:
    del price_dict["pen"]
# Remove another product
if "bags" in price_dict:
    price_dict.pop("bags")
print("After removing products:", price_dict)
# Calculate the average price
total = 0
for price in price_dict.values():
    total = total + price
average_price = total / len(price_dict)
print("Average price:", average_price)


# Extra (optional): Print the product with both the maximum and minimum prices.
maximum_price = 0
maximum_product = ""
for product, price in price_dict.items():
    if price > maximum_price:
        maximum_price = price
        maximum_product = product

print("Maximum price product:", maximum_product)
print("Maximum price:", maximum_price)
