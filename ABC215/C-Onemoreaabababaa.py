S,K = map(str,input().split())
ans = 0
import itertools
for v in sorted(list(set(itertools.permutations(S,len(S))))):
  if ans==int(K)-1:
    print ("".join(v))
    break
  ans+=1