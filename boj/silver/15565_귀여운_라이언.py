# 221109
N, K = map(int, input().split())
dolls = list(map(int, input().split()))
l = r = 0
result = N
cnt = 1 if dolls[0] == 1 else 0

while r + 1 < N:
    r += 1
    if dolls[r] == 1:
        cnt += 1
    while cnt >= K:
        result = min(r - l + 1, result)
        if dolls[l] == 1:
            cnt -= 1
        l += 1

result = -1 if result == N else result

print(result)