def binary_search(arr, x, n):
    lo = 0
    hi = n - 1
    mid = 0

    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] < x:
            lo = mid + 1
        elif arr[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

import bisect
N,M = map(int,input().split())
Slist = list(map(str,input().split()))
Tlist = list(map(str,input().split()))
ans =[]
d ={}
for i in range(N):
  d[Slist[i]]=i
  ans.append(i)
#print (d)
di={}
search=[]
for j in range(M):
  di[Tlist[j]]=d[Tlist[j]]
  search.append(d[Tlist[j]])
#print (di)
for i in range(N):
  if binary_search(search, ans[i] ,len(search))!=-1:
    print ("Yes")
  else:
    print ("No")