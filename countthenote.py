amount=int(input("enter the amount"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of hundred naira",note1)
print("notes of fifty naira",note2)
print("notes of ten naira",note3)