function toTime(min) {
  let h = Math.floor(min / 60).toString();
  if (h.length < 2) h = "0" + h;
  let m = (min % 60).toString();
  if (m.length < 2) m = "0" + m;

  return h + ":" + m;
}

function solution(n, t, m, timetable) {
  let crewTimes = timetable
    .map((time) => {
      return Number(time.slice(0, 2)) * 60 + Number(time.slice(3, 5));
    })
    .sort((a, b) => a - b);

  let busTime = 540;
  let crewIndex = 0;

  for (let i = 0; i < n; i++) {
    let passengerCount = 0;

    while (
      passengerCount < m &&
      crewIndex < crewTimes.length &&
      crewTimes[crewIndex] <= busTime
    ) {
      passengerCount++;
      crewIndex++;
    }

    // 마지막 버스
    if (i === n - 1) {
      if (passengerCount < m) {
        return toTime(busTime);
      } else {
        return toTime(crewTimes[crewIndex - 1] - 1);
      }
    }

    busTime += t;
  }

  return toTime(busTime);
}
