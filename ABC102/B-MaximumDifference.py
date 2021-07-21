N = int(input())
Alist = list(map(int,input().split()))

Alist = sorted(Alist)
print (abs(Alist[0]-Alist[-1]))