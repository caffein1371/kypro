##########################################
import io
import sys

_INPUT = """\
4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
#AB=XかつCD=N-Xになる(A,B,C,D)の個数をX=1,Nと求める
#AB=Xとなる(A,B)=f(x)とすると
import math
ans=0
for i in range(1,N):
        X=i
        Y=N-i
        x,y=0,0
        
        for j in range(1,int(math.sqrt(X))+1):
                if X%j==0:
                        x+=1
                        if X!=j*j:
                                x+=1

        for j in range(1,int(math.sqrt(Y))+1):
                if Y%j==0:
                        y+=1
                        if Y!=j*j:
                                y+=1
        ans+=x*y
print (ans)