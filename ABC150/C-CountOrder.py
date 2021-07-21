import itertools

N = int(input())
Plist = list(map(int,input().split()))
Qlist = list(map(int,input().split()))

anslist = [i for i in range(1,N+1)]
temp1 =0
temp2 = 0
it = 0
for v in itertools.permutations(anslist):
  #print (v)
  if list(v) ==Plist:
    temp1= it
  if list(v) ==Qlist:
    temp2 = it
  it +=1

print (abs(temp1-temp2))