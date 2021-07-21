# ABC179
# 問題文
# 高橋君は、「サイコロを2個振る」という行動をN回行いました。 i回目の出目は Di,1,Di,2です。
# ゾロ目が 3回以上続けて出たことがあるかどうか判定してください。 より正確には、Di,1=Di,2かつDi+1,1=Di+1,2かつDi+2,1=Di+2,2を満たすようなiが少なくとも一つ存在するかどうか判定してください。


N = int(input())
count = 0
for i in range(N):
  one,two = map(int,input().split())
  if one==two:
    count+=1
  else:
    count =0
  if count ==3:
    break
if count ==3:
  print ('Yes')
else :
  print ('No')