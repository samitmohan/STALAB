public class Main {
    public static void main(String[] args) {
        Main c = new Main();
        System.out.println(c.triangle(2,2,2));
    }
    public String triangle(int a, int b, int c) {
        boolean s1 = (a>=1) && (a<=10);
        boolean s2 = (b>=1) && (b<=10);
        boolean s3 = (c>=1) && (c<=10);
        if (!s1)
            return "a not in range";
        if (!s2)
            return "b not in range";
        if (!s3)
            return "c not in range";
        if (a < (b + c) && b < (a + c) && c < (a + b)) {
            if ((a == b) && (b == c)) return "equilateral";
            else if ((a != b) && (b != c) && (c != a)) return "scalene";
            else {
                return "isosceles";
            }
        }
        return "not triangle";
    }
}
