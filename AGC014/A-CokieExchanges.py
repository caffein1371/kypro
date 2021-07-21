a,b,c = map(int,input().split())
count = 0
while True:
  #print ('a={} b={} c={} '.format(a,b,c))
  if a%2==1 or b%2==1 or c%2==1:
    print (count)
    quit()
  ahenka = a/2
  bhenka = b/2
  chenka = c/2
  #print ('{} {} {} '.format(ahenka,bhenka,chenka))
  a = bhenka + chenka
  b = ahenka + chenka
  c = ahenka + bhenka
  count +=1
  if a==b and b==c and c==a:
    print (-1)
    quit()