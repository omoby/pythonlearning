age = int(input("输入狗狗的年龄："))
print("")
if age <= 0:
    print("狗狗还没有出生！")
elif age == 1:
    print("相当于14岁的人！")
elif age == 2:
    print("相当于22岁的人！")
else:
    human = 22 + (age - 2) * 5
    print("狗狗%d岁,相当于%d岁的人！" %(age,human))

input("点击enter键退出")
