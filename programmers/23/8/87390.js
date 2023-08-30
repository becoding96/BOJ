function solution(n, left, right) {
  const answer = [];

  for (let i = left + 1; i <= right + 1; i++) {
    const q = Math.floor(i / n);
    const r = i % n;

    if (r === 0) {
      answer.push(n);
    } else {
      /**
      몇 번째 행에 속하는 원소인지에 따라 최소값이 정해지는데
      ex) n = 4고, 2번째 행이면 2, 2, 3, 4
      이걸 처음에 2중 for문으로 해결하려 했음 => 실패 이유
      나눔의 몫으로 몇 번째 행인지 알 수 있으므로 몫으로 해결
      **/
      answer.push(Math.max(q + 1, r));
    }
  }

  return answer;
}
