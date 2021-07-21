s = input()
n = len(s)

ans = 0

for bit in range(1 << (n - 1)):
    f = s[0]

    for i in range(n - 1):
        # ここのif文の判定基準が理解できていません。
        # ビット bit の i 番目のフラグ（１）が立っているかどうか
        # bitに1番目が１
        # bitに2番目が１か？
        #if bit & (1 << i):
        if (bit>>i) &1:
          #１が立っていた場合
            f += "+"
        f += s[i + 1]
        
    print (f)
    ans += sum(map(int, f.split("+")))

print(ans)