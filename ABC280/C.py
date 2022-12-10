N,T = map(int,input().split())
Alist = list(map(int,input().split()))
temp = [0 for i in range((10**5)+1)]
temp[0]=Alist[0]
rem = T%sum(Alist)
sum = 0
for i in range(len(Alist)):
    if sum+Alist[i]>rem:
        print (i+1,rem-sum)
        quit()
    sum+=Alist[i]
