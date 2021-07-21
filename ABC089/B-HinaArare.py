N = int(input())
anslist = list(map(str,input().split()))
if len(set(anslist))==3:
  print ('Three')
elif len(set(anslist))==4:
  print ('Four')