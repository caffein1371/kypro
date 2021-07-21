import re
s = input()
result = re.search(r'A(.+)Z',s)
print (result.end()-result.start())