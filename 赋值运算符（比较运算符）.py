python=98                        #定义变量，存储python的分数
english=92                       #定义变量，存储english的分数
c=89                             #定义变量，存储c语言的分数
sub=python-c                     #计算python语言和c语言的分数之差
avg=(python+english+sub)/3       #计算平均成绩
avg=int(avg)                     #字符串转换
print(type(avg))
sum=python+english+c             #计算总分
print(type(sum))
print("python课程与c语言课程分数之差:"+str(sub)+"分\n")
print("课程的平均分："+str(avg)+"分\n")
print("课程总分:"+str(sum)+"分\n")
print("python="+str(python)+"english="+str(english)+"c="+str(c)+"\n")
print("english>pthon分数:"+str(english>python)+"\n")

