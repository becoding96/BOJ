## 부분 집합

[subset](ssafy/subset/subset.py)

<br>

## 병합 정렬

[merge_sort](ssafy/sort/merge.py)

[better_merge_sort](ssafy/sort/better_merge.py)

<br>

## 퀵 정렬

[quick_sort](ssafy/sort/quick.py)

<br>

## 순열, 조합

[combination](ssafy/permutation%2C%20combination/combination_SSAFY.py)

[permutation](ssafy/permutation%2C%20combination/permutation_SSAFY.py)

<br>

## 프림 알고리즘

[prim](ssafy/graph/prim.py)

<br>

## 크루스칼 알고리즘

[kruskal](ssafy/graph/kruskal.py)

<br>

## 다익스트라 알고리즘

[dijkstra](ssafy/graph/dijkstra.py)

<br>

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

<br>

## set 연산자 시간복잡도

- 합집합(union): O(N + M)  

- 교집합(intersection): O(N + M)  

- 차집합(difference): O(N + M)  

- in
    - list에서 in 연산의 평균 시간 복잡도: O(N)
    - set에서 in 연산의 평균 시간 복잡도: O(1)  
    