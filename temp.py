##########################################
import io
import sys

_INPUT = """\
4 2


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
temp =10**9
ans = K
a = [1 for i in range(10**6)]
a[K] = K
s = [1 for i in range(10**6)]
for i in range(0,N):
    s[i+1]=a[i]+s[i]
print (s[0:10])
print (a[0:10])

for i in range(K,N+1):
    a[i]=s[i]-s[i-K]
    s[i+1]=(s[i]+a[i])%temp

print (a[N])