## 소수 판별

```python
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):  # 제곱근까지만 탐색
        if n % i == 0:
            return False
    return True
```

<br>

## Union & Find 최적화 코드

```python
def find(a):
    while a != rep[a]:  # rep: 대표 원소 저장 리스트
        a = rep[a]
    return a


def union(a, b):  # 두 트리의 rank를 비교
    ar = find(a)
    br = find(b)

    if rank[ar] > rank[br]:  # rank가 높은 쪽이 대표가 됨
        rep[br] = ar
    elif rank[br] > rank[ar]:
        rep[ar] = br
    else:  # 같으면 아무나 대표가 되고, 대표가 된 트리는 rank를 1 더해줌
        rep[br] = ar
        rank[ar] += 1
```
