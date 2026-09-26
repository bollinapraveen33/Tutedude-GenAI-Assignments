## main.py, import this module in two different ways:
#testing all functions 
# - import math_utils

import math_utils 
print("added vlaue:",math_utils.add(1,2))
print("subtracted value:",math_utils.subtract(4,5))
print("squared vlaue:",math_utils.square(4))

#-from math_utils import square
from math_utils import square
print("squared vlaue:",square(4))

##importing the string_utis.py and testing all functions 
from string_utils import *
print("capitalize_words:",capitalize_words('praveen'))
print("reverse_string",reverse_string('praveen'))
print("word_count:",word_count('praveen'))

#task->4 importing the package in main.py
#in main.py do the following 
#1->import shop_package.discount as disc
#2->from shop_package.billing import calculate_total
import shop_package.discount as disc
from shop_package.billing import calculate_total,apply_tax

#3->call every function inside the package
#example usage:

#first i am calling all the discount functions 
print("after applying the discount:",disc.apply_discount(1000,10))
print("after applying the falt_discount:",disc.flat_discount(1000))

#second i am calling all the billing functions
print("after calculating the total:",calculate_total([100,200,300]))
print("after applying the tax:",apply_tax(100))

