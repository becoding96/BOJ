# 220725
scores = [int(input()) for _ in range(8)]

tmp = scores[:]
tmp.sort(reverse = True)

sum = 0
idx = []
for top_s in tmp[:5]:
    for j in range(8):
        if top_s == scores[j]:
            sum += top_s
            idx.append(j + 1)
idx.sort()

print(sum)
for i in idx:
    print(i, end = ' ')