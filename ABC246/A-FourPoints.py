x1,y1= map(int,input().split())
x2,y2= map(int,input().split())
x3,y3= map(int,input().split())

if x1==x2:
  temp1=x3
elif x2==x3:
  temp1=x1
elif x1==x3:
  temp1=x2
  
if y1==y2:
  temp2=y3
elif y2==y3:
  temp2=y1
elif y1==y3:
  temp2=y2
print (str(temp1)+" "+str(temp2))