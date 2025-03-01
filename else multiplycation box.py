try:
    num,num2= eval(input("enter two numbers,sperated by a comma"))
    result=num/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by zero is an error:")
except SyntaxError:
    print("comma is missing,enter numbers seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will execute no matter what")

