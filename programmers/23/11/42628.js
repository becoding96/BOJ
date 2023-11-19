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

  heapMaxPop() {
    if (this.isEmpty()) return;

    const findStartIndex = Math.floor((this.heap.length - 1) / 2) + 1;
    let maxValue = this.heap[findStartIndex];
    let maxIndex = findStartIndex;

    for (let i = findStartIndex + 1; i <= this.heap.length - 1; i++) {
      if (this.heap[i] > maxValue) {
        maxValue = this.heap[i];
        maxIndex = i;
      }
    }

    this._swap(maxIndex, this.heap.length - 1);

    return this.heap.pop();
  }

  getResult() {
    if (this.isEmpty()) return [0, 0];

    const minValue = this.heap[1];

    if (this.heap.length === 2) return [minValue, minValue];

    const findStartIndex = Math.floor((this.heap.length - 1) / 2) + 1;
    const maxValue = Math.max(...this.heap.slice(findStartIndex));

    return [maxValue, minValue];
  }

  isEmpty() {
    return this.heap.length === 1;
  }

  _swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
}

function solution(operations) {
  const minHeap = new Heap();

  for (const oper of operations) {
    const [order, data] = oper.split(" ");

    if (order === "I") minHeap.heappush(Number(data));
    else {
      if (data === "1") minHeap.heapMaxPop();
      else minHeap.heappop();
    }
  }

  return minHeap.getResult();
}
