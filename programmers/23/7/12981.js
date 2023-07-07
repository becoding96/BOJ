function solution(n, words) {
  const used = new Set([words[0]]); // 말했던 단어, 첫 단어 넣어놓고 시작

  /** 아래에서 i + 1은 몇 번째 턴인지 의미한다. **/
  for (i = 1; i < words.length; i++) {
    if (
      words[i - 1][words[i - 1].length - 1] !== words[i][0] ||
      used.has(words[i])
    ) {
      return [
        (i + 1) % n === 0 ? n : (i + 1) % n,
        (i + 1) % n === 0
          ? Math.floor((i + 1) / n)
          : Math.floor((i + 1) / n) + 1,
      ];
    }

    used.add(words[i]);
  }

  return [0, 0];
}
