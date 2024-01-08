function solution(n) {
  const way = Array(n + 1);
  way[1] = 1;
  way[2] = 2;

  for (let i = 3; i <= n; i++) {
    way[i] = (way[i - 1] + way[i - 2]) % 1234567;
  }

  return way[n];
}
