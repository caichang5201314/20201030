# -*- coding: utf-8 -*-

# def func(x):
#     return x
# 
# def test_one():
#     assert func(3)==3


class  TestGoods():

    def func(self, x):
        return x
 
    def test_one(self):
        assert self.func(3) == 3

        
g = TestGoods()
g.test_one()
