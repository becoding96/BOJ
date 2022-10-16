import sys
sys.stdin = open("sample_input.txt")


def partition(l, r):
    pivot = arr[l]
    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def qsort(l, r):
    if l < r:
        s = partition(l, r)
        qsort(l, s - 1)
        qsort(s + 1, r)


for T in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort(0, N - 1)
    print(f'#{T + 1} {arr[N // 2]}')
