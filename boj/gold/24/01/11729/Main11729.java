import java.io.*;

public class Main11729 {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        sb.append((int) (Math.pow(2, n) - 1) + "\n");
        solution(n, '1', '2', '3');
        System.out.println(sb);
    }

    static void solution(int n, char from, char tmp, char to) {
        if (n == 1) {
            sb.append(from + " " + to + "\n");
        } else {
            solution(n - 1, from, to, tmp);
            sb.append(from + " " + to + "\n");
            solution(n - 1, tmp, from, to);
        }
    }
}