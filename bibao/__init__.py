def test(fun):
    def test2(*args,**kwargs):
        print("check login!!")
        fun(*args,**kwargs)
    return test2

@test
def f1(x):
    print("this is f1",x)

@test
def f2(x,y):
    print("this is f2",x,y)

@test
def f3(*args,**kwargs):
    print("this is f3",args,kwargs)


f1(123)
f2(1,3)
f3(1,4,5,test='abc',test2='xyz')