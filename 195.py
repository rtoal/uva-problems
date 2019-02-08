import sys

# String to array of ints that can be arranged and sorted according to the
# weird rules of the problem. Interleaves uppers and lowers in ASCII letters.
def encoded(s):
    return [c*2 if c<92 else c*2-63 for c in bytes(s, "utf-8")]

# Encoded array back to string
def decoded(a):
    return ''.join(chr(b//2 if b%2==0 else (b+63)//2) for b in a)

# Credit to SO user jfs https://stackoverflow.com/a/34325140/831878
def next_permutation(a):
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break
    else:
        return False
    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

cases = int(sys.stdin.readline())
for _ in range(cases):
    word = sorted(encoded(sys.stdin.readline().strip()))
    while True:
        print(decoded(word))
        if not next_permutation(word):
            break
