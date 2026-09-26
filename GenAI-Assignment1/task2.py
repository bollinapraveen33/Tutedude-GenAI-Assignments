# Task 2: Categories (Sets)

'''1->From your products list, create a set of categories called categories_set. 
(If product names do not contain categories, create a short parallel list categories = [...] with matching length and use that.)'''

products = ["phone", "laptop", "headphones", "smartwatch", "shoes", "bags"]
categories = [
    "Electronics",
    "Electronics",
    "Electronics",
    "Electronics",
    "Footwear",
    "Bags & Accessories"
]
categories_set = set(categories)

# 2->Demonstrate adding a new category to the set and show that duplicates are ignored.
categories_set.add("Fashion")
print("Categories:", categories_set)

# 3->Show how to check whether a category exists in the set (print a boolean result).
print("Electronics exists:", "Electronics" in categories_set)
print("Footwear exists:", "Footwear" in categories_set)
print("Fashion exists:", "Fashion" in categories_set)

# Extra (optional): Show how to get the total number of unique categories using a set.
print("Number of unique categories:", len(categories_set))
