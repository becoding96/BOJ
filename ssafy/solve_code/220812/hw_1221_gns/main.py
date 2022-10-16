import sys

sys.stdin = open('input.txt')

# 0.18768s
for T in range(int(input())):
    t, N = input().split()
    N = int(N)
    line = input().split()
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR",
            "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for i in range(10):                        # nums 순회
        for num in line:                       # 입력 문자열 순회
            if nums[i] == num:                 # 정렬 상태의 nums의 첫 번째 원소부터 같은 문자를 문자열에서 찾아 append
                result.append(num)
    print(f'#{T + 1}')
    print(' '.join(result))




