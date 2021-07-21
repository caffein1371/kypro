N,Y = map(int,input().split())
man = -1
gosen = -1
sen = -1

for x in range(0,N+1):
  for y in range(0,N+1-x):
    z = N-x-y
    #print ("{} {} {}".format(x,y,z))
    if z>=0 and x*10000+y*5000+z*1000==Y:
      man =x
      gosen =y
      sen = z
      break
      
print ("{} {} {}".format(man,gosen,sen))