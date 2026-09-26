## task -> 2 Process Multiple Orders (for loop)


'''1->Given a list of order amounts: orders = [1200, 2500, 800, 1750, 3000], 
use a for loop to apply the discount rules from Task 1 to each order and print 
a summary table showing: order_amount -> discount% -> final_amount.'''
total_revenue = 0
orders = [1200, 2500, 800, 1750, 3000]
for i in orders:
    if i >= 2000:
        discount = i * 15/100
    
    elif i>=1500 and i<2000:
        discount = i * 10/100
    
    elif i >=1000 and i < 1500:
        discount = i * 7/100
    
    else:
        discount = 0
    print("order_amount:", i)
    print("discount%", discount)

    subtotal = i - discount
    tax = subtotal * 5 / 100
    fianal_amount = subtotal + tax
    print("fianal_amount:", fianal_amount)
    print()
    
    ##2->Also compute and print the total revenue after discounts. 
    total_revenue =total_revenue + fianal_amount
print("total_revenue:", total_revenue)


##Extra (optional): Print the number of orders that received a discount (discount > 0).
no_of_orders = 0
for i in orders:
    if i < 1000:
        pass
    else:
        no_of_orders = no_of_orders + 1
print()

print("no_of_orders that received discount:", no_of_orders)
