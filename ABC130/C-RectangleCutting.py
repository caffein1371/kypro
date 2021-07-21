W,H,x,y = map(int,input().split())
ans = H*W/2
count = 0
#(x,y)と(W/2,H/2)を通る直線が存在すれば良い
#中心を通れば，二等分できる
if x== W/2 and y==H/2:
  count +=1

print ('{} {}'.format(ans,count))