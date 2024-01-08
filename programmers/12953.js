/**
제일 큰 수에 곱하는 수를 늘려가면서
곱한 값이 작은 값들에 의해 나눠 떨어지는지 확인한다.
**/

function solution(arr) {
  const max = arr[arr.length - 1];
  let K = 1;

  while (true) {
    let checked = arr.length - 1;

    for (let i = 0; i < arr.length - 1; i++) {
      if ((max * K) % arr[i] === 0) {
        checked -= 1;
      }
    }

    if (checked === 0) {
      return max * K;
    }

    K += 1;
  }
}
