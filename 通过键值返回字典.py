name=['绮梦','大美女','奥黛丽赫本','玛丽莲梦露']               #作为键的列表
sign=['水平座','天蝎座','双鱼座','魔蝎座']                    #作为值的列表
dictionary=dict(zip(name,sign))                            #转换为字典
print(dictionary)
print(dictionary['大美女'])      #在使用字典时，很少直接输出它的内容，一般需要根据指定的键获得相应的结果
#在实际开发中，我们可不知道存在什么键，所以需要避免该异常的发生，具体的解决办法使用if语句对不存在的情况进行处理，需设置一个默认值
#python中使用字典对象的get()方法获得指定键的值
#dictionary.get(key,[,default]）
#default:为可选项，当指定的“键”不存在时，返回一个默认值，如果省略返回none

print('型的的星座是:',dictionary['型的'] if '型的' in dictionary else '我就干了此人')