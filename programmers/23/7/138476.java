import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        // 귤 사이즈 별 개수를 저장
        HashMap<Integer, Integer> count = new HashMap<>();
        
        for (int size : tangerine) {
            if (count.get(size) == null) {
                count.put(size, 1);
            } else {
                count.put(size, count.get(size) + 1);
            }
        }
        
        // 귤 사이즈 리스트, 내림차순으로 정렬
        ArrayList<Integer> sizeList = new ArrayList<>();
        
        for (int size: count.keySet()) {
            sizeList.add(count.get(size));
        }
        
        Collections.sort(sizeList, Collections.reverseOrder());
        
        /*
        사이즈 별 개수가 많은 것들을 먼저 담음
        담은 사이즈 종류 카운트 하기
        담은 귤의 개수가 k보다 같거나 커지면
        사이즈 종류 리턴
        */
        int sum = 0;
        int i = 0;
        
        while (sum < k) {
            answer += 1;
            sum += sizeList.get(i);
            
            i += 1;
        }
        
        return answer;
    }
}