def matchwords(words):
    
    ctr=0
    lst=[]

    for word in words:
      if len(words)> 1 and word[0]==word[-1]:
         ctr+=1
         lst.append(word)
    print("list of words with first and last character same\n",lst)
    return ctr
count=matchwords (["abc","cfc","xyz","aba","1221"])
print("number of words having first and last characther same is:",count)


    