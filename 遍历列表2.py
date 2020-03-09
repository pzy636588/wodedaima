#直接使用for循环
print("一走计算机房")
team=["休斯敦 火箭","金州 勇士","波特兰 开拓者","犹他 爵士"]
'''for item in team:
    print(item)'''

#使用for循环和enumerate()函数实现
#for index,item in enumerate(listname)
#输出index和item
for index,item in enumerate(team):       #index,用于保存元素的suoy，item用于保存取到的元素值，要输入元素内容时，直接输出改变量即可
    print(index+1,item)