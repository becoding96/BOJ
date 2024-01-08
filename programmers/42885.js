/**
1. 남은 사람 중 가장 무거운 사람을 보트에 탑승 시킨다.
2. 남은 사람 중 가장 가벼운 사람을 동승시킬 수 있는지 확인한다.
**/

function solution(people, limit) {
  let answer = 0;

  people.sort((a, b) => a - b);

  while (people.length > 0) {
    const heaviest = people.pop();

    if (people[0] + heaviest <= limit) {
      people.shift();
    }

    answer++;
  }

  return answer;
}
