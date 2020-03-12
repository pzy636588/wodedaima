'''verse=[["千山鸟飞绝"],["万径人踪灭"],["孤舟蓑笠翁"],["独钓寒江雪"]]
print(verse)'''
arr=[]                       #创建一个空列表
for i in range(4):
    arr.append([])           #在空列表中添加一个空列表si
    for j in range(5):
        arr[i].append(j)     #为内层列表添加元素


print(arr)