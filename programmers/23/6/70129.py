def solution(s):
    cnt = 0
    zero_cnt = 0

    while s != '1' and cnt <= 5:
        cnt += 1
        zero_cnt += len(s)
        s = s.replace('0', '')
        zero_cnt -= len(s)
        s = bin(len(s))[2:]

    answer = [cnt, zero_cnt]

    return answer


print(solution("110010101001"))