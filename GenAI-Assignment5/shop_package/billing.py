#billing.py
#functions:
#1->calculate_total(price)->return total bill(sum of all price)
def calculate_total(price):
    total_bill=0
    for i in price:
        total_bill +=i
    return total_bill

#2->apply_tax(amount) -> add 5% tax

def apply_tax(amount):
    tax_amount = 0
    final_price = 0
    tax_amount = amount * 5/100
    final_price = amount - tax_amount
    return final_price
    