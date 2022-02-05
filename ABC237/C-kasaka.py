S = list(input())
length = len(S)
i = 0
x = 0
for i in range(len(S)):
  if S[i]=="a":
    x+=1
  else:
    break
#print (x)
#print (S)
re_S = S[::-1]
y=0
for i in range(len(S)):
  if re_S[i]=="a":
    y+=1
  else:
    break
#print (y)
del S[0:x]
re_S = S[::-1]
del re_S[0:y]
#print (S)
#print (re_S)
if x<=y and re_S==re_S[::-1]:
  print ("Yes")
else:
  print ("No")
