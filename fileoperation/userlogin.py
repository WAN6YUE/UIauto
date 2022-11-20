accounts = {}
f = open('account')
for i in f:
    i = i.strip().split(",")  # strip去掉首位空格  用split使用 ，变成列表
    accounts[i[0]] = i
print(accounts)

count = 0
while True:
    username = input("请输入账号：").strip()
    if username not in accounts:
        print("非法用户名 请重新输入")
        continue
    elif username in accounts and accounts[username][2]=='1':
        print('用户锁定状态 不可登录')
        continue
    while count < 3:
        passward = input("请输入密码：").strip()
        if accounts[username][1] == passward:
            exit(f"密码正确 欢迎！{username} 正在进入系统")
        else:
            print("用户名 或 密码错误！ 请重试！")
        count += 1
        if count==3:
            print(f"输错{count}次密码，{username}账户 被锁定")
            accounts[username][2]='1'
            f2=open('account','w')
            for k in accounts:
                new_data=','.join(accounts[k])+'\n'
                f2.write(new_data)
            f2.close()
            exit()




# if username in account and account[username][2]=='1':
#     passward = input("请输入密码：").strip()
#     if account[username][1]==passward:
#         exit("用户密码正确 进入系统")
#     else:
#         print("用户名 或 密码错误！ 请重试！")
#         if count ==2 :
#             account[username][2]='0'
# else:
#     print("非法用户名 用户未注册 或者已经被锁定")
#     count-=1
