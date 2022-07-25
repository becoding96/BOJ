# 220712
def grouped(w):
    w = [w[i] for i in range(len(w)) if i == 0 or w[i - 1] != w[i]]
    return len(set(w)) == len(w)

print(sum(map(grouped, [input() for i in range(int(input()))])))