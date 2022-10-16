import sys

sys.stdin = open("input.txt")

for t in range(int(input())):
    k, n, m = map(int, input().split())
    st = list(map(int, input().split()))
    charged = [0]  # 마지막 원소가 현재 위치임을 나타내는 리스트
    flag = False  # 다음 충전 정류장이 멀어서 도달할 수 없는지 확인하는 변수

    # 현재 위치에서 k만큼 갔을 때 종착점을 넘으면 반복문 종료
    while charged[-1] + k < n:
        tmp = 0  # 현재 위치를 정하기 위한 변수

        for s in st:
            if s <= charged[-1]:  # 이미 지나갔거나 도착했던 정류장 continue
                continue
            lim = charged[-1] + k  # 현재 위치 + k가 갈 수 있는 최대 위치
            if s <= lim:  # 정류장 위치가 최대 위치보다 같거나 작으면 tmp에 저장
                tmp = s
            else:  # 정류장 위치가 최대 위치보다 크면 break
                break

        # 다음 충전 정류장이 charged[-1] + k보다 커서 도달할 수 없으면
        # tmp는 값이 변하지 않고 그대로 0이므로
        if tmp == 0:
            flag = True  # 도달할 수 없음
            break

        # tmp가 0이 아니라면 charged에 위치를 저장
        charged.append(tmp)

    if flag:  # 도달할 수 없다면
        print(f'#{t + 1} 0')
    else:
        print(f'#{t + 1} {len(charged) - 1}')