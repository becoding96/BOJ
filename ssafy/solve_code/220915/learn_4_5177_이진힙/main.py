import sys
sys.stdin = open("input.txt")


def heappush(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


def f(v):
    s = 0
    v //= 2
    while v >= 1:
        s += heap[v]
        v //= 2
    return s


for T in range(int(input())):
    N = int(input())
    last = 0
    heap = [0] * (N + 1)
    arr = list(map(int, input().split()))
    for a in arr:
        heappush(a)
    print(f'#{T + 1} {f(N)}')
