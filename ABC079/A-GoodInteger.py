N = input()
  
count = 0
temp = -1
for i in range(len(N)):
  if temp==N[i]:
    count+=1
  else:
    count =0
  if count ==2:
    print ('Yes')
    quit()
  temp =N[i]
    
print ('No')