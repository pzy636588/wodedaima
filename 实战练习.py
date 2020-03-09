print("欢迎使用中国移动充值业务,请输入充值金额:")
strmoney=input("用户输入充值金额(输入整数):0")
if strmoney<=0 and strmoney>=10:
    print("充值失败")
else:
    print("充值成功"+str(strmoney))