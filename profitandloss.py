actual_cost= float(input("please enter the actual product price")) 
sales_amount= float(input("please enter the sales amount"))
if(sales_amount>actual_cost):
    amount= sales_amount-actual_cost
    print(".profit={0}".format(amount))
else: 
    print("you made a loss")