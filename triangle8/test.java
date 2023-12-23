package triangle8;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class TestClass {

    @Test
    public void testTriangle() {
        Test obj = new Test();
        String op1 = obj.triangle(10, 10, 10);
        assertEquals("equilateral", op1);
        String op2 = obj.triangle(10, 10, 5);
        assertEquals("isosceles", op2); // Corrected the spelling of isosceles
        String op3 = obj.triangle(5, 6, 7); // Corrected the variable name to op3
        assertEquals("scalene", op3);
    }
}
