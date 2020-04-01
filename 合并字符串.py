#strnew=string.join(iterable)
#iterable:可迭代对象，该迭代对象中的所有元素（字符串表示），被合并称一个新的字符串
list_friend=['明日科技','马云','奥巴马','马化腾']
str_friend=' @'.join(list_friend)   #用空格+@符号进行连接
at='@'+str_friend                   #由于使用join()方法时，第一个元素前不加分割符，所以要在前面加@符号
print('您要@的好友：',at)
