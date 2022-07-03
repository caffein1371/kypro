K=int(input())
if 9<K and K<60:
  print("21:"+str(K))
elif K<10:
  print("21:0"+str(K))
elif 59<K and K<70:
  print("22:0"+str(K-60))
elif 69<K:
  print("22:"+str(K-60))