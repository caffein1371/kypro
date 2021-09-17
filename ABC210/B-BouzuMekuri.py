N = int(input())
S = input()
for i in range(N):
  if S[i]=="1" and i%2==1:
    print ("Aoki")
    quit()
  elif S[i]=="1" and i%2==0:
    print ("Takahashi")
    quit()