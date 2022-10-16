import sys
sys.stdin = open("input.txt")

for T in range(int(input())):
    str = input()

    # 방법 1
    print(f'{T + 1} {str[::-1]}')

    # # 방법 2
    # s = 0
    # e = len(str) - 1
    # str_list = list(str)
    # while s < e:
    #     str_list[s], str_list[e] = str_list[e], str_list[s]
    #     s += 1
    #     e -= 1
    # print(f'{T + 1} {"".join(str_list)}')

    # # 방법 3
    # result = ''
    # str_list = list(str)
    # for i in range(len(str_list)):
    #     result += str_list.pop(-1)
    # print(f'{T + 1} {result}')


