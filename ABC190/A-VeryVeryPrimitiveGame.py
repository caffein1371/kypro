A,B,C =map(int,input().split())
i=0
if C==0:
  i=2
else:
  i=1
while True:
  if i%2==0:
    A-=1
    if A<0:
      print ('Aoki')
      exit()
    
  else:
    B-=1
    if B<0:
      print ('Takahashi')
      exit()
  
  

  i+=1