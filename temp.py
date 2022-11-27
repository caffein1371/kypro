##########################################
import io
import sys

_INPUT = """\
10 1



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from math import sqrt


A, B = map(int, input().split())

L, R = 0, (A + B - 1) // B

while L + 1 < R:
    M = (L + R) // 2
    condition_0 = A * A > B * B * M * (M + 1) * (2 * M + 1)
    condition_1 = A ** 4 + B ** 4 * M * M * (M + 1) * (M + 1) > 2 * A * A * B * B * M * (M + 1) * (2 * M + 1)
    if condition_0 and condition_1:
        L = M
    else:
        R = M

print(A / sqrt(L + 1) + B * L)
