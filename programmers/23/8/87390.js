function solution(n, left, right) {
  const answer = [];

  for (let row = 1; row <= n; row++) {
    for (let col = 1; col <= n; col++) {
      answer.push(Math.max(row, col));
    }
  }

  return answer.slice(left, right + 1);
}
