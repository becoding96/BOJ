import sys
sys.stdin = open('input.txt')

# 126ms
def BruteForce(pattern, source):
    cnt = 0
    for i in range(len(source) - len(pattern) + 1):
        for j in range(len(pattern)):
            if source[i + j] != pattern[j]:
                break
        else:
            cnt = 1
            break  # 찾으면 더 반복할 필요 없음
    return cnt

for T in range(int(input())):
    str1 = input()
    str2 = input()
    print(f'#{T + 1} {BruteForce(str1, str2)}')