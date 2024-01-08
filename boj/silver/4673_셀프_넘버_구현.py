# 220710
# 소수 구하기와 비슷함
is_check_list = list(1 for i in range(10001))


def d(num):
    tmp = num
    answer = 0
    while tmp > 0:
        answer += tmp % 10
        tmp //= 10
    return num + answer


def check(num):
    next = d(num) # 매번 계산하지 않게 next에 저장
    if next <= 10000 and is_check_list[next]:
        is_check_list[next] = 0
        check(next)


for i in range(1, len(is_check_list)):
    check(i)

for i in range(1, len(is_check_list)):
    if is_check_list[i]:
        print(i)