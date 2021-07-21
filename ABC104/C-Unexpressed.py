S = input()

if S[0]!='A':
  print ('WA')
  quit()
if 'C' not in S[2:-1] :
  print ('WA')
  quit()

cnt = 0
for c in S:
  if c.isupper(): 
    cnt += 1
print("AC" if cnt==2 else "WA")