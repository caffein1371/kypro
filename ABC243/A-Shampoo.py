V,A,B,C= map(int,input().split())

while True:
  V = V-A
  if V<0:
    print ("F")
    break
  V=V-B
  if V<0:
    print ("M")
    break
  V=V-C
  if V<0:
    print ("T")
    break