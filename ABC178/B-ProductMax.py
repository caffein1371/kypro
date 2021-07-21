# ABC178
# 問題文
# 整数 a,b,c,dが与えられます。 a≤x≤b,c≤y≤dを満たす整数x,yについて、x×yの最大値はいくつですか。


a,b,c,d = map(int,input().split())

anslist = []
anslist.append(a*c)
anslist.append(a*d)
anslist.append(b*c)
anslist.append(b*d)

print (max(anslist))