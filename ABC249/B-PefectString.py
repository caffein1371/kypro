S =str(input())
S1 = list(set(S))
temp =False
if len(S)==len(S1):
  temp =True

temp1 =False
for i in range(len(S1)):
  if S1[i].isupper():
    temp1 = True
temp2 = False
for i in range(len(S1)):
  if S1[i].islower():
    temp2 = True
    
if temp and temp1 and temp2:
  print ("Yes")
else:
  print ("No")