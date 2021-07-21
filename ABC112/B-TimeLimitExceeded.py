N,T = map(int,input().split())
ctlist =[]
for i in range(N):
  c,t = map(int,input().split())
  ctlist.append([c,t])
  
anslist = sorted(ctlist, reverse=False, key=lambda x: x[0])  #[1]に注目してソート
for i in range(N):
  if T>=anslist[i][1]:
    print (anslist[i][0])
    quit()
      
print ('TLE')
  