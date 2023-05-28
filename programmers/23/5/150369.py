def solution(cap, n, deliveries, pickups):
    answer = 0
    d_idx, p_idx = n - 1, n - 1

    while d_idx >= 0 or p_idx >= 0:
        d_cap, p_cap = cap, cap
        max_length = 0

        for i in range(d_idx, -1, -1):
            if d_cap == 0:
                break

            if deliveries[i]:
                if deliveries[i] >= d_cap:
                    deliveries[i] -= d_cap
                    d_cap = 0
                else:
                    d_cap -= deliveries[i]
                    deliveries[i] = 0

                max_length = max(max_length, i + 1)

                d_idx = i

        for i in range(p_idx, -1, -1):
            if p_cap == 0:
                break

            if pickups[i]:
                if pickups[i] >= p_cap:
                    pickups[i] -= p_cap
                    p_cap = 0
                else:
                    p_cap -= pickups[i]
                    pickups[i] = 0

                max_length = max(max_length, i + 1)

                p_idx = i

        answer += max_length * 2

        if max_length == 0:
            break

    return answer


print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
