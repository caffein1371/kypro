N=int(input())
T=input()
way = 0
ans1 =0
ans2 =0
for i in range(N):
  if way==0 and T[i]=="S":
    ans1+=1
  elif way==1 and T[i]=="S":
    ans2-=1
  elif way==2 and T[i]=="S":
    ans1-=1
  elif way==3 and T[i]=="S":
    ans2+=1
  elif T[i]=="R" and way==0:
    way=1
  elif T[i]=="R" and way==1:
    way=2
  elif T[i]=="R" and way==2:
    way=3
  elif T[i]=="R" and way==3:
    way=0
    
print (str(ans1)+" "+str(ans2))
    