n,k = map(int,input().split())
ans = [i*100+j for i in range(1,n+1) for j in range(1,k+1)]
print (sum(ans))