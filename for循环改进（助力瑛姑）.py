print("今有物不知期数，三三数之剩二五，五五数之剩三，七七数之剩二，问几何？")
for number in range(100):
    if number%3==2and number%5==3 and number%7==2:
        print("答曰这个数是：",number)
        break
    print(number)