a,b,c = map(int,input().split())
k = int(input())
anslist = [a,b,c]
anslist= sorted(anslist)
#print (anslist)

ans = 0
for i in range(k):
  anslist[-1] = anslist[-1]*2
  ans = sum(anslist)

#print (anslist)
print (ans)