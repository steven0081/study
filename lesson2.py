age= int(input("请输入你家狗的年龄："))
print("")
if age<0 :
    print("你是在骗人吧！")
elif age==1:
    print("相当于人类的14岁")
elif age== 2:
    print("相当于人类22岁")
elif age > 2:
    human = 22 + (age-2)*5
    print("相当于人类年龄：", human)

input("点击 enter 退出 。")