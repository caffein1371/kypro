##########################################
import io
import sys

_INPUT = """\
3 1
1 2





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
for i in range(M):
    a,b = map(int,input().split())
    UF.merge(a-1,b-1)

ans = []
for i in range(N):
    #print (UF.leader(i))
    ans.append(UF.leader(i))
ans = set(ans)
#print (ans)


if len(ans)==1:
    print (0)
else:
    print (len(ans)-1)