#string[start:end:step]
#start:表示要截取的第一字符串的索引（包括该字符）
#end:表示要截取的最后一个字符串的索引（不包括该字符）
#step:表示切片的步长，如果省略可默认为1,当省略改步长时，后面的冒号也可以省略

str='人生苦短，我用Python'
substr1=str[2]               #截取第三个字符
substr2=str[:4]              #从左边开始截取第4个字符
substr3=str[5:]              #从第6个字符开始截取
substr4=str[2:6]             #截取第3个到第6个字符
print(substr1+'\n'+substr2+'\n'+substr3+'\n'+substr4)