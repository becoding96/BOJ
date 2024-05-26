function solution(dirs) {
  let answer = 0;
  const cur = [0, 0];
  const visited = new Set([]);

  for (let i = 0; i < dirs.length; i++) {
    const dir = dirs[i];
    const tmp = [cur[0], cur[1]];

    if (dir === "U") {
      if (cur[1] + 1 > 5) continue;
      cur[1] += 1;
    } else if (dir === "D") {
      if (cur[1] - 1 < -5) continue;
      cur[1] -= 1;
    } else if (dir === "R") {
      if (cur[0] + 1 > 5) continue;
      cur[0] += 1;
    } else if (dir === "L") {
      if (cur[0] - 1 < -5) continue;
      cur[0] -= 1;
    }

    const path1 = `${tmp[0]}${tmp[1]}${cur[0]}${cur[1]}`;
    const path2 = `${cur[0]}${cur[1]}${tmp[0]}${tmp[1]}`; // 반대로 가는 경우도 길을 지난 것이므로

    if (!visited.has(path1) && !visited.has(path2)) {
      visited.add(path1);
      visited.add(path2);
      answer += 1;
    }
  }

  return answer;
}
