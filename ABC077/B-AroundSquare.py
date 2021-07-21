N = int(input())
iter = 1
while True:
  if N<iter**2:
    break
  iter+=1
print ((iter-1)**2)