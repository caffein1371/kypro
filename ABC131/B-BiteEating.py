N,L = map(int,input().split())
aji = [0 for i in range(N)]
for i in range(N):
  aji[i] = L+i+1-1

#print (aji)
zettaichi = [abs(i) for i in aji]
temp = zettaichi.index(min(zettaichi))
del aji[temp]
print (sum(aji))