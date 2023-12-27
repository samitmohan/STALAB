print("Enter M1 Rows, M1 Columns, M2 Rows, M2 Columns : ")
m, n, o, p = map(int, input().split())
if n == o:
    A = [[int(input()) for _ in range(n)] for _ in range(m)]
    B = [[int(input()) for _ in range(p)] for _ in range(o)]
    ans = [[0 for _ in range(p)] for _ in range(m)] # empty matrix
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            ans[i][j] = total
    for each_row in ans:
        for val in each_row:
            print(val, end = " ")
        print() # empty line
else:
    print("Matrix Multiplication not possible")
