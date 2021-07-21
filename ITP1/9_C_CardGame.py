n = int(input())
taro =0
hanako =0
for i in range(n):
  cardlist = list(map(str,input().split()))
  templist = sorted(cardlist)
  if cardlist[0]==cardlist[1]:
    taro+=1
    hanako+=1
  elif cardlist[0]==templist[0]:
    hanako+=3
  else:
    taro+=3
print ("{} {}".format(taro,hanako))
    