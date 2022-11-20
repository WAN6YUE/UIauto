# 读取csv 函数

from csv import DictReader


def read_csv(filename):
    # 从数据文件中 加载测试数据
    with open(filename, encoding="utf-8-sig") as f:
        read = DictReader(f)  # 实例化数据读取器
        for i in read:
            yield i


# if __name__=='__main__':
#     for data in read_csv("../datas/search.csv"):
#         print(data)
