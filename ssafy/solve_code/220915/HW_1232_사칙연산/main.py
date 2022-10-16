import sys
sys.stdin = open("input.txt")


def postfix(v):
    if dic[v][0] == '+':
        return postfix(dic[v][1]) + postfix(dic[v][2])
    elif dic[v][0] == '-':
        return postfix(dic[v][1]) - postfix(dic[v][2])
    elif dic[v][0] == '*':
        return postfix(dic[v][1]) * postfix(dic[v][2])
    elif dic[v][0] == '/':
        return postfix(dic[v][1]) / postfix(dic[v][2])
    else:
        return dic[v][0]


for T in range(10):
    N = int(input())
    dic = {(i + 1): [] for i in range(N)}
    for _ in range(N):
        p, *data = input().split()
        p = int(p)
        if data[0].isdecimal():
            dic[p].append(int(data[0]))
        else:
            dic[p].append(data[0])
            dic[p].append(int(data[1]))
            dic[p].append(int(data[2]))
    print(f'#{T + 1} {int(postfix(1))}')
