import random
num=random.randint(1,100)
guess_times=0
flag=True
while flag:
    guess_num=int(input("请输入一个数字："))
    guess_times+=1
    if guess_num==num:
        print("恭喜你猜对了！")
        flag=False
    else:
        if guess_num>num:
            print("你猜大了")
        else:
            print("你猜小了")
print("你已经猜测了%d次"%guess_times)










