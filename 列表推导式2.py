price=[1200,5330,2998,6200,1998,8888]
'''sale=[int(x*0.5)for x in price]'''
sale=[x for x in price if x>5000]
print("原来的价格：",price)
print("价格高于5000的：",sale)

price=[1200,5330,2988,6200,1988,8888]
sale=[int(x*0.5) for x in price]
print("原来的价格:",price)
print("打折后价格：",sale)

#列表推导式的三种语法
#1 生成指定范围的数值列表
#list=[Expression for var in range]
#参数说明：list:表示生成的列表名称
#         Expression:表达式用于计算新列表的元素
#         var:循环变量
#         range:采用range()函数生成的range对象
# 例子：import random
# randomnumber=[random.randint(10,100)for i in range(10)]
# print("生成的随机数为：",randomnumber)


#2 根据列表生成指定需求的列表
#newlist=[Expression for var in list]
#参数说明：newlist:表示新生成的列表名称
#         Expression:表达式,用于计算新列表的元素
#         var:变量,值为后面列表的每个元素值
#         list:用于生成新列表的原列表
#例子:price=[1200,5330,2988,6200,1988,8888]
sale=[int(x*0.5) for x in price]
print("原来的价格:",price)
print("打折后价格：",sale)

#从列表中选择符合条件的元素组成新的列表
#newlist=[Expression for var in list if condition]
#参数说明：newlist:表示新生成的列表名称
#         Expression:表达式，用于计算新列表的元素
#         var:变量，值为后面列表的每个元素值
#         list:用于生成新列表的原列表
#         condition:条件表达式，用于指定帅选条件
#例子：price=[1200,5330,2998,6200,1998,8888]
'''sale=[int(x*0.5)for x in price]'''
sale=[x for x in price if x>5000]
print("原来的价格：",price)
print("价格高于5000的：",sale)
#
#
#
#
#
