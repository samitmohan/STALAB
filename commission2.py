lock_price = 45.0
stock_price = 30.0
barrel_price = 25.0

total_locks = 0
total_stocks = 0
total_barrels = 0

print("Enter the number of locks and to exit press -1")
locks = int(input())

while locks != -1:
    if not (1 <= locks <= 70):
        print("Value of locks is not in the range of 1...70")
    else:
        total_locks += locks

    print(f"Total locks = {total_locks}")

    print("Enter the number of stocks and barrels")
    stocks, barrels = map(int, input().split())

    if not (1 <= stocks <= 80):
        print("Value of stocks is not in the range of 1...80")
    else:
        total_stocks += stocks

    if not (1 <= barrels <= 90):
        print("Value of barrels is not in the range of 1...90")
    else:
        total_barrels += barrels

    print(f"Total stocks = {total_stocks}")
    print(f"Total barrels = {total_barrels}")

    print("Enter the number of locks and to exit press -1")
    locks = int(input())

print(f"Total locks = {total_locks}")
print(f"Total stocks = {total_stocks}")
print(f"Total barrels = {total_barrels}")

lock_sales = total_locks * lock_price
stock_sales = total_stocks * stock_price
barrel_sales = total_barrels * barrel_price
sales = lock_sales + stock_sales + barrel_sales

print(f"Total sales = {sales}")

if sales > 1800:
    com = 0.10 * 1000 + 0.15 * 800 + 0.20 * (sales - 1800)
elif sales > 1000:
    com = 0.10 * 1000 + 0.15 * (sales - 1000)
else:
    com = 0.10 * sales

print(f"Commission = {com}")

