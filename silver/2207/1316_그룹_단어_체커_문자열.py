# 220712
n = int(input())
answer = n

for i in range(n):
    ch = [0 for _ in range(26)] # a ~ z: 97 ~ 122
    word = input()
    for j in range(len(word)):
        if j >= 1 and word[j] != word[j - 1] and ch[ord(word[j]) - 97]:
            answer -= 1
            break
        ch[ord(word[j]) - 97] = 1 # 1 = True, 해당 line이 if문보다 먼저 나오면 안됨

print(answer)