N = int(input())

count =0
for i in range(1,N+1):
  if i%2!=0:
    count+=1
    
print ('{:.10f}'.format(count/N))