A,B = map(int,input().split())
rule = [2,3,4,5,6,7,8,9,10,11,12,13,1]
if rule.index(A)<rule.index(B):
  print ('Bob')
elif rule.index(A)>rule.index(B):
  print ('Alice')
else:
  print ('Draw')
