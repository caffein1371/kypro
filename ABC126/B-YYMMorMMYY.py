S = input()
if (int(S[0:2])<13)and (int(S[0:2])>0) and (int(S[2:4])<13)and (int(S[2:4])>0):
  print ("AMBIGUOUS")
elif ((int(S[0:2])>13) or (int(S[0:2])==0)) and ((int(S[2:4])>13)or (int(S[2:4])==0)):
  print ("NA")
elif (int(S[0:2])<13)and (int(S[0:2])>0):
  print ("MMYY")
elif (int(S[2:4])<13)and (int(S[2:4])>0):
  print ("YYMM")