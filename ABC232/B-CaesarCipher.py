ori = 'abcdefghijklmnopqrstuvwxyz'
d = {}
S = input()
T = input()
for i in range(len(ori)):
  d[ori[i]]=i+1
#print (d)
ans =[]
for i in range(len(S)):
  temp = d[T[i]]-d[S[i]]
  #print (temp)
  if temp<0:
    temp = temp+26
  ans.append(temp)
  #print (ans)
if len(list(set(ans))) ==1:
  print ('Yes')
else:
  print ('No')