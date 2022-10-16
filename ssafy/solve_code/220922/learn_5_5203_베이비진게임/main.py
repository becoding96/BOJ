import sys
sys.stdin = open("input.txt")

def is_win(arr):
    if any(arr[i] >= 3 for i in range(10)):
        return True
    if any(arr[i - 1] and arr[i] and arr[i + 1] for i in range(1, 9)):
        return True
    return False

for T in range(int(input())):
    cards = list(map(int, input().split()))
    A_cards, B_cards = [cards[i] for i in range(0, 11, 2)], [cards[i] for i in range(1, 12, 2)]
    A, B = [0] * 10, [0] * 10
    result = 0
    for i in range(6):
        A[A_cards[i]] += 1
        if is_win(A):
            result = 1
            break
        B[B_cards[i]] += 1
        if is_win(B):
            result = 2
            break
    print(f'#{T + 1} {result}')
