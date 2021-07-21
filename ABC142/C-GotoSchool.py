N = int(input())
Alist = list(map(int,input().split()))

number = [i for i in range(1,N+1)]

d = dict(zip(Alist, number))

for i in range(1,len(number)+1):
  if i==number:
    print (d[i],end ='')
  else:
    print (d[i],end =' ')