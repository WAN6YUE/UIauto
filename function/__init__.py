def stu_register(name, age, *args, **kwargs):
    # 其中 args kwargs是习惯性写法
    # *args中数据以元组方式存储  **kwargs以关键参数传参 字典方式存储
    #*args是可变参数  **kwargs是关键字参数
    print(name, age, args, kwargs)


stu_register('小王', 24, '参数1', '参数2', '参数3', addr='山村')

# def test(*args,**kwargs):
#     print('------info------')
#     if 'hobbie' not in kwargs.keys():
#         print(f"name:{kwargs.get('name')}")
#         print(f"age:{kwargs.get('age')}")
#         print(f"sex:{kwargs.get('sex')}")
#         print("hobbie:大保健")
#     else:
#         print(f"name:{kwargs.get('name')}")
#         print(f"age:{kwargs.get('age')}")
#         print(f"sex:{kwargs.get('sex')}")
#         print(f"hobbie:{kwargs.get('hobbie')}")
#
# test(name='alex',age=22,sex='M')
# test(name='jack',age=26,sex='F',hobbie='学习')


