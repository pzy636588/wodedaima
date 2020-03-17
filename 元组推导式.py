#使用元组推导式可以快速生成一个元组，它的表现形式与列表推导式相同，只是将列表推导式中的“[]”修改成“()”,例子如下
import random                                              #导入randorm标准库
randomnumber=(random.randint(10,100)for i in range(10))
randomnumber=tuple(randomnumber)                           #转换为元组
print("生成的元组为：",randomnumber)


number=(i for i in range(10))                             #生成生成器对象
for  i in number:                                         #遍历生成器对象
    print(i,end="")                                       #输出每个元素的值
print(tuple(number))                                      #转化为元组输出


number1=(i for i in range(6))
print(number1.__next__())
print(number1.__next__())
print(number1.__next__())
print(number1.__next__())
print(number1.__next__())
print(number1.__next__())
number1=tuple(number1)
print("转换后：",number1)