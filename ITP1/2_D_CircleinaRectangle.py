# 長方形の中の円
# 長方形の中に円が含まれるかを判定するプログラムを作成してください。次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 
# (W,H)が与えられます。また、円はその中心の座標 (x,y)と半径rで与えられます。

W,H,x,y,r = map(int,input().split())

if x>=r and y>=r and x+r<=W and y+r<=H:
    print ('Yes')
else:
    print ('No')