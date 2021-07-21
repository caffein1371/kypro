w = str(input())
n = int(input())
for i in range(n):
  a = str(input()).split()
  if a[0]=='replace':
    #print (w[0:int(a[1])])
    #print (a[3])
    temp = w
    w = w[0:int(a[1])]+a[3]+w[int(a[2])+1:len(w)]
    #print (w)
  elif a[0]=='print':
    print (w[int(a[1]):int(a[2])+1])
  elif a[0]=='reverse':
    temp = w[int(a[1]):int(a[2])+1]
    #print (temp)
    temp = temp[::-1]
    #print (temp)
    w = w[0:int(a[1])]+temp+w[int(a[2])+1:len(w)]
    #print (w)
    