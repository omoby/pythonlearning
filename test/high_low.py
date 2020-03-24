number = 7
guess = -1
print("猜数字游戏")
while guess != number:
    guess = int(input("请输入你猜的数字："))
    if guess == number:
        print("恭喜你猜对了！")
    elif guess < number:
        print("你猜的数字太小了..")
    else:
        print("你猜的数字太大了...")