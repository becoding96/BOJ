/*
1. 100% 채우는데 걸리는 일수를 저장한 배열 ex) 1번의 경우 [7, 3, 9]
2. 해당 배열의 맨 앞(기준)부터 기준일 초과의 데이터가 나올 때까지 카운트
3. 카운트를 결과 배열에 저장
4. 2 ~ 4번 반복
*/

function solution(progresses, speeds) {
  const answer = [];
  const required = [];

  for (let i = 0; i < progresses.length; i++) {
    if ((100 - progresses[i]) % speeds[i] == 0)
      required.push((100 - progresses[i]) / speeds[i]);
    else required.push(Math.ceil((100 - progresses[i]) / speeds[i]));
  }

  let head = 0; // 배열의 맨 앞을 가리키는 인덱스

  while (head < required.length) {
    let flag = false;

    for (let i = head + 1; i < required.length; i++) {
      if (required[i] > required[head]) {
        answer.push(i - head);
        head = i;
        flag = true;
        break;
      }
    }

    // 배열의 맨 앞보다 많이 걸리는 작업이 안나온 경우
    if (!flag) {
      answer.push(required.length - head);
      break;
    }
  }

  return answer;
}
