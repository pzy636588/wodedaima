#setname.add(element)
#setname:表示要添加元素的集合
#element:表示要添加的元素内容，只能使用字符串，数字布尔类型的true或false及元组等不可变对象
mrs=set(['零基础学Python','零基础学电脑','零基础学c语言'])
mrs.add('零基础学写代码')
print(mrs)
mrs.remove('零基础学电脑')
mrs.pop()          #随机删除一个
mrs.clear()        #清除所有数据
print(mrs)