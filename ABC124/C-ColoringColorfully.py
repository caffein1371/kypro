import numpy as np
S =input()
sample1 = [0 if i % 2 == 0 else 1 for i in range(len(S))]
sample2 = [1 if i % 2 == 0 else 0 for i in range(len(S))]
S = [int(i) for i in S]
test = np.array(S)
sample1np = np.array(sample1)
sample2np = np.array(sample2)
ans1 = abs(test-sample1np)
ans2 = abs(test-sample2np)
print (min(sum(ans1),sum(ans2)))