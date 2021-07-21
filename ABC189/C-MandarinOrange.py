#pythonでは時間内に解けず

N = int(input())
Alist = list(map(int,input().split()))

#lを固定し，rを増やながら，xを更新する
#O(N**2)で解ける
ans = 0
for l,now in enumerate(Alist):
  #lを固定
  x = now
  for r in range(l,N):
    #区間最小値を選ぶ
    x = min(x,Alist[r])
    #lからrまでの区間最小値の和を求め，値が大きければ更新
    ans = max(ans,x*((r-l)+1))
    
print (ans)
