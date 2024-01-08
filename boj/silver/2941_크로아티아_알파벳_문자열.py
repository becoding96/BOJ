#220713
ca_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
answer = len(word)

i = 0 
while i <= len(word) - 2:
    comb1 = word[i] + word[i + 1]
    if i <= len(word) - 3:
        comb2 = word[i] + word[i + 1] + word[i + 2]
    elif i > len(word) - 3:
        comb2 = ''  # 이전 loop에 저장된 comb2 초기화
    for ca in ca_list:
        if comb1 == ca:
            answer -= 1  # 두 글자가 한 글자로 처리되므로
            i += 1
            break
        elif comb2 == ca:
            answer -= 2  # 세 글자가 한 글자로 처리되므로
            i += 2
            break
    i += 1

print(answer)
