/* 한 글자만 다른지도 판별하고, 멀어지는 지도 판별한다.*/
function canBeChanged(from, to, target) {
  let cnt = 0;
  let fromTargetCnt = 0;
  let toTargetCnt = 0;

  for (let i = 0; i < from.length; i++) {
    if (from[i] === to[i]) cnt++;
    if (from[i] === target[i]) fromTargetCnt++;
    if (to[i] === target[i]) toTargetCnt++;
  }

  if (cnt !== from.length - 1 || fromTargetCnt > toTargetCnt) return false;

  return true;
}

function solution(begin, target, words) {
  let answer = words.length + 1;
  const visited = new Array(words.length).fill(0);

  function dfs(cur, cnt) {
    if (cnt > words.length) return;

    if (cur === target && cnt < answer) {
      answer = cnt;
      return;
    }

    words.forEach((word, i) => {
      if (canBeChanged(cur, word, target) && visited[i] === 0) {
        visited[i] = 1;
        dfs(word, cnt + 1);
        visited[i] = 0;
      }
    });
  }

  dfs(begin, 0);

  return answer === words.length + 1 ? 0 : answer;
}
