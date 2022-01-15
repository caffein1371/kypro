N = int(input())
Slist = list(map(int,input().split()))
count =0
for s in Slist:
  flag = False
  for a in range(1,1001):
    for b in range(1,1001):
      if s-(4*a*b+3*a+3*b)==0:
        flag = True
        continue
  if not flag:
    count+=1
            
print (count)