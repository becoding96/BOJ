# 220717
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    cnt = 0
    sen = input()
    if sen == '#':
        break
    for s in sen:
        if s in vowel:
            cnt += 1
    print(cnt)