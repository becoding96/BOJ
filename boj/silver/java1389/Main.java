package boj.silver.java1389;

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] link;
    static int kb = Integer.MAX_VALUE;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        StringTokenizer st = new StringTokenizer(tmp);
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        link = new int[N][N];

        for (int i = 0; i < M; i++) {
            tmp = br.readLine();
            st = new StringTokenizer(tmp);
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            link[A - 1][B - 1] = 1;
            link[B - 1][A - 1] = 1;
        }

        br.close();

        for (int i = 0; i < N; i++) {
            if (bfs(i) < kb) {
                kb = bfs(i);
                answer = i + 1;
            }
        }

        System.out.print(answer);
    }

    static int bfs(int startNode) {
        Queue<Integer[]> queue = new LinkedList<>();
        Integer[] start = {startNode, 0};
        queue.offer(start);
        int[] check = new int[N];
        check[startNode] = 1;
        int sum = 0;

        while (!queue.isEmpty()) {
            Integer[] cur = queue.poll();
            int curV = cur[0];
            int curLevel = cur[1];

            for (int i = 0; i < N; i++) {
                if (check[i] != 1 && link[curV][i] == 1) {
                    sum += curLevel + 1;

                    Integer[] next = {i, curLevel + 1};
                    queue.offer(next);
                    check[i] = 1;
                }
            }
        }

        return sum;
    }
}