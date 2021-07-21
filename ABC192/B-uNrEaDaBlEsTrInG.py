S = input()
for i in range(len(S)):
  #print (S[i])
  if (i+1)%2==0 and S[i].islower() ==True:
    print ('No')
    quit()
    
  elif (i)%2==0 and S[i].isupper() ==True:
    print ('No')
    quit()
    
print ('Yes')