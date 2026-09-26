## task -> 3 User Menu (while loop + break/continue)


## 1->Implement a simple while-loop driven menu that keeps asking the user to choose an action until they press q to quit.
i=1
orders = [1200, 2500, 800, 1750, 3000]
while i>0:


    '''Menu options:
    1 Add order amount to a running list (use input())
    2 Show all orders and totals after applying discounts
    q Quit'''

    options = input("enter the option:")
    if options == "1":
        price = int(input("enter the price you want to add:"))
        orders.append(price)
        print("price is added to list")

    if options == "2":
        print(orders)
        ## printing the totals after applying discount 
        ## i am taking the discount 10% for every order
        ## i am taking the empty list to store the all totals
        lists =[]
        for i in orders:
            discount = i * 10/100
            subtotal = i - discount
            ## tax -> i am taking the tax 5%
            tax = subtotal * 5/100
            total = subtotal + tax
            lists.append(total)

        ## printing the totals after applying the discount 
        print(lists)
    if options == "q":
        break



''' i am doing the 2nd one separately kindly understand '''
''' 2 -> use continue to re-show the menu after invalid input and break to
exit on q'''

i=1
orders = [1200, 2500, 800, 1750, 3000]
while i>0:
    options = input("enter the option:")
    if options == "1":
        price = int(input("enter the price you want to add:"))
        orders.append(price)
        print("price is added to list")
    elif options == "2":
        print(orders)
        lists =[]
        for i in orders:
            discount = i * 10/100
            subtotal = i - discount
            tax = subtotal * 5/100
            total = subtotal + tax
            lists.append(total)
        print(lists)
    else:
        continue
    if options == "q":
        continue