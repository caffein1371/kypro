X,A,B = map(int,input().split())
if -A+B>X:
  print ('dangerous')
elif -A+B<=0:
  print ('delicious')
elif -A+B>0 and -A+B<=X:
  print ('safe')
