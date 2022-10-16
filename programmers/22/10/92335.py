# 221015
def to_k_notation(n, k):
    if n == k:
        return '10'
    elif n < k:
        return str(n)
    return to_k_notation(n // k, k) + str(n % k)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    visited = {}  # 메모이제이션 용도, 다시 소수 판별 안해도 되도록
    
    for prime_cand in to_k_notation(n, k).split('0'):
        if prime_cand:
            pc = int(prime_cand)
            try:
                if visited[pc]:
                    answer += 1
            except:
                if is_prime(pc):
                    visited[pc] = 1
                    answer += 1
                else:
                    visited[pc] = 0

    return answer