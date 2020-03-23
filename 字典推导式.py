import random
randomdict={i:random.randint(2,5000) for i in range (1,8)}
print('生成的字典为:',randomdict)



name=['绮梦','姜子牙','诸葛亮']
sign=['天蝎','射手','魔蝎']
dictionary={i:j+'座' for i,j in zip(name,sign)}   #使用列表推导式生成字典
print(dictionary)