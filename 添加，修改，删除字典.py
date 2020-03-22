#dictionary[key]=value

#其中key表示键（必须是唯一的），value表示元素的值（可以是任何数据类型）
dictionary=dict((('绮梦','水瓶座'),('王祖贤','天蝎座'),('李嘉欣','处女座'),('钟楚红','魔蝎座')))
dictionary['林青霞']='天平座'           #添加一个元素，当元素存在时，则相当于修改功能
del dictionary['钟楚红']               #删除一个元素
if '黎巴嫩' in dictionary:
    del dictionary['黎巴嫩']
else:
     dictionary['黎巴嫩']='法国的曾经的殖民地'

print(dictionary)