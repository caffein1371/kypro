#フィボナッチ数列
#フィボナッチ数列の第 n 項の値を出力するプログラムを作成してください。ここではフィボナッチ数列を以下の再帰的な式で定義します：

from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n):
    if n==1 or n==0:
        return 1
    return fib4(n-1)+fib4(n-2)

X= int(input())  
fib4=fib4(X)
print(fib4)