import java.io.*;
import java.util.StringTokenizer;

public class Main2630 {
    static int[][] cp;
    static int[] totalColorCnt = {0, 0};
    static int[] reverse = {1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        cp = new int[n][n];

        for (int i = 0; i < n; i++) {
            String lineString = br.readLine();
            StringTokenizer st = new StringTokenizer(lineString);

            for (int j = 0; j < n; j++) {
                cp[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        solution(n, 0, 0);

        System.out.println(totalColorCnt[0]);
        System.out.println(totalColorCnt[1]);
    }

    static void solution(int n, int x, int y) {
        boolean flag = true;
        int[] colorCnt = {0, 0};

        outer: for (int i = x; i < x + n; i++) {
            for (int j = y; j < y + n; j++) {
                colorCnt[cp[i][j]] += 1;

                if (colorCnt[reverse[cp[i][j]]] > 0) {
                    flag = false;
                    break outer;
                }
            }
        }

        if (flag) {
            totalColorCnt[cp[x + n - 1][y + n - 1]] += 1;
        } else {
            int half = n / 2;
            solution(half, x, y);
            solution(half, x + half, y);
            solution(half, x, y + half);
            solution(half, x + half, y + half);
        }
    }
}