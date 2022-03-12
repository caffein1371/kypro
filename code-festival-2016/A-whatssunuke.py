H,W=map(int,input().split())
snuke ="snuke"
ans =[]
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(H):
  ans =list(map(str,input().split()))
  if snuke in ans:
    print (alpha[ans.index(snuke)]+str(i+1))