# Task 1: Product Collections (Lists & Tuples)

# 1. Create a list named products containing at least 6 product names (strings).
products = ["phone", "laptop", "headphones", "smartwatch", "shoes", "bags"]

# 2.Create a tuple named sample_product that stores (product_name, price, category) for one product.
sample_product = ("phone", 15000, "Electronics")

# 3. Print the 2nd and last product from the products list.
print("Second product:", products[1])
print("Last product:", products[-1])

# 4. Append two new product names to products and then print the updated list.
products.append("mouse")
products.append("keyboard")
print("Updated product list:", products)

# Extra (optional): Convert sample_product into a list, change its price, and convert it back to a tuple.
sample_product = list(sample_product)
sample_product[1] = 20000
sample_product = tuple(sample_product)

print("Updated sample product:", sample_product)
