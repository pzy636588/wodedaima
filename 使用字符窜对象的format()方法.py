template='编号:{:0>9s}\t公司名称:  {:s}  \t官网:  http://www.{:s}.com'  #定义模板
context1=template.format('7','百度','baidu')                           #转换内容1
context2=template.format('8','明日学院','mingrisoft')                  #转换内容2
print(context1)
print(context2)