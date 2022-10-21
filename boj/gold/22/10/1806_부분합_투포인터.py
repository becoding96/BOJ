# 221021
N, S = map(int, input().split())
arr = list(map(int, input().split()))
result = N
cumulated = 0

l = r = 0
cumulated = arr[0]
while r < N - 1:
    if arr[r] >= S:
        print(1)
        exit()
    if cumulated >= S:
        while cumulated - arr[l] >= S:
            cumulated -= arr[l]
            l += 1
        result = r - l + 1 if r - l + 1 < result else result
    r += 1
    cumulated += arr[r]

if cumulated >= S:
    while cumulated - arr[l] >= S:
        cumulated -= arr[l]
        l += 1
    result = r - l + 1 if r - l + 1 < result else result

if sum(arr) < S:
    print(0)
else:
    print(result)
