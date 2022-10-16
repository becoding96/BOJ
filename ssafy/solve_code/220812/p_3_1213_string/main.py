import sys

sys.stdin = open('input.txt', encoding="UTF-8")

# 0.14612s
def BruteForce(pattern, source):
    cnt = 0
    for idx in range(len(source) - len(pattern) + 1):  # pattern의 길이만큼 슬라이딩 윈도우를 만들어 source를 순회
        for j in range(len(pattern)):                  # pattern과 윈도우의 문자열을 비교
            if source[idx + j] != pattern[j]:
                break
        else:
            cnt += 1
    return cnt

for _ in range(10):
    T = int(input())
    pattern = input()
    source = input()
    print(f'#{T} {BruteForce(pattern, source)}')