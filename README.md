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

## Heap 구현

```js
class Heap {
  constructor() {
    this.heap = [null];
  }

  heappush(value) {
    this.heap.push(value);
    let curIdx = this.heap.length - 1;
    let parIdx = Math.floor(curIdx / 2);

    while (this.heap.length >= 2 && this.heap[curIdx] < this.heap[parIdx]) {
      if (this.heap[parIdx] === null) return;

      [this.heap[parIdx], this.heap[curIdx]] = [
        this.heap[curIdx],
        this.heap[parIdx],
      ];

      curIdx = parIdx;
      parIdx = Math.floor(curIdx / 2);
    }
  }

  heappop() {
    const min = this.heap[1];
    if (this.heap.length <= 2) this.heap = [null];
    else this.heap[1] = this.heap.pop();

    let curIdx = 1;
    let leftIdx = curIdx * 2;
    let rightIdx = curIdx * 2 + 1;

    // 왼쪽 자식이 없으면 루트만 있는 상태
    if (!this.heap[leftIdx]) return min;
    // 오른쪽 자식이 없으면 왼쪽 자식 하나만 있는 상태
    if (!this.heap[rightIdx] && this.heap[curIdx] > this.heap[leftIdx]) {
      [this.heap[curIdx], this.heap[leftIdx]] = [
        this.heap[leftIdx],
        this.heap[curIdx],
      ];

      return min;
    }

    while (
      this.heap[curIdx] > this.heap[leftIdx] ||
      this.heap[curIdx] > this.heap[rightIdx]
    ) {
      const lowerIdx =
        this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;

      [this.heap[curIdx], this.heap[lowerIdx]] = [
        this.heap[lowerIdx],
        this.heap[curIdx],
      ];

      curIdx = lowerIdx;
      leftIdx = curIdx * 2;
      rightIdx = curIdx * 2 + 1;
    }

    return min;
  }
}

/** 기존의 배열을 Heap으로 */
function heapify(arr) {
  const heapArr = new Heap();

  arr.map((item) => heapArr.heappush(item));

  return heapArr;
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
