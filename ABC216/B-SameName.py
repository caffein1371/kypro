N = int(input())
STlist = []
for i in range(N):
  ST =input()
  STlist.append(ST)
  
STlist = sorted(STlist)
for i in range(N-1):
  if STlist[i]==STlist[i+1]:
    print ("Yes")
    quit()
    
print ("No")