N,M = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
for i in range(M):
  try:
    Alist.remove(Blist[i])
  except:
    print ("No")
    quit()
print ("Yes")