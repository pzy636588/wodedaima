import turtle                                #导入turtle模块
turtle.showturtle()                         #显示箭头
turtle.write("彭大帝国")                      #写字符串
turtle.forward(200)                          #前进300像素
turtle.color("red")                         #画笔颜色改为红色
turtle.left(91)                              #箭头左转91度
turtle.forward(300)
turtle.goto(0,50)
turtle.goto(0,0)
turtle.penup()                             #抬笔（不然路径画不出来）
turtle.goto(0,300)                         #引入坐标0,300
turtle.pendown()                           #收笔
turtle.goto(0,50)
turtle.goto(50,50)
turtle.circle(100)
turtle.goto(100,0)
turtle.circle(200)
turtle.goto(0,50)
turtle.circle(150)
turtle.forward(50)

