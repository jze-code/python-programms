l=[2,4,1,9]
print("original list:",l)
sum=0
for nums in l:
    sum=sum+nums
print("the addition of elements",sum)
avg=sum/len(l)
print("the average of the elements is",avg)
l.sort()
print("sorted list is",l)