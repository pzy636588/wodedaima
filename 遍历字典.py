#dictionary.item(),其中dictionary为字典对象，返回值即可遍历的（键--值）的元素列表，想要获取到具体的“键--值对”，可以通过for循环
#遍历该元素列表
dictionary={'阿里巴巴':'码云','腾讯控股':'马化腾','字节跳动':'张一鸣'}
for item in dictionary.items():
    print(item)                          #获取字典的各个元素
dictionary = {'阿里巴巴': '码云', '腾讯控股': '马化腾', '字节跳动': '张一鸣'}
for key,value in dictionary.items():
    print(key,'掌门人是',value)  #获取每个的键和值

