# 220821
import sys

input = sys.stdin.readline
N = int(input().rstrip())
words = list(set([input().rstrip() for _ in range(N)]))
words.sort(key=lambda x: (x[0], len(x)))    # 첫 글자를 1순위, 글자의 길이를 2순위로 정렬
result = N = len(words)                     # 중복된걸 제거한 후에 N 갱신

for i in range(N):
    cur = words[i]
    for j in range(i + 1, N):
        if cur[0] == words[j][0]:           # 첫 글자가 같을 때만 검사
            if cur == words[j][:len(cur)]:
                result -= 1
                break
        else:                               # 같지 않으면 더 이상 볼 필요 없으므로 break, 시간 줄이기 용
            break

print(result)
