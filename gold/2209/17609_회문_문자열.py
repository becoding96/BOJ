# 220909
import sys


def is_normal_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True

def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l, r = l + 1, r - 1
        else:
            # l과 r 사이 문자가 하나 이상 있을 때
            if l < r - 1:
                # r에 있는 문자 제거
                tmp = s[:r] + s[r + 1:]
                if is_normal_palindrome(tmp):
                    return 1
                # l에 있는 문자 제거
                tmp = s[:l] + s[l + 1:]
                if is_normal_palindrome(tmp):
                    return 1
            return 2
    return 0


input = sys.stdin.readline
for _ in range(int(input().rstrip())):
    s = input().rstrip()
    print(is_palindrome(s))
