# 二分探索
# n 個の整数を含む数列 S と、q 個の異なる整数を含む数列 T を読み込み、T に含まれる整数の中で S に含まれるものの個数 C を出力するプログラムを作成してください。

def binary_search(list,item):
  low =0
  high = len(list)-1
  while low<=high:
    mid = (low+high)//2
    guess = list[mid]
    if guess == item:
      return mid
    if guess>item:
      high = mid-1
    else:
      low = mid+1
  return None

n= int(input())
nlist= list(map(int,input().split()))
q= int(input())
tlist= list(map(int,input().split()))

count =0
for i in range(q):
  if binary_search(nlist,tlist[i])!=None:
    count+=1
  
print (count)