N = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))

#print (Alist)
Alist.reverse()
Blist.reverse()

ans =0
nokori = 0
for i in range(N):
  #print ("{} {}".format(Alist[i],Blist[i]))
  if Alist[i]-Blist[i]>=0:
    ans+=Blist[i]
  else:
    ans+=Alist[i]
    nokori = Blist[i]-Alist[i]
    if nokori>=Alist[i+1]:
      ans+=Alist[i+1]
      Alist[i+1]=0
    else:
      ans+=nokori
      Alist[i+1]=Alist[i+1]-nokori
      
print (ans)