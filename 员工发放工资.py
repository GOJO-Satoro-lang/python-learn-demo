money=10000
worker=1
for worker in range(1,21):
    import random
    score = random.randint(1, 10)
    if score <5:
        print(f"员工{worker}，绩效分低于5，不发工资，下一位")
        continue
    if money>=1000:
        money-=1000
        print(f"向员工{worker}发放工资1000元，账户余额还剩余{money}元")
    else:
        print("工资发完了，下个月领取吧。")
        break



