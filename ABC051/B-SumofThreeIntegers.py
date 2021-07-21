K,S =map(int,input().split())

count =0
for x in range(0,K+1):
  for y in range(0,K+1):
    z = S-x-y
    #print ('{} {} {}'.format(x,y,z))
    if z<=K and z>=0:
      count+=1
        
print (count)
