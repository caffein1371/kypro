A,B =map(int,input().split())
S = input()
if S.count('-')>2:
  print ('No')
  quit()

if '-' in S:
  a,b = S.split('-')
  if len(a)==A and len(b)==B:
    print ('Yes')
    quit()
  else:
    print ('No')
    quit()
else:
  print ('No')