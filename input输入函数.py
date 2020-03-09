height=float(input("请输入您的身高(单位位米):168"))
weight=float(input("请输入您的体重(单位位千克):65"))
bmi=weight/(height*height)
print("您的bmi:"+str(bmi))
if bmi<18.5:
    print("您的体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("正常范围请注意保持")
if bmi>=24.9 and  bmi<29.9:
    print("您的的体重过重，注意锻炼身体")
if bmi>29.9:
    print("肥胖")