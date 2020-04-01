str1='白日依山尽，黄河入海流，日穷千里目，更上一层楼 >>> www.sohu.com'
print('原字符串',str1)
'''list1=str1.split('.')
print(list1)'''
#list2=str1.split('>')
list3=str1.split()
print(list3)


str2='@奥巴马 @mayun @ksji'
list6=str2.split()
print(list6)
for item in list6:
    print(item[1:])     #输出每个好友，去掉@符号