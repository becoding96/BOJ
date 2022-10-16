# 220810
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = set(input().rstrip() for _ in range(n))
b = set(input().rstrip() for _ in range(m))

db = list(d & b)

db.sort()

print(len(db))
for name in db:
    sys.stdout.write(name + '\n')
