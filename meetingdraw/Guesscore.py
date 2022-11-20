import string

age = 14
# if guess_age>age:
#     print("猜大了")
# if guess_age<age:
#     print("猜小了")
# if guess_age==age:
#     print("猜对了")

# for i in range(3):
#     guess_age = int(input("输入猜测的年龄："))
#     if guess_age>age:
#         print("猜大了")
#     elif guess_age<age:
#         print("猜小了")
#     else:
#         print("猜对了")
#         break #break终止循环 后面的代码依然会执行 只是跳出本层循环
# print("后面的代码")

# for i in range(3):
#     guess_age = int(input("输入猜测的年龄："))
#     if guess_age>age:
#         print("猜大了")
#     elif guess_age<age:
#         print("猜小了")
#     else:
#         exit("猜对了")#for循环退出语法 且后面的代码不会执行
# print("后面的代码")



#0-100奇偶数
# for i in range(100):
#     if i % 2 == 0:
#         print(f"偶数：{i}")
#     else:
#         print(f"奇数{i}")


#打印楼层房间号
# for i in range(1,6):
#     for j in range(1,11):
#         print(f"这是L{i}-{i}{j}房间",end=",")
#     print()

#continue结束本次循环 进入下次循环
#break 结果本层循环 如果遇到多层循环 直结束当前这层

# for i in range(1,6):
#     if i==3:
#         continue
#     for j in range(1,11):
#         print(f"这是L{i}-{i}{j}房间",end=",")
#     print()

# for i in range(1,6):
#     for j in range(1,11):
#         if i==4 and j==4:
#             print("遇到鬼屋",end="")
#             break
#         print(f"这是L{i}-{i}{j}房间",end=",")
#     print()

# #打印三角形
# for i in range(10):
#     if i<=5:
#         print("*"*i)
#     else :
#         print("*"*(10-i))


# string='aabbcc112233'
# x=[]
#
# for i in range(len(string)):
#     if string[i] not in x:
#         x.append(string[i])
# print(x)
# print("".join(x))#list转string list里面必须去全部是字符串

#string转list
# string='aabbcc112233'
# print(list(string))


# name = "王李张李陈王杨张吴周王刘赵黄吴杨"
# new_name = ''
# for char in name:
#     if char not in new_name:  # 如果不在新的字符串中
#         new_name += char  # 拼接到新字符串中的末尾
# print(new_name)
#
#set去重
# city = ['上海', "广州", "上海",  "上海", "上海",  "广州"]
# new_city=set(city)
# print(new_city)


#while循环
# while 条件： 当条件成立就会不断的循环

# count = 0
# while count<10:
#     count += 1
#     print(count)

# #打印99乘法表
# for i in range(10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i * j}',end=",")
#     print()
#

#生成车牌
#random模块
import random

# print(random.choice("abc123"))
# s="abc123"
# print(random.sample(s,4))
# print(random.randint(1,100))

#string模块
# import string
# print(string.ascii_letters)#打印所有大小写字母
# print(string.ascii_lowercase)#所有小写字母
# print(string.ascii_uppercase)#所有大写字母
# print(string.punctuation)#所有特殊字符
# print(string.digits)#所有数字

#
# plate=random.sample(string.ascii_uppercase+string.digits,5)
# print(f'京{"".join(plate)}')

# import time
# count =1
# while count<4:
#     total_plate = []
#     for i in range(10):
#         n1=random.choice(string.ascii_uppercase)
#         n2="".join(random.sample(string.ascii_uppercase+string.digits,5))
#         now_plate=f'川{n1}-{n2}'
#         total_plate.append(now_plate)
#         print(i+1,now_plate)
#     choice_plate=input("进入选号流程 输入'无' 或 请输入你想要的车牌号：").strip()
#     if count != 0:
#             if choice_plate in total_plate:
#                 exit(f'恭喜！ 选号完成 车牌是：{choice_plate}')
#             elif choice_plate == '无':
#                 if count == 3:
#                     print("机会用完 无法选号 即将退出程序-----")
#                     time.sleep(2)
#                     break
#                 else:
#                     print(f'请继续选号 还剩下{3 - count}次机会!')
#                     print('车牌生成中，请稍后-----')
#                     time.sleep(2)
#             else:
#                 if count == 3:
#                     print("机会用完 无法选号 即将退出程序-----")
#                     time.sleep(2)
#                     break
#                 else:
#                     print(f'输入不合法，还剩下{3 - count}次机会! 请重新输入')
#                     print('车牌生成中，请稍后-----')
#                     time.sleep(2)
#     count += 1


#meeeting_draw
emp_pop3=[]
emp_pop2=[]
emp_pop1=[]
total_emp_pop=[]
three_count=0
two_count=0
one_count=0
while three_count<3:#
    emp=f"emp_{random.randint(1,6)}"
    if emp not in total_emp_pop:
        total_emp_pop.append(emp)
        emp_pop3.append(emp)
    else:
        three_count-=1
    three_count+=1
while two_count<2:
        emp=f"emp_{random.randint(1,6)}"
        if emp not in total_emp_pop:
            total_emp_pop.append(emp)
            emp_pop2.append(emp)
        else:
            two_count -= 1
        two_count += 1
while one_count < 1:
            emp = f"emp_{random.randint(1, 6)}"
            if emp not in total_emp_pop:
                total_emp_pop.append(emp)
                emp_pop1.append(emp)
            else:
                one_count -= 1
            one_count += 1


print(f'获得三等奖的员工的{len(emp_pop3)}位员工是{emp_pop3}')
print(f'获得二等奖的员工的{len(emp_pop2)}位员工是{emp_pop2}')
print(f'获得一等奖的员工的{len(emp_pop1)}位员工是{emp_pop1}')





