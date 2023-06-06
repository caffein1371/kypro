##########################################
import io
import sys

_INPUT = """\
4 5
2 -1
3 1
8 8
0 5



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n

    def leader(self,a):
        if self.parent_size[a]<0:
            return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):
            x,y=y,x
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

N,D = map(int,input().split())

p = []

for i in range(N):
    x,y = map(int,input().split())
    p.append([x,y])

UF = UnionFind(N)

for i in range(N):
    for k in range(i+1,N):
        ix,iy = p[i]
        kx,ky = p[k]

        d = (ix-kx)**2+(iy-ky)**2
        if d<=D**2:
            UF.merge(i,k)

for i in range(0,N):
    if UF.same(0,i):
        print ('Yes')
    else:
        print ('No')

        
