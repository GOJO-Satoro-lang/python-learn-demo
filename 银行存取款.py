money=50
name=None
def query(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f"{name},您好，您的余额剩余：{money}元")

def saving(num_in):
    global money
    money+=num_in
    print("----------存款----------")
    print(f"{name},您好，您存款{num_in}元成功")
    query(False)

def taking(num_out):
    global money
    print("----------取款----------")
    if money >= num_out and num_out>0:
        money-=num_out
        print(f"{name},您好，您取款{num_out}元成功")
    else:
        print(f"{name},您好，您取款{num_out}元失败。")
    query(False)

def menu():
    print("----------主菜单----------")
    print(f"{name},您好，欢迎来到黑马银行ATM，请选择操作。")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    return input("请输入您的选择：   ")

while True:
    keyboard_input=menu()
    if keyboard_input == "1":
        query(True)
        while True:
            back=input("输入数字0，返回主菜单：")
            if back=="0":
                break
    elif keyboard_input == "2":
        num_in=int(input("请输入存款金额："))
        saving(num_in)
        while True:
            back = input("输入数字0，返回主菜单：")
            if back == "0":
                break
    elif keyboard_input == "3":
        num_out=int(input("请输入取款金额："))
        taking(num_out)
        while True:
            back = input("输入数字0，返回主菜单：")
            if back == "0":
                break
    else:
        print("程序退出了。")
        break