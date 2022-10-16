import sys
sys.stdin = open("input.txt")

for _ in range(10):
    T = int(input())
    queue = list(map(int, input().split()))
    minus = [1, 2, 3, 4, 5]
    i = 0

    while True:
        popped = queue.pop(0) - minus[i]
        if popped <= 0:
            popped = 0
            queue.append(popped)
            break
        else:
            queue.append(popped)
        i = (i + 1) % 5

    print(f'#{T}', end=" ")
    print(*queue)
