#字典

#列表实现查工资 缺点：需要遍历
# staff_list =[['emp_001',22,'CEO','1000'],['emp_002','25','PM','2000']]
# for i in staff_list:
#     if i[0]=='emp_001':
#         print(i[3])#或者print(i[-1])


# #字典实现查对应人工资
# #dict定义{key1:value1,key2:value2}
# dict={'emp001':[22,'CEO',1000],'emp002':[25,'PM',2000]}
# print('emp002' in dict)#判断 emp002 是否在dict里面
# print(dict['emp002'])
#
# dict ={'a':1,'a':2}
# print(dict)

# #key-value结构
# #key必须为不可变数据类型 字符 数字 必须唯一
# #可存放任意多个value 可修改 不可唯一
# #无序
# #查询速度快 且不受dict大小影响
#
# #新增key
# dict={'a':1,'b':2,4:4,5:5}
# dict['c']=3#新增
# print(dict)
# #删
# print(dict.pop(4))#根据key指定删除  且返回删除的key对应的 value
# print(dict)
# del dict[5]
# print(dict)
# #改
# dict['a']='editTest'
# print(dict['a'])
#
# #注意： 字典无切片操作 也只能通过key查value 不能直接查value(遍历可以达到)

# #遍历字典
dict={'a':1,'b':2,4:4,5:5}
# for k in dict.keys():#循环key
#     print(k)
# print()
# for v in dict.values():#循环value
#     print(v)
# print()
# for item in dict.items():#转为元组 item有转化过程 效率低
#     print(item)
# print()
# for itemk,itemv in dict.items():#两个变量 单独取key和value
#     print(itemk,itemv)
# print()
for k in dict:#推荐 效率最高
    print(k,dict[k])

# #字段长度
# dict={'a':1,'b':2,4:4,5:5}
# print(len(dict))#len()可判断 字典 列表 字符串的长度

# #字典嵌套  可无限制嵌套
# dict ={}
# dict['test'] = {'test123':123}
# print(dict)
# print(dict['test']['test123'])




