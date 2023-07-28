import java.util.*;

class Solution {
    public int solution(String[] maps) {
        int answer = 0;
        int row = maps.length, col = maps[0].length();
        int[][] visited = new int[row][col];
        int[] di = {1, 0, -1, 0};
        int[] dj = {0, 1, 0, -1};
        boolean leverFound = false;
        
        Queue<int[]> q = new LinkedList<>();
        
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {                
                if (maps[i].charAt(j) == 'S') {
                    q.offer(new int[] {i, j, 0});
                    visited[i][j] = 1;
                    break;
                }
            }
        }
        
        // BFS
        while (q.size() > 0) {
            int[] cur = q.poll();
            int i = cur[0];
            int j = cur[1];
            int level = cur[2];
            
            // 레버 찾았을 때
            if (maps[i].charAt(j) == 'L') {
                leverFound = true;
                q.clear();
                visited = new int[row][col];
                visited[i][j] = 1;
            }
            
            // 출구 찾았을 때
            if (leverFound && maps[i].charAt(j) == 'E') {
                return level;
            }
            
            // 4방향 탐색
            for (int k = 0; k < 4; k++) {
                int ni = i + di[k];
                int nj = j + dj[k];
                
                if (ni >= 0 && nj >= 0 && ni < row && nj < col && maps[ni].charAt(nj) != 'X' && visited[ni][nj] == 0) {
                    q.offer(new int[] {ni, nj, level + 1});
                    visited[ni][nj] = 1;
                }
            }
        }
        
        return -1;
    }
}