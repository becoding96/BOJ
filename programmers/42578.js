/*
n번째 종류의 개수를 Cn이라 하면
[(1 + Cn)들의 곱셈의 합 - 1]을 출력하면 된다.
=> 해당 종류에서 하나도 안고르는 경우 1개 + Cn개 중에 하나를 뽑는 경우의 수 Cn
=> 그 것들의 곱을 더하고 아무것도 고르지않는 경우 1을 뺀다.
*/

function solution(clothes) {
  const typeCnt = {};
  let result = 1;

  clothes.forEach((cloth) => {
    if (cloth[1] in typeCnt) typeCnt[cloth[1]] += 1;
    else typeCnt[cloth[1]] = 1;
  });

  Object.keys(typeCnt).forEach((type) => {
    result *= typeCnt[type] + 1;
  });

  return result - 1;
}
