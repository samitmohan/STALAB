def main():
    check = True
    while check:
        a, b, c = map(int, input().split())
        # constraints : 1-10
        side1 = ((a >= 1)) and ((a <= 10))
        side2 = ((b >= 1)) and ((b <= 10))
        side3 = ((c >= 1)) and ((c <= 10))
        if not side1: print("a is not in range")
        if not side2: print("b is not in range")
        if not side3: print("c is not in range")

        check = (not side1) or (not side2) or (not side3)
        if (a < (b + c)) and (b < (a + c)) and (c < (a + b)): # tri
            if ((a == b) and (b == c)):
                print("EQ")
            elif ((a != b) and (b != c) and (c != a)):
                print("SC")
            else:
                print("IS")
        else:
            print("Triangle cannot be formed")

main()
