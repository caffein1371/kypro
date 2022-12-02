W,a,b = map(int,input().split())

if a<b:
    if a+W>b:
        print (0)
    elif a+W<=b:
        print (b-(a+W))
else :
    if b+W>a:
        print (0)
    elif b+W<=a:
        print (a-(b+W))