S1 = input()
S2 = input()
S3 = input()
S4 = input()
List = ["H","2B","3B","HR"]
try:
  List.remove(S1)
  List.remove(S2)
  List.remove(S3)
  List.remove(S4)
except:
  pass
if len(List)==0:
  print ("Yes")
else:
  print ("No")