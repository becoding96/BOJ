package boj.silver.java17609;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            sb.append(is_palindrome(str, 1) + "\n");
        }

        System.out.println(sb);
    }

    static int is_palindrome(String str, int chance) {
        int l = 0;
        int r = str.length() - 1;

        while (l <= r) {
            if (str.charAt(l) != str.charAt(r)) {
                if (chance == 1 && (is_palindrome(str.substring(l + 1, r + 1), 0) == 1
                        || is_palindrome(str.substring(l, r), 0) == 1)) {
                    return 1;
                } else {
                    return 2;
                }
            }

            l += 1;
            r -= 1;
        }

        if (chance == 0) {
            return 1;
        }

        return 0;
    }
}
