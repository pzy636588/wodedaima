#语法如下
#dictionary=dict(key1=value1,key2=value2,...,keyn=valuen)
#dictionary:表示字典名称
#key1,key2,keyn:表示参数名，必须是唯一的，并且符合python的命名规则，改参数名将转换为字典的键
#value1,value2,valuen:表示参数值，可以是任何数据类型，不必须唯一，改参数的值将作为字典的值

dictionary=dict(绮梦='水瓶座',冷意一='天蝎座',香菱='双鱼座',戴兰='双子座')
print(dictionary)


#在python中，还可以使用dict对象的fromkeys()方法创建值为空的字典
#参数说明
#dictionary:表示字典名称
#list:作为字典键的列表
name_list=['绮梦','冷意一','项链','合办']            #作为键的列表
dictionary=dict.fromkeys(name_list)
print(dictionary)

#另外还可以通过已经存在的元组和列表创建字典，例如
name_tuple=('绮梦','冷意一','项链','合办')            #作为键的元组
sign=['水瓶座','天蝎座','双鱼座','处女座']             #作为值的列表
dict1={name_tuple:sign}                             #创建字典
print(dict1)