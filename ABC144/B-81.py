N = int(input())

ansflag = False
for i in range(1,10):
  if N%i==0:
    if N/i<10:
      ansflag = True
      break
    
if ansflag ==True:
  print ('Yes')
else:
  print ('No')