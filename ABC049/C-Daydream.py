S = input()

text = ['dream','dreamer','erase','eraser']
newtext = []
for i in range(len(text)):
  newtext.append(text[i][::-1])
#print (newtext)
S= S[::-1]

#print (S)
temp =S
ansflag = False
while len(temp)>4:
  templen = len(temp)
  for i in range(len(text)):
    if temp.startswith(newtext[i])==True:
      temp=temp.replace(newtext[i],'',1)
      #print (temp)
  if len(temp)==0:
    ansflag =True
  if templen==len(temp):
    break
    break
    
if ansflag ==True:
  print ('YES')
else:
  print ('NO')
    
    