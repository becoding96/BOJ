function canBeChanged(from, to) {
  let cnt = 0;

  for (let i = 0; i < from.length; i++) {
    if (from[i] !== to[i]) cnt++;
    if (cnt > 1) return false;
  }

  return cnt === 1;
}

function solution(begin, target, words) {
  if (!words.includes(target)) return 0;

  const queue = [[begin, 0]];
  const visited = new Set([begin]);

  while (queue.length > 0) {
    const [current, steps] = queue.shift();

    if (current === target) return steps;

    words.forEach((word) => {
      if (!visited.has(word) && canBeChanged(current, word)) {
        visited.add(word);
        queue.push([word, steps + 1]);
      }
    });
  }

  return 0;
}
