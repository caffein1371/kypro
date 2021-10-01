N = int(input())
plist = list(map(int,input().split()))
qlist = [i+1 for i in range(N)]
for i in range(N):
  qlist[plist[i]-1]=i+1
print (*qlist)