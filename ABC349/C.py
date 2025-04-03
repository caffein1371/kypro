##########################################
import io
import sys

_INPUT = """\
narita
NRT

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def is_airport_code(S, T):
    # Sから長さ3の部分列を生成して候補とする
    for i in range(len(S) - 2):
        for j in range(i+1, len(S) - 1):
            for k in range(j+1, len(S)):
                candidate = S[i].upper() + S[j].upper() + S[k].upper()  # 部分列を大文字に変換
                if candidate == T:
                    return True

    # Sから長さ2の部分列を生成し、末尾にXを追加して候補とする
    for i in range(len(S) - 1):
        for j in range(i+1, len(S)):
            candidate = S[i].upper() + S[j].upper() + 'X'  # 部分列を大文字に変換し、末尾にXを追加
            if candidate == T:
                return True

    return False
# テストケース
S = input().strip()
T = input().strip()
if is_airport_code(S, T):
    print("Yes")
else:
    print("No")
