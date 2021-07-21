N = int(input())
ans = 0
iter = 1 
while True:
    ans +=iter
    if ans>=N:
        print (iter)
        quit()
    iter+=1