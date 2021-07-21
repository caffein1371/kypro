N = int(input())

anslist = [i*111 for i in range(1,10)]
#print (anslist)

for i in anslist:
  if N<=i:
    print (i)
    quit()