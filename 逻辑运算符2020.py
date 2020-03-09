print("\n手机店正在打折，活动进行中........")
strWeek=input("请输入中文星期(如星期一):星期六")
intTime=int(input("请输入时间中的小时(范围:0~23):10"))
if (strWeek =="星期二" and (intTime>=9 and intTime<=12)) or (strWeek =="星期五" and (intTime>=13 and intTime<=16)):
    print("恭喜您获得活动参与资格，快去抢购吧")
else:
    print("很遗憾，您来晚一步，下次继续")
