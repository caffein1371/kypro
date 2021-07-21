n = input()


ans = []
for i in range(len(n)):
  if n[i] == '9':
    ans.append('1')
  elif n[i] == '1':
    ans.append('9')

answer = ''.join(ans)
print (answer)
