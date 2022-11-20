#在类里面的方法 第一个参数写self
class findMax:

    def __init__(self,content):
        self.data=content#初始化方法 在实例化对象时 自动执行

    def max(self,a,b):
        data = self.data
        print(data)
        if a>b:
            return a
        else:
            return b

    def min(self, a, b):
        data = self.data
        print(data)
        if a > b:
            return b
        else:
            return a


test_max = findMax("测试TEST")#实例化对象test_max


print(test_max.max(3,4))#使用test_max对象 使用方法max 传入3，4且返回4
print()
print(test_max.min(3,4))#使用test_max对象 使用方法min 传入3，4且返回3
print()

test_max2 = findMax("测试TEST2")#实例化对象test_max

print(test_max2.max(4,5))



#类属性     所有实例共享
#实例属性   实例独享