import sys
sys.stdin = open('input.txt')

# 126ms
for T in range(int(input())):
    str1 = input()
    str2 = input()
    d = {}

    for s in str1:
        d[s] = 0          # str1에 있는 문자를 key로 딕셔너리 초기화

    for s in str2:
        try:
            d[s] += 1
        except:           # 딕셔너리에 s 키가 없을 경우를 대비
            continue

    print(f'#{T + 1} {max(list(d.values()))}')