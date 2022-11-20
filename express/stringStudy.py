# #数据类型
#
# #字符串 字符串是一个 有序 的字符的集合，用于在计算里存储和表示文本信息
#
# string = 'hello,my name is wang'
# #字符串可以按照索引取值
# print(string[1])
#
# #字符串可以切片
# print(string[0:7])#顾头不顾尾 0会切进来 7不会切进来
#
# #字符串是不可变的，不可修改其中元素； 但是可以重新赋值；注意 重新赋值 不等于 修改
# string[0]= '1'#错误操作，字符串是不可变的
# string ='abc '#重新赋值

# #字符串常用方法
# a = 'wangyuew'
# print(a.center(10,"-"))#居中操作
# print(a.count('w'))#字符计数 且可规定统计范围
# print(a.count('g',0,1))#字符计数 且可规定统计范围 局部计数
# print(a.endswith('w'))#判断字符是不是以 什么 结尾
# print(a.endswith('x'))#判断字符是不是以 什么 结尾
# print(a.startswith('w'))#判断字符是不是以 什么 开头
# print(a.startswith('x'))#判断字符是不是以 什么 开头
# print(a.find("f"))#查找字符 从左到右 找到返回索引，未找到返回-1
# print(a.find("a"))#
# print(a.isdigit())#判断是否是整数
# print('100'.isdigit())#判断是否是整数 数字形式返回True
#
# l=['小鲤鱼','懒洋洋','奥特曼']
# print('-连接符-'.join(l))#join 拼接字符串
#
# print(a.replace('w','W',1))#w替换为W 替换1次
# print(a)#a值不会变
#
b='acbcdc1'
print(b.split('c'))#按照 aplit中的元素划分未list
print(b.split('c',1))#按照 aplit中的元素划分未list 分一次

