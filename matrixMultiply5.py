m = int(input("Enter M1 rows:"))
n = int(input("Enter M1 columns:"))
o = int(input("Enter M2 rows:"))
p = int(input("Enter M2 columns:"))

if n == o:
    A = [[int(input()) for _ in range(n)] for _ in range(m)]
    B = [[int(input()) for _ in range(p)] for _ in range(o)]
    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            result[i][j] = total

    for row in result:
        for val in row:
            print(val, end=" ")
        print()
else:
    print("Matrix Multiplication is not possible")
