package boj.gold.java1759;

import java.io.*;
import java.util.*;

public class Main {
    static int l, c;
    static String[] arr;
    static HashSet<String> vowelSet = new HashSet<>(Arrays.asList("a", "e", "i", "o", "u"));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String tmp = br.readLine();
        StringTokenizer st = new StringTokenizer(tmp);
        l = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        tmp = br.readLine();
        st = new StringTokenizer(tmp);
        arr = new String[c];
        for (int i = 0; i < c; i++) {
            arr[i] = st.nextToken();
        }

        Arrays.sort(arr);

        comb(0, 0, "", 0, 0);

        br.close();
        bw.flush();
        bw.close();
    }

    static void comb(int start, int cnt, String res, int voCnt, int coCnt) throws IOException {
        if (cnt == l) {
            if (voCnt >= 1 && coCnt >= 2) {
                bw.write(res);
                bw.newLine();
            }

            return;
        }

        for (int i = start; i < c; i++) {
            if (vowelSet.contains(arr[i])) {
                comb(i + 1, cnt + 1, res + arr[i], voCnt + 1, coCnt);
            } else {
                comb(i + 1, cnt + 1, res + arr[i], voCnt, coCnt + 1);
            }
        }
    }
}
