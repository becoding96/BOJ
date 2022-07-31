## 220731
import sys

input = sys.stdin.readline
n = int(input())
cur = []
for c in input().rstrip():
    cur.append(int(c))
pur = []
for c in input().rstrip():
    pur.append(int(c))

result = []

# 1. 첫 스위치를 누를 때
cur_o = cur[:]
count_o = 1
cur_o[0] = not cur_o[0]
cur_o[1] = not cur_o[1]

# n - 2 스위치까지
for i in range(1, n - 1):
    if cur_o[i - 1] != pur[i - 1]:
        count_o += 1
        cur_o[i - 1] = not cur_o[i - 1]
        cur_o[i] = not cur_o[i]
        cur_o[i + 1] = not cur_o[i + 1]

# n - 1 스위치
if cur_o[n - 2] != pur[n - 2]:
    count_o += 1
    cur_o[n - 2] = not cur_o[n - 2]
    cur_o[n - 1] = not cur_o[n - 1]

# 마지막 전구가 같으면 결과 리스트에 추가
if cur_o[n - 1] == pur[n - 1]:
    result.append(count_o)

# 2. 첫 스위치를 안 누를 때
cur_x = cur[:]
count_x = 0

# n - 2 스위치까지
for i in range(1, n - 1):
    if cur_x[i - 1] != pur[i - 1]:
        count_x += 1
        cur_x[i - 1] = not cur_x[i - 1]
        cur_x[i] = not cur_x[i]
        cur_x[i + 1] = not cur_x[i + 1]

# n - 1 스위치
if cur_x[n - 2] != pur[n - 2]:
    count_x += 1
    cur_x[n - 2] = not cur_x[n - 2]
    cur_x[n - 1] = not cur_x[n - 1]

# 마지막 전구가 같으면 결과 리스트에 추가
if cur_x[n - 1] == pur[n - 1]:
    result.append(count_x)

if result == []:
    print(-1)
else:
    print(min(result))

'''
1. 첫 번째 스위치는 누른다 or 안누른다 선택지 두 개 뿐이다.
첫 번째 스위치에 대한 결정이 정해졌을 때 그 뒤의 스위치는 강제로 정해진다.
둘 중에 스위치 누른 횟수 최소값을 구하면 그것은 최적해이다.
따라서 그리디로 풀 수 있다.

2. 첫 번째 스위치를 누른다. (현재 인덱스를 i라고 표현함)
두 번째 스위치(i = 1)부터 i - 1의 전구 상태가 목표 상태와 다르면 누른다.
맨 마지막 n - 1까지 가서도 n - 2위치의 전구가 서로 다른지 판단하고 누른다.
그러면 n - 2 인덱스 까지는 전구가 무조건 같다.
n - 1번 전구가 같냐 다르냐가 중요하다, 같으면 카운트를 저장

3. 첫 번째 스위치를 안누른다.
과정 동일
'''
