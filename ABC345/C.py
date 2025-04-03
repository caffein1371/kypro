##########################################
import io
import sys

_INPUT = """\
abc

"""
sys.stdin = io.StringIO(_INPUT)
##########################################

import math

def count_possible_strings(S):
    N = len(S)
    char_count = {}
    
    # 文字列の各文字の出現回数を数える
    for char in S:
        char_count[char] = char_count.get(char, 0) + 1
    
    # 各文字の出現回数の階乗を計算し、それらを全て掛け合わせる
    permutations = 1
    for count in char_count.values():
        permutations *= math.factorial(count)
    
    # 重複した順列の数を割り、重複を避ける
    result = math.factorial(N) // permutations
    return result
# テスト用の文字列
S = input()
print(count_possible_strings(S))  # 結果を出力