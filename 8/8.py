# If permitted in exam else do in Java
import unittest

class Main:
    @staticmethod
    def triangle(a, b, c):
        s1 = 1 <= a <= 10
        s2 = 1 <= b <= 10
        s3 = 1 <= c <= 10
        if not s1: return "a not in range"
        if not s2: return "b not in range"
        if not s3: return "c not in range"

        if s1 and s2 and s3:
            if a < (b + c) and b < (a + c) and c < (a + b):
                if a == b == c: return "equilateral"
                elif a != b != c != a: return "scalene"
                else: return "isosceles"
            else:
                return "Triangle can't be formed"

class TestTT(unittest.TestCase):
    def test_triangle(self):
        obj = Main()
        op1 = obj.triangle(10, 10, 10)
        self.assertEqual(op1, "equilateral")

        op2 = obj.triangle(10, 10, 5)
        self.assertEqual(op2, "isosceles")

        op3 = obj.triangle(5, 6, 7)
        self.assertEqual(op3, "scalene")

if __name__ == '__main__':
    unittest.main()

