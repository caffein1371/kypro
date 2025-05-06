##########################################
import io
import sys

_INPUT = """\
100 0


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,N = map(int,input().split())
plist = list(map(int,input().split()))

templist = [i for i in range(102)]
#print (templist)

for i in range(N):
  templist.remove(plist[i])
#print (templist)

if N==0:
  print (X)
  quit()


diff = 10**7
ans = 10**7

for i in range(len(templist)):
  if diff>abs(X-templist[i]):
    diff = abs(X-templist[i])
    ans = templist[i]
print (ans)