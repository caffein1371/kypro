a = int(input())
b = int(input())
ans = 0
while True:
 if (ans+a)%b==0:
   break
 ans+=1
print (ans)