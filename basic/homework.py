# -*- coding: utf-8 -*-

# 1+2+3+....+100的和

total = 0
for i in range(1, 101):
    total = i + total

print('1+2+3+....+100的和:%s' % total)

# 100以内能被3整除但是不能被5整除的数
# 把这些数弄成一个列表
num_list = []
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        num_list.append(i)
print("100以内能被3整除但是不能被5整除的数:%s" % num_list)

# 有一个水缸，能装50L水，现在已经有了15L，每次挑水只能挑4L，几次能挑满
total = 0

for i in range(0, 50, 4):
    if i <= 50 - 15:
        total = total + 1

print('%s次可以挑完' % total)

