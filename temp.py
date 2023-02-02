##########################################
import io
import sys

_INPUT = """\
10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
alist = list(map(int,input().split()))


res = 0
right = 0 
sume = 0
# Blist = [i for i in range(N)]
# Blist[0]=alist[0]
# for i in range(1,N):
#     Blist[i]=Blist[i-1]+alist[i]

#print (Blist)
for left in range(N):
    #print (left)
    while (right<N and sume<K):
        sume+=alist[right]
        right+=1
    
    #print (sume)
    if K<=sume:
        res+=N-right+1
    if right==left:
        right+=1
    else:
        sume-=alist[left]

    #print (right)
print (res)