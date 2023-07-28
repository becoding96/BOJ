import java.util.*;

class Solution {
    public int solution(int[] elements) {
        int[] circular = new int[elements.length * 2];
        
        System.arraycopy(elements, 0, circular, 0, elements.length);
        System.arraycopy(elements, 0, circular, elements.length, elements.length);
        
        Set<Integer> set = new HashSet<Integer>();
        
        for (int i = 1; i <= elements.length; i++) {
            for (int j = 0; j <= circular.length - i; j++) {
                int sum = 0;
                
                for (int k = 0; k < i; k++) {
                    sum += circular[j + k];
                }
                
                set.add(sum);
            }
        }
        
        return set.size();
    }
}