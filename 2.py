lockPrice = 45.0
stockPrice = 30.0
barrelPrice = 25.0

total_locks = 0
total_stocks = 0
total_barrels = 0

print("Enter number of locks (to exit enter -1)")
locks = int(input())

while locks != -1:
    if not (1 <= locks <= 70):
        print("Not in range")
    else:
        total_locks += locks
    print(f"Total locks = {total_locks}")

    print("Enter number of stocks and barrels : ")
    stocks, barrels = map(int, input().split())
    if not (1 <= stocks <= 80):
        print("Not in range")
    else:
        total_stocks += stocks
    if not (1 <= barrels <= 90):
        print("Not in range")
    else:
        total_barrels += barrels

    print(f"Total stocks = {total_stocks}")
    print(f"Total barrels = {total_barrels}")

    print("Enter number of locks (to exit enter -1)") # ask again
    locks = int(input())

# end result
print(f"Total locks = {total_locks}")
print(f"Total stocks = {total_stocks}")
print(f"Total barrels = {total_barrels}")
lock_sales = total_locks * lockPrice
stock_sales = total_stocks * stockPrice
barrel_sales = total_barrels * barrelPrice
sales = lock_sales + stock_sales + barrel_sales
print(f"Total sales : {sales}")

# comission
if sales > 1800:
    com = 0.10 * 1000 + 0.15 * 800 + 0.20 * (sales-1800)
elif sales > 1000:
    com = 0.10 * sales + 0.15 * (sales-1000)
else:
    com = 0.10 * sales

print(f"Comission = {com}")
