def ly(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def nxtDate(d, m, y):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if ly(y): days_in_month[2] = 29 # update
    if m < 1 or m > 12 or d < 1 or d > days_in_month[m]:
        print("invalid date")
    d += 1 # else

    if d > days_in_month[m]: # next month
        d = 1
        m += 1
        if m > 12: # next year
            m = 1
            y += 1
    print(f"Next date is : {d} {m} {y}")

if __name__ == "__main__":
    print("Enter date in format dd mm yyyy : ")
    d, m, y = map(int, input().split())
    nxtDate(d,m,y)
