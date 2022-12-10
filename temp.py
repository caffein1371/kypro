##########################################
import io
import sys

_INPUT = """\
1 600
130







"""
sys.stdin = io.StringIO(_INPUT)
##########################################

N,T = map(int,input().split())
Alist = list(map(int,input().split()))
temp = [0 for i in range(10**5+1)]
temp[0]=Alist[0]

i = 1
while True:
    temp[i]=((Alist[i%N])+temp[i-1])
    
    #print (temp)
    #time.sleep(3)

    if temp[i]>T:
        if (i+1)%N==0:
            print (N,T-temp[i-1])
        else:
            print ((i+1)%N,T-temp[i-1])
        quit()
    i+=1
    
    