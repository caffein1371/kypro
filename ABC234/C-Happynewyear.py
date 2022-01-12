K=int(input())
ans=''
while K>=1:
  if K%2==1:
    ans+='1'
  elif K%2==0:
    ans+='0'
  K=K//2
  
print (int(ans[::-1])*2)  