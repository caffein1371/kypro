X = input()
if X[0]==X[1] and X[1]==X[2] and X[2]==X[3] and X[3]==X[0]:
  print ("Weak")
  quit()

if str(int(X[0])+1)[-1]==X[1] and str(int(X[1])+1)[-1]==X[2] and str(int(X[2])+1)[-1]==X[3]:
  print ("Weak")
  quit()
  
print ("Strong")