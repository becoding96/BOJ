#220710
max = 1000

ch = [1 for i in range(max + 1)]
ch[1] =  0

for i in range(2, max + 1):
    j = 2
    while(i * j <= max):
        ch[i * j] = 0
        j += 1


n = int(input())
nums = list(map(int, input().split()))

answer = 0
for i in range(n):
    if ch[nums[i]]:
        answer += 1

print(answer)