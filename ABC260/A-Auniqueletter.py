import collections

S= input()
c = collections.Counter(S)
for k,v in c.items(): 
  if v==1:
    print (k)
    quit()

print (-1)