##########################################
import io
import sys

_INPUT = """\
5 2
1 3


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
Alist = list(map(int,input().split()))


if N==1 and M==0:
    print (1)
    quit()
elif N==M:
    print (0)
    quit()
else:
    Alist.append(0)
    Alist.append(N+1)
    Alist = list(sorted(set(Alist)))
    TEMP =[]
    for i in range(len(Alist)-1):
        temp = Alist[i+1]-Alist[i]-1
        #print (temp)
        if temp!=0:
            TEMP.append(temp)
a = min(TEMP)
ans = 0
for i in range(len(TEMP)):
    ans+=-(-TEMP[i]//a)

print (ans)