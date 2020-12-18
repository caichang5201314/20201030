# -*- coding: utf-8 -*-


def total(start, end, step):
    total = 0
    for i in range(start, end, step):
        total = i + total
    
    print('他们的和:%s' % total)

    
def division(start, end, step, can_div, cannot_div):
    num_list = []
    for i in range(start, end, step):
        if i % can_div == 0 and i % cannot_div != 0:
            num_list.append(i)
    print("%s以内能被%s整除但是不能被%s整除的数:%s" % (end - 1, can_div, cannot_div, num_list))
    
# total(5, 51, 3)
# total(5, 51, 5)
# total(5, 51, 1)

division(1, 301, 4, 3, 5)
