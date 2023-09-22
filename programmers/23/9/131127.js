function solution(want, number, discount) {
  let answer = 0;
  const wantSet = new Set(want); // 할인 품목이 want에 있는지
  const index = {}; // 할인 품목이 want의 몇 번째 인덱스인지
  let cnt = 10; // 매 번 number 배열이 전부 0인지 확인하지 않도록 하는 용도

  // want 원소 index 저장
  for (let i = 0; i < want.length; i++) {
    index[want[i]] = i;
  }

  // discount의 맨 뒤 원소부터
  for (let j = discount.length - 1; j >= 0; j--) {
    // 할인 품목이 want에 있는지
    if (wantSet.has(discount[j])) {
      // 있으면 number에 개수 깎기
      number[index[discount[j]]] -= 1;
      cnt -= 1;
    }

    // 10일 동안만 할인 되니까 10일 이후의 것들은 number 되돌려놓기
    if (j <= discount.length - 11 && wantSet.has(discount[j + 10])) {
      number[index[discount[j + 10]]] += 1;
      cnt += 1;
    }

    // number가 전부 0인지 확인
    if (cnt === 0) {
      if (number.every((item) => item === 0)) {
        answer += 1;
      }
    }
  }

  return answer;
}
