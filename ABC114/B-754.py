S = input()

num = 753
number = []
minnum = 1000
for i,n in enumerate(S):
  number.append(n)
  if i>=2:
    minnum = min(abs(int(''.join(number))-num),minnum)
    number.pop(0)
    
print (minnum)