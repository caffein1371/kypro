X,Y = map(str,input().split())
if int(X,base=16)==int(Y,base=16):
  print ('=')
elif int(X,base=16)>int(Y,base=16):
  print ('>')
else:
  print ('<')