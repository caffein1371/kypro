N = int(input())
S = input()
x =0
temp = 0
for i in range(len(S)):
  if S[i]=='I':
    temp+=1
  elif S[i]=='D':
    temp-=1
  if x< temp:
    x = temp
print (x)