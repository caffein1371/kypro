# ABC169
# 問題文
# A×Bの小数点以下を切り捨て、結果を整数として出力してください。




from decimal import Decimal

A,B = input().split()

A = int(A)
B = Decimal(B)
#print (A)
#print (B)

print (int(A*B))