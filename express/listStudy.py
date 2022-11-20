#list列表 []内 以逗号分割，按照索引，存放各种数据类型，每个位置代表一个元素

#可存放多个值
#从左至右 从0开始
#可修改指定索引的值 是可变的
#
# x = []
#
# #append 追加
# x.append('appenTest')
# print(x)
#
# #insert 插入
# x.insert(1,'插入索引为1的位置')
# print(x)
#
# #合并
# n1=['n1的值']
# n2=['n2的值']
# n2.extend(n1)#n2合并n1
# print(n2)
# n1.extend(n2)
# print(n1)

#列表嵌套 列表中可以嵌套列表
# x1=[1,2,3]
# x2=['x2的值']
# x2.insert(0,x1)
# print(x2)
# print(x2[0][2])

# #删除 del
# x=[1,2,3]
# del x[0]
# print(x)

# #删除pop 默认删除最后一个元素并返回被删除的值
# x2=[1,2,3]
# print(x2.pop())
# print(x2)
# x3=[1,2,3]
# print(x3.pop(0))
# print(x3)
# x4=['a','b','c']
# x4.remove('a')
# print(x4)
# x5=[3,2,1]
# x5.clear()
# print(x5)
#
# test=['a','b','c','d','e','f','a']
#
# if 'f' in test:
#     item_index=test.index('f')#取索引
#     test[item_index]='修改'
#     print(test)
#
# print(test.count('a'))#代表有两a

# #排序
# x=['a','b','测','e','E','A','阿','百']
# x.sort()
# print(x)#字符不能和数字一起排序 字符排序规则为 大写 小写 中文
# x.reverse()#反转
# print(x)

# #循环列表+索引
# x=[1,2,3,4]
# for i in enumerate(x):#enumerate为关键字 打印出元组 元组和list完全一样 只是不能改
#     print(i[0],i[1])

#元组
# tuple = (1,2,3)
# #遍历元组
# for i in tuple:
#     print(i)
#
# tuple[0]='x' #错误 元组不可修改

# #成绩分组 分成3组 90-100 ，60-89，0-59
# stu_list=[['stu_001',100],['stu_002',95],['stu_003',89],['stu_004',70],['stu_005',59]]
#
# new_list=[[],[],[]]
#
# for i in stu_list:
#     if i[1]>=90 and i[1]<=100:
#         new_list[0].append(i)
#     elif i[1]>=60 and i[1]<=89:
#         new_list[1].append(i)
#     else:
#         new_list[2].append(i)
#
# print(new_list)
# print(new_list[0])
# print(new_list[1])
# print(new_list[2])



