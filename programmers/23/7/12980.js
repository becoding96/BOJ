/**
N을 2로 나눌 수 있는지 확인
안되면 - 1
반복
**/

function solution(n) {
  let K = 0;

  while (n !== 0) {
    if (n % 2 === 0) {
      n /= 2;
    } else {
      n -= 1;
      K += 1;
    }
  }

  return K;
}
