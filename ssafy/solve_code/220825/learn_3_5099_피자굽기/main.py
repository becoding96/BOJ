import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    num_arr = [i + 1 for i in range(M)]
    arr = list(zip(num_arr, arr))
    cheese, arr = arr[:N], arr[N:]

    while True:
        if cheese and cheese[0][1] // 2 == 0:
            cheese.pop(0)
            if arr:
                cheese.insert(0, arr.pop(0))
            if len(cheese) == 1:                    # 해당 if문 보다 arr에서 가져오는게 먼저
                print(f'#{T + 1} {cheese[0][0]}')
                break
        elif cheese:
            tmp = cheese.pop(0)
            cheese.append((tmp[0], tmp[1] // 2))