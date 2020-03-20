name=['绮梦','大美女','奥黛丽赫本','玛丽莲梦露']               #作为键的列表
sign=['水平座','天蝎座','双鱼座','魔蝎座']                    #作为值的列表
dictionary=dict(zip(name,sign))                            #转换为字典
print(dictionary)
#del dictionary            删除整个字典
#dictionary.clear()         #删除字典内容，原字典变空字典

dictionary.pop('绮梦')
print(dictionary)