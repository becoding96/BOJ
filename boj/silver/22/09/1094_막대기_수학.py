# 220910
X = int(input())
cnt = 0

for p in [64, 32, 16, 8, 4, 2, 1]:
    if p <= X:
        X -= p
        cnt += 1
        if X == 0:
            break

print(cnt)
