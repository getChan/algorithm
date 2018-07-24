import sys

src = sys.stdin.readline().rstrip()
dst = "".join(chr(i-3) if i>67 else chr(i+23) for i in map(ord, src))

print(dst)