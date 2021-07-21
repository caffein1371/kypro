data = []
for i in range(3):
  temp = list(map(int,input().split()))
  data.append(temp)
#a1,a2,a3,b1,b2,b3 = 0
for a1 in range(101):
    b1 = data[0][0]-a1
    b2 = data[0][1]-a1
    b3 = data[0][2]-a1
    if b1>=0 and b2>=0 and b3>=0 and b1<=100 and b2<=100 and b3<=100:
      a2 = data[1][1]-b2
      a3 = data[2][2]-b3
      if a2>=0 and a3>=0 and a2<=100 and a3<=100 and data[1][2]==a2+b3 and data[2][1]==a3+b2 and data[1][0]==a2+b1 and data[2][0]==a3+b1:
        #print ('{} {} {} {} {} {}'.format(a1,a2,a3,b1,b2,b3))
        print ('Yes')
        quit()
      else:
        continue
    else:
      continue
print ('No')