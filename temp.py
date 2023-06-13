##########################################
import io
import sys

_INPUT = """\
21
0 20 62 192 284 310 323 324 352 374 409 452 486 512 523 594 677 814 838 946 1000
10
77 721
255 541
478 970
369 466
343 541
42 165
16 618
222 592
730 983
338 747


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
Q = int(input())
temp = [0 for i in range(N+1)]
for i in range(N-1):
    if i%2!=0:
        temp[i+1]=Alist[i+1]-Alist[i]
for i in range(N):
    temp[i+1]+=temp[i]
# print (temp)
# print (Alist)
import bisect

def cal(num):
    ans0 = bisect.bisect_right(Alist,num)
    ans0-=1
    #print (ans0)
    answer = 0
    if ans0<0:
        return answer

    if ans0%2==1:
        answer =num-Alist[ans0]+temp[ans0]
        return answer
    else:
        answer = temp[ans0]
        return  answer
        # return temp[ans0]


for i in range(Q):
    l,r = map(int,input().split())
    # cal(r)
    # cal(l)
    print (cal(r)-cal(l))
