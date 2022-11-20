# #操作文件
# #w 创建
# #r 只读
# #a 追加
# #各模式不能混用
#
# #创建文件w
# f=open('TestWord',mode='w')#w参数用于创建 无则创建 有则覆盖
# f.write("hello,this is word write TEST1\n")
# f.write("hello,this is word write TEST2\n")#需要自己手动添加\n换行 不然文件中不会换行
# f.close()
# # f.read() #前面指定了 w ，此时不能读
#
# #只读文件r
# x=open('TestWord',mode='r')#等同 x=open('TestWord','r') x=open('TestWord')
# print("read first line first :\n%s" %x.readline())#读取第一行
# print("read all:\n%s" %x.read())
# print("rea first line again :\n%s" %x.readline())#前面已经read所有 再次read为空
#
# #追加文件a
# a = open('TestWord',mode='a')#用于写日志场景
# a.write('zhuijia 1\n')
# a.write('zhuijia 2\n')
# f.close()

# #遍历文件
# f=open('TestWord2','rb')
# # print(f.readline().decode())
# for i in f:
#     i =i.decode().split()
#     height=int(i[3])
#     weight=int(i[4])
#     if height>=170 and weight<=50:
#         print(i)