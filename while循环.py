none=True
number=0
while none:
    number+=1
    if number%3==2 and number%5==3 and number%7==2:
        print("这个数是",number)
        none=False