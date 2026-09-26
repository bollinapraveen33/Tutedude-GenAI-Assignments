# Task 1: Discount Rules (if / elif / else)

# 1->Write a program that reads an integer order_amount from the user using input().
order_amount = input("Enter the order amount: ")


'''3->Ensure you convert input to a number and handle the case when the input is 
non-numeric by displaying an error message and exiting the program.'''
if order_amount.isdigit():
    order_amount = int(order_amount)
    
 
    '''2->Apply the following discount rules and print the final amount:
    order_amount >= 2000 → 15% discount
    1500 <= order_amount < 2000 → 10% discount
    1000 <= order_amount < 1500 → 7% discount
    otherwise → 0% discount'''
    if order_amount >= 2000:
        discount = order_amount * 15 / 100
    elif order_amount >= 1500:
        discount = order_amount * 10 / 100
    elif order_amount >= 1000:
        discount = order_amount * 7 / 100
    else:
        discount = 0


    '''Extra (optional): Add tax (fixed 5%) after discount and print subtotal, tax, 
    and final total (still within conditionals and basic arithmetic).'''
    subtotal = order_amount - discount
    tax = subtotal * 5 / 100
    final_total = subtotal + tax

    print("Order amount:", order_amount)
    print("Discount:", discount)
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Final total:", final_total)

else: 
    print("Error: Please enter a valid number.")
