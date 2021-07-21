#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

A,B,C = map(int,input().split())

alist = divisor(A)
blist = divisor(B)
anslist = sorted(list(set(alist) & set(blist)),reverse=True)

#print (anslist)

print (anslist[C-1])