l = list(map(int,input().split()))
for i in range(1,11):
  if l.count(i)==1 or l.count(i)==3:
    print (i)
    break