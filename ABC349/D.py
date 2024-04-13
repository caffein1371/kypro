##########################################
import io
import sys

_INPUT = """\
0 1024



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def find_good_sequences(L, R):
    good_sequences = []
    i = 0
    while True:
        start = 2 ** i
        end = 2 ** (i + 1)
        if start >= R:
            break
        good_sequences.append((max(start, L), min(end, R)))
        i += 1
    return good_sequences

def main():
    L, R = map(int, input().split())
    good_sequences = find_good_sequences(L, R)
    print(len(good_sequences))
    for sequence in good_sequences:
        print(sequence[0], sequence[1])

if __name__ == "__main__":
    main()
