##create a simple package(shop_package)
#inside folder shop_package/, creat:

#discount.py
#1 apply_discount(price,percent)->returns discounted price
def apply_discount(price, percent):
    discounted_price = price * percent/100
    return discounted_price

#2 flat_discount(price)->always subtracts 50 from price
def flat_discount(price):
    return (price-50)


    