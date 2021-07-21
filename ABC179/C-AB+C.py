N = int(input())

#https://drken1215.hatenablog.com/entry/2020/09/21/070100
#https://qiita.com/acannie/items/d9859b8ce61a69c2b9f3

count = 0
#A,Bが決まればCは一択
#Bの数は(N-1)/Aで求められる
for i in range(1,N):
  count +=(N-1)//i
    
print (count)