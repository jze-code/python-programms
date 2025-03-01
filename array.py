import array as arr
array_num= arr.array('i',[1,3,5,3,7,9,3])
print("original array:"+str(array_num))
print("number of occurences of the number 3 is"+str(array_num.count(3)))
array_num.reverse()
print("the array in the reverse array is")
print(str(array_num))