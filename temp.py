##########################################
import io
import sys

_INPUT = """\
5 4
4 2
3 1
5 2
3 2




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import deque

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]  # グラフを表現する隣接リスト
for i in range(M):
    u,v = map(int,input().split())
# 頂点 a から頂点 b への辺を張る
    G[u].append(v)
    # 無向グラフのため、頂点 b から頂点 a への辺も張る
    G[v].append(u)

color = [-1 for _ in range(N+1)]    # color[v]：頂点 v の色が黒なら 1, 白なら 0, 未探索なら -1
ans = 0
# 全ての頂点について
for v in range(N+1):
    # 頂点 v がすでに訪問済みであれば、スキップ
    if color[v] != -1: continue
    # そうでなければ、頂点 v を含む連結成分は未探索
    # 頂点 v の色を白で決め打ちしたうえで、幅優先探索を行う
    deq = deque([]) # 探索候補の頂点番号を入れるキュー
    color[v] = 0
    deq.append(v)
    # キューに要素が残っている限り
    while len(deq) > 0:
        qv = deq.popleft()
        # 頂点 qv に隣接している頂点 nv について、
        for nv in G[qv]:
            # nv がすでに探索済みならば、スキップする
            if color[nv] != -1:
                # 隣り合う頂点どうしが同じ色なら、答えは No
                if color[nv] != color[qv]:
                    ans+=1
                continue
            
            # そうでなければ、頂点 nv の色を color[qv] と逆にしたうえで、nv も探索候補に入れる
            color[nv] = 1 - color[qv]
            #color[nv] = color[qv]
            deq.append(nv)

# 答えを出力する
print(ans)