N = int(input())
count = 0
for i in range(1,N+1):
  yakucount = 0
  for j in range(1,i+1):
    if i%j==0 and j%2==1:
      yakucount+=1
      #print (yakucount)
  if yakucount ==8:
    count+=1
print (count)