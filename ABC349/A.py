##########################################
import io
import sys

_INPUT = """\
6
10 20 30 40 50


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def final_score(N, A):
    scores = [0] * N  # 各人の持ち点を初期化

    # A[i] が与えられたとき、それに応じて人Nの持ち点を計算する
    for i in range(N - 1):
        diff = A[i] - scores[i]  # 他の人の持ち点との差分を計算
        scores[i] += diff  # 他の人の持ち点を合わせる
        scores[N - 1] -= diff  # 人Nの持ち点を更新

    return scores[N - 1]

N = int(input())
A = list(map(int,input().split()))
print (final_score(N,A))