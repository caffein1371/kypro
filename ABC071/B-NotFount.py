S = input()
S = sorted(list(set(S)))
alpha = [chr(i) for i in range(97, 97+26)]
for i in range(len(alpha)):
  if alpha[i] not in S:
    print (alpha[i])
    quit()
print ('None')