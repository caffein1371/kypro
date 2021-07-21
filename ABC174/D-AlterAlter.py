# ABC174
# 問題文
# 祭壇に、左から右へと一列に並ぶ N個の石が祀られています。左から i個目 (1≤i≤N)の石の色は文字 ciとして与えられ、ciが R のとき赤、W のとき白です。
# あなたは、以下の二種の操作を任意の順に何度でも行うことができます。
# 石を 2個選び (隣り合っていなくてもよい)、それらを入れ替える。石を 1個選び、その石の色を変える (赤なら白に、白なら赤に)。
# 占い師によると、赤い石の左隣に置かれた白い石は災いを招きます。そのような白い石がない状態に至るには、最小で何回の操作が必要でしょうか。

#import re

N = input()
stones = input()
#pattern = 'W.*R'
#stoneslist =list(stones)
#result = re.search(pattern,stones)
#if result:
 # print (result.start())
  #print (result.end())
#print(stones[result.start()])
#stoneslist[result.start()]='R'
#stoneslist[result.end()-1]='W'

count =0
#while 'WR' in stones:
 # if stones.count('WR')>1:
  #  stoneslist =list(stones)
   # result = re.search(pattern,stones)
    #stoneslist[result.start()]='R'
    #stoneslist[result.end()-1]='W'
    #stones =str(stoneslist)
    #stones = "".join(stoneslist)
  #else:
   # stones = stones.replace('WR','RR',1)
  #count+=1
  #print(stones)

#print (stones)

red = 0
white = 0
for i in range(len(stones)):
  if stones[i] == "R":
    red +=1
for i in range(red):
  if stones[i] =='W':
    white+=1
print (white)
#print (count)