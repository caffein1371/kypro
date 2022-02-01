L,R = map(int,input().split())
S = input()
temp = S[L-1:R][::-1]
print (S[:L-1]+temp+S[R:])