package triangle;

public class yo {
	public static String triangle(int a, int b, int c) {
		
		boolean side1 = (a>=1) && (a <=10);
		boolean side2 = (b>=1) && (b <=10);
		boolean side3 = (c>=1) && (c <=10);
		if (!side1)
			System.out.println("a not in range");
		if (!side2)
			System.out.println("b not in range");
		if (!side3)
			System.out.println("c not in range");
		if (side1 && side2 && side3) {
			// check for triangle
			if (a < (b+c) && b < (a+c) && c <(a+b)) {
				if ((a==b) && (b==c)) System.out.println("equilateral");
				else if ((a !=b) && (b!=c) && (c!=a)) {
					System.out.println("scalene");
				} else {
					System.out.println("isoceles");
				}
			} else {
				System.out.println("Triangle cant be formed");
			}
		}
		return null;
	}
}
