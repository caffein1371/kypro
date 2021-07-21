N = int(input())
T,A = map(int,input().split())
Hlist =list(map(int,input().split()))

#anslist = []
ans = 0
temp =10**5
for i in range(N):
  #anslist.append(abs(A-(T-Hlist[i]*0.006)))
  if temp>abs(A-(T-Hlist[i]*0.006)):
    temp = abs(A-(T-Hlist[i]*0.006))
    ans = i+1
print (ans)