S = input()
Resultkisu = True
Resultgusu = True
for i in range(len(S)):
  if i%2==0:
    #print (S[i])
    if S[i]!='R' and S[i]!='U' and S[i]!='D':
      Resultkisu = False
  else:
    #print (S[i])
    if S[i]!='L' and S[i]!='U' and S[i]!='D':
      Resultgusu = False
      
    
if Resultkisu==True and Resultgusu==True:
  print ('Yes')
else :
  print ('No')