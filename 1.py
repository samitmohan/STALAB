def main():
    check = True
    while check:
        a,b,c = map(int, input().split())
        s1 = ((a >=1 ) and (a<=10))
        s2 = ((b >=1 ) and (b<=10))
        s3 = ((c >=1 ) and (c<=10))
        if not s1: print("a not in range")
        if not s2: print("b not in range")
        if not s3: print("c not in range")
        if s1 and s2 and s3:
            if (a < (b+c)) and (b < (a+c)) and (c < (a+b)):
                    if a == b ==c: print("Equilateral")
                    elif a != b != c != a: print("Scalene")
                    else:
                        print("Iscoceles")
            else:
                print("Triangle can't be formed")
main()
