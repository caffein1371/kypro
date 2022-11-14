##########################################
import io
import sys

_INPUT = """\
0 0
1 0
1 1
0 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################

xy = []
for i in range(4):
    x,y= map(int,input().split())
    xy.append([x,y])

import itertools
import numpy as np


def degree(a, b, c):

    # ベクトルを定義
    vec_a = a - b
    vec_c = c - b

    # コサインの計算
    length_vec_a = np.linalg.norm(vec_a)
    length_vec_c = np.linalg.norm(vec_c)
    inner_product = np.inner(vec_a, vec_c)
    cos = inner_product / (length_vec_a * length_vec_c)

    # 角度（ラジアン）の計算
    rad = np.arccos(cos)

    # 弧度法から度数法（rad ➔ 度）への変換
    degree = np.rad2deg(rad)

    return degree

for v in itertools.combinations(xy,3):
    print (V)
