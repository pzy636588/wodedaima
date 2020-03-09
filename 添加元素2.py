print("2017-2018赛季NBA西部联盟前八名")
team=["火箭","勇士","开拓者","雷霆","爵士","鹈鹕","森灵狼"]
for index,item in enumerate(team):
    if index%2==0:
        print(item+"\t\t",end='')
    else:
        print(item+"\n")