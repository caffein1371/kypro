N,X = map(int,input().split())
Vlist =[]
Plist =[]

for i in range(N):
  V,P = map(int,input().split())
  Vlist.append(V)
  Plist.append(P)
ans = 0
count =0
for i in range(N):
  count+=1
  ans += Vlist[i]*Plist[i]
  #print (ans)
  if ans>X*100:
    print (count)
    exit()

print (-1)