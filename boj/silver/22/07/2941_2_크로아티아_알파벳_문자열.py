# 220713

# 백준 기준 실행 시간은 기존 풀이보다 오히려 오래 걸림..
# list에서 'z='가 무조건 'dz='보다 뒤에 와야함
# 'dz='안에 'z='가 포함되어있기 때문

ca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] 
word = input()

for i in ca :
    word = word.replace(i, ' ')

print(len(word))