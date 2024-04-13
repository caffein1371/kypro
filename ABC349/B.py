##########################################
import io
import sys

_INPUT = """\
ab


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def is_good_string(s):
    # 文字の出現回数をカウントする辞書を作成
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # 出現回数がi回の文字が1種類以上あるかどうかを確認
    for i in range(1, len(s) + 1):
        count_of_i = sum(1 for count in char_count.values() if count == i)
        if count_of_i not in (0, 2):
            return False
    
    return True

# テスト用の文字列Sを指定して判定します
S = input()
result = is_good_string(S)
if result:
    print ("Yes")
else:
    print ("No")