h,w = map(int,input().split())
anslist =[]
for i in range(h):
  anslist.append(input())
ue = ['#' for i in range(w+2)]
print (''.join(ue))
for i in range(h):
  print (''.join('#'+anslist[i]+'#'))
print (''.join(ue))