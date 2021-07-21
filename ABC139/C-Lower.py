N = int(input())
Hlist = list(map(int,input().split()))

ans = 0
maxnum = 0
for i in range(len(Hlist)-1):
  if Hlist[i+1]<=Hlist[i]:
      #print ('{} {}'.format(Hlist[j],Hlist[j+1]))
      ans+=1
  else:
    ans = 0
  if maxnum<=ans:
    maxnum = ans
  
print (maxnum)