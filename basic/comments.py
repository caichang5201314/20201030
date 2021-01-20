# -*- coding: utf-8 -*-

# 单行 某行或某些行为

'''
这是块级别注释
对类或对函数进行解释用
'''


# 定义一个计算执行时间的函数作装饰器，传入参数为装饰的函数或方法
def print_execute_time(func):
    from time import time
    def wrapper(*args, **kwargs):
        start = time()
        func_return = func(*args, **kwargs)
        end = time()
        if end-start<func_return:
            print(f'{func.__name__}() execute time: {end - start}s')
        return func_return
    return wrapper

@print_execute_time
def cal_sum(size):
    from random import random
    li = [random() for i in range(size)]
    return sum(li)


if __name__ == '__main__':
    # 打印一下1000000个的和，同时会显示执行时间
    print(cal_sum(1000000))