function solution(n, computers) {
  const rep = new Array(n).fill().map((_, i) => i);
  const level = new Array(n).fill(0);

  function find(v) {
    while (v !== rep[v]) {
      v = rep[v];
    }

    return v;
  }

  function union(a, b) {
    const aRep = find(a);
    const bRep = find(b);

    if (level[aRep] > level[bRep]) {
      rep[bRep] = aRep;
    } else if (level[bRep] > level[aRep]) {
      rep[aRep] = bRep;
    } else {
      rep[bRep] = aRep;
      level[aRep]++;
    }
  }

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (i === j) continue;

      if (computers[i][j] === 1) union(i, j);
    }
  }

  const uniqueReps = new Set();

  for (let i = 0; i < n; i++) {
    uniqueReps.add(find(i));
  }

  return uniqueReps.size;
}
