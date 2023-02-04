##########################################
import io
import sys

_INPUT = """\
5 3
1 2
1 3
2 3




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
 
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
 
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 
 
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
 
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
 
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

N,M = map(int,input().split())

UF = UnionFind(N)
ans = 0
temp = 0
hasloop = False
for i in range(M):
    A,B = map(int,input().split())
    if UF.leader(A-1)==UF.leader(B-1):
        hasloop = True

    if hasloop:
        temp+=1
        hasloop = False
    UF.merge(A-1,B-1)


# for i in range(N+1):
#     for j in range(i+1,N):
#         print (i,j)
#         if UF.leader(i)==UF.leader(j):
#             ans+=1

print (temp)
#print (min(temp,M-temp))
# print (ans)