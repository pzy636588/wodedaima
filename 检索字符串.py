#str,count(sub,start[,end])
#str:原字符串
#sub:要检索的字符串
#start:可选参数，表示检索范围的起始位置的索引，如果不指定，则从头开始检索
#end:可选参数，表示检索范围的结束位置的索引，如果不指定，则一直检索到结尾

str1='@麻花 @马云 @liuj'
print(str1.count('@'),'个@符号')