#国家质量监督检验局发布的《车辆驾驶人员血液。呼吸酒精含量阀值与检验》中规定，车辆驾驶人员血液中的酒精含量小于20Mg/100ml
#不构成饮酒驾驶行为;酒精含量大于或等于20mg/100m,小于80mg/100ml为饮酒驾车;酒精含量大于或等于50mg/100ml为醉酒驾车
#现编写如下python代码判断是否酒后驾车
print("\n为了您和您家人的安全，严禁酒后驾车!\n")
proof=20
if proof<20:
    print("\n您不构成酒驾行为，可以开车，但要注意安全")
else:
    if proof<80:
            print("\n您的行为已经构成酒后驾驶标准，请不要开车")
    else:
        print("\n已经达到醉酒驾驶标准，千万不要开车")