import math
A,B,C,D = map(int,input().split())

ans = 0
def num(n,c,d):
  G = math.gcd(c,d)
  L = c//G*d
  return n-n//c-n//d+n//L
#「A 以上 B 以下の整数のうち〜を満たすものの個数を求めよ」という問題では
#(B 以下の整数のうちの〜を満たすものの個数) から
#(A-1 以下の整数のうちの〜を満たすものの個数) を引く
print (int(num(B,C,D)-num(A-1,C,D)))
#求めたいのはCでもDでも割り切れないもの
#全体ーCで割れるもの＋Dで割れるものーCでもDでも割れるもの