A,B,C = map(int,input().split())
for i in range(1000):
  if A<=C*i and C*i <=B:
    print (C*i)
    quit()
  elif B<C*i:
    print ("-1")
    quit()
    
