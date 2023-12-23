// Add build files -> junit from build path
package Q8;

class Test {
    public static String triangle(int a, int b, int c) {
        // constraints: 1-10
        boolean side1 = (a >= 1) && (a <= 10);
        boolean side2 = (b >= 1) && (b <= 10);
        boolean side3 = (c >= 1) && (c <= 10);

        if (!side1) {
            System.out.println("a is not in range");
        }
        if (!side2) {
            System.out.println("b is not in range");
        }
        if (!side3) {
            System.out.println("c is not in range");
        }

        if (side1 && side2 && side3) {
            if (a < (b + c) && b < (a + c) && c < (a + b)) { // triangle
                if ((a == b) && (b == c)) {
                    System.out.println("equilateral");
                } else if ((a != b) && (b != c) && (c != a)) {
                    System.out.println("scalene");
                } else {
                    System.out.println("isoceles");
                }
            } else {
                System.out.println("Triangle cannot be formed");
            }
        }
    }
}