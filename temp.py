##########################################
import io
import sys

_INPUT = """\
xyz
abc



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
O = input()
E = input()
temp = max(len(O),len(E))
ans = []
for i in range(temp):
    try:
        ans.append(O[i])
    except:
        pass
    try:
        ans.append(E[i])
    except:
        pass

print ("".join(ans))