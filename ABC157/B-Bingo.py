# ABC157
# 問題文
# 3×3のサイズのビンゴカードがあります。上から i行目、左からj列目の数は Ai,jです。
# 続けて、 N個の数b1,b2,⋯,bNが選ばれます。選ばれた数がビンゴカードの中にあった場合、ビンゴカードのその数に印を付けます。
# N個の数字が選ばれた時点でビンゴが達成されているか、則ち、縦・横・斜めのいずれか 
# 1列に並んだ3つの数の組であって、全てに印の付いているものが存在するかどうかを判定してください。


A11,A12,A13 = map(int,input().split())
A21,A22,A23 = map(int,input().split())
A31,A32,A33 = map(int,input().split())

Alist = []
Alist.append(A11)
Alist.append(A12)
Alist.append(A13)
Alist.append(A21)
Alist.append(A22)
Alist.append(A23)
Alist.append(A31)
Alist.append(A32)
Alist.append(A33)
bingolist =[0]*9

N = int(input())
#print (N)
for i in range(N):
  b = int(input())
  #print (b)
  for j in range(len(bingolist)):
    if b ==Alist[j]:
      bingolist[j] = 1

if sum(bingolist[0:3])==3 or sum(bingolist[3:6])==3 or sum(bingolist[6:9])==3 or (bingolist[0]+bingolist[3]+bingolist[6])==3 or (bingolist[1]+bingolist[4]+bingolist[7])==3 or (bingolist[2]+bingolist[5]+bingolist[8])==3 or (bingolist[0]+bingolist[4]+bingolist[8])==3 or (bingolist[2]+bingolist[4]+bingolist[6])==3:
  print ("Yes")
else :
  print ("No")
#print (bingolist[0:3])
#print (bingolist[3:6])
#print (bingolist[6:9])
#print (bingolist)