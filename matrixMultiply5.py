m = int(input("Enter M1 rows:"))
n = int(input("Enter M1 columns:"))
o = int(input("Enter M2 rows:"))
p = int(input("Enter M2 columns:"))

if n == o:
    A = [[int(input()) for _ in range(n)] for _ in range(m)]
    B = [[int(input()) for _ in range(p)] for _ in range(o)]

    result = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(p)] for i in range(m)]

    for row in result:
        for val in row:
            if val != 0:
                print(val, end=" ")
            else:
                print("Matrix Multiplication is not possible")
else:
    print("Matrix Multiplication is not possible")

