function solution(s) {
  const s1 = s.slice(2, -2).split("},{");

  s1.sort((a, b) => {
    if (a.split(",").length > b.split(",").length) return 1;
    else return -1;
  });

  const result = [];

  s1.forEach((sub) => {
    sub.split(",").forEach((item) => {
      if (!result.includes(Number(item))) {
        result.push(Number(item));
      }
    });
  });

  return result;
}
