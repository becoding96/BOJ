/** 최대값을 낮추는게 중요하다. (제곱 그래프는 접점의 기울기가 점점 증가하기 때문에) */

function solution(n, works) {
  const timeCnt = {};
  let max = 0;

  works.forEach((work) => {
    if (timeCnt[work] === undefined) timeCnt[work] = 1;
    else timeCnt[work] += 1;

    if (max < work) max = work;
  });

  for (let i = max; i > 0; i--) {
    if (timeCnt[i] !== undefined) {
      if (timeCnt[i] < n) {
        n -= timeCnt[i];

        if (timeCnt[i - 1] !== undefined) {
          timeCnt[i - 1] += timeCnt[i];
        } else {
          timeCnt[i - 1] = timeCnt[i];
        }

        timeCnt[i] = 0;
      } else {
        timeCnt[i] -= n;

        if (timeCnt[i - 1] !== undefined) {
          timeCnt[i - 1] += n;
        } else {
          timeCnt[i - 1] = n;
        }

        break;
      }
    }
  }

  return Object.keys(timeCnt).reduce((result, key) => {
    const value = Number(key);
    const cnt = timeCnt[key];

    if (value !== 0 && cnt !== 0) {
      return result + value ** 2 * cnt;
    } else {
      return result;
    }
  }, 0);
}
