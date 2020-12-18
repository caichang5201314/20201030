# -*- coding: utf-8 -*-
import random

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

# 写一个竞猜游戏，用户必须猜一个秘密的数字，在每次猜完后程序会告诉用户他猜的数是太大了还是太小了，
# 直到猜测正确，最后打印出猜测的次数。如果用户连续猜测同一个数字则只算一次。

me = random.randint(1, 100)
total = 0
print(me)
for i in range(1001):
    guess = int(input('请输入你要猜测的数（1-100包含1和100）：'))
    if guess > me:
        total = total + 1
        print('大了')
    elif guess < me:
        total = total + 1
        print('小了')
    else:
        total = total + 1
        print('猜对了，喝酒吧,我们测了%s次才正确' % total)
        break

