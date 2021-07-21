N = int(input())
S = input()
#print (S)
temp = S[0:N//2]
#print (temp)

if S == temp+temp :
  print ('Yes')
else:
  print ('No')