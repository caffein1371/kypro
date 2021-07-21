def is_kaibun(kaibun):
    for i in range(len(kaibun)//2):
        if kaibun[i] != kaibun[-i-1]:
            return False
    return True
ans =0
A,B =map(int,input().split())
for i in range(A,B+1):
  if is_kaibun(str(i)):
    ans+=1
print (ans)