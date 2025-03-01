try:
    number=int(input("enter an number"))
    print("the number enter is",number)
except ValueError as ex:
    print("exception:",ex)