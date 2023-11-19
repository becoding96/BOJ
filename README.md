## 소수 판별

```js
function isPrime(n) {
  if (n === 1) return false;

  for (let i = 2; i <= Math.sqrt(n); i++) {
    // 제곱근까지만 탐색
    if (n % i === 0) return false;
  }

  return true;
}
```

<br>

## 최소 Heap 구현

```js
class Heap {
  constructor() {
    this.heap = [null];
  }

  heappush(value) {
    this.heap.push(value);

    let curIndex = this.heap.length - 1;
    let parIndex = Math.floor(curIndex / 2);

    while (parIndex !== 0 && this.heap[curIndex] < this.heap[parIndex]) {
      this._swap(parIndex, curIndex);

      curIndex = parIndex;
      parIndex = Math.floor(curIndex / 2);
    }
  }

  heappop() {
    if (this.isEmpty()) return;
    if (this.heap.length === 2) return this.heap.pop();

    const min = this.heap[1];
    this.heap[1] = this.heap.pop();

    let curIndex = 1,
      leftIndex = 2,
      rightIndex = 3;

    while (
      (this.heap[leftIndex] && this.heap[curIndex] > this.heap[leftIndex]) ||
      (this.heap[rightIndex] && this.heap[curIndex] > this.heap[rightIndex])
    ) {
      if (this.heap[leftIndex] === undefined) {
        this._swap(rightIndex, curIndex);
      } else if (this.heap[rightIndex] === undefined) {
        this._swap(leftIndex, curIndex);
      } else if (this.heap[leftIndex] > this.heap[rightIndex]) {
        this._swap(curIndex, rightIndex);
        curIndex = rightIndex;
      } else if (this.heap[leftIndex] <= this.heap[rightIndex]) {
        this._swap(curIndex, leftIndex);
        curIndex = leftIndex;
      }

      leftIndex = curIndex * 2;
      rightIndex = curIndex * 2 + 1;
    }

    return min;
  }

  isEmpty() {
    return this.heap.length === 1;
  }

  _swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
}
```

<br>

## Union & Find 최적화 코드

```js
function find(item) {
  // rep: 대표 원소 저장 리스트
  while (item !== rep[item]) {
    item = rep[item];
  }

  return item;
}

function union(a, b) {
  aRep = find(a);
  bRep = find(b);

  // rank가 높은 쪽이 대표
  if (rank[aRep] > rank[bRep]) {
    rep[bRep] = aRep;
  } else if (rank[bRep] > rank[aRep]) {
    rep[aRep] = bRep;
  } else {
    // rank가 같으면 아무나 대표, 대표가 된 원소는 rank 1 증가
    rep[bRep] = aRep;
    rank[aRep] += 1;
  }
}
```

<br>

## 순열, 조합

<br>

## 프림 알고리즘

<br>

## 크루스칼 알고리즘

<br>

## 다익스트라 알고리즘
