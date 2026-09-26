# Task 5: Loop Control with Conditions (break & continue)

'''1->Given a list of daily sales: daily = [200, 150, 0, 400, 50, -1, 300], 
iterate through it with a for loop and:'''

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sales in daily:

    '''If a day's value is -1, treat it as corrupted data and break the loop (stop processing).
    If a day's value is 0, treat it as a day with no sales and continue (skip adding to revenue).
    For valid positive sales, add to total_sales and print the running total.'''
    if sales == -1:
        print("Corrupted data found:", sales)
        break

    elif sales == 0:
        print("No sales for this day.")
        continue

    else:
        total_sales = total_sales + sales
        print("Running total:", total_sales)


'''2->Print the final total after the loop completes (or stops due to corrupted data).'''
print("Final total sales:", total_sales)
