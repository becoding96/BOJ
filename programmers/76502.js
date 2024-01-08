function isCorrect(str) {
  const stack = [];

  for (let i = 0; i < str.length; i++) {
    switch (str[i]) {
      case "(":
        stack.push("(");
        break;
      case ")":
        if (stack && stack[stack.length - 1] === "(") {
          stack.pop();
        } else {
          // 현재 문자가 ')'일 때 스택의 마지막 원소가 '('이 아니면 바로 false 리턴
          return false;
        }
        break;
      case "{":
        stack.push("{");
        break;
      case "}":
        if (stack && stack[stack.length - 1] === "{") {
          stack.pop();
        } else {
          return false;
        }
        break;
      case "[":
        stack.push("[");
        break;
      case "]":
        if (stack && stack[stack.length - 1] === "[") {
          stack.pop();
        } else {
          return false;
        }
        break;
    }
  }

  if (stack.length === 0) {
    return true;
  }

  return false;
}

function solution(s) {
  if (s.length % 2 !== 0) {
    return 0;
  }

  let answer = isCorrect(s) ? 1 : 0;

  for (let i = 1; i < s.length; i++) {
    s = s.substr(1, s.length) + s[0];

    if (isCorrect(s)) {
      answer += 1;
    }
  }

  return answer;
}
