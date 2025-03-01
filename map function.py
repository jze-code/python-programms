numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("addition of two list")
print(list(result))
num=[1,2,3,4,5,6]
def sq(n):
    return n*n
square=(list(map(sq,num)))
print("sqyare of numbers in list")
print(square)