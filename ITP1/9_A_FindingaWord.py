w = str(input())
count =0
ans =[]
while True:
  t = input()
  if t=='END_OF_TEXT':
    break
  tlist = list(map(str,t.split()))
  for i in range(len(tlist)):
    ans.append(tlist[i])
#print (ans)
for i in range(len(ans)):
  if ans[i].upper() == w.upper():
    count+=1

print (count)