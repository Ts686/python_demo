# coding=utf-8
# *args 代表把所有传的位置参数接收成列表
# **kwargs 传递参数可能有key-value,都用此参数接收
# 总结：*args可以传入列表，元组。**kwargs可以传入字典作为参数。
def method(*args, **kwargs):
    for key in kwargs:
        print("the key is: %s, and the value is: %s" % (key, kwargs[key]))
    index = 1
    for value in args:
        # print("the " + str(index) + " is:" + str(value))
        # index += 1
        print(type(value), value)


method(1, "helo", ["world", 1, 1.21], (1, "a"), a=1, b=2, **{"aa": "11", "bb": "22"})
# method(1, "helo", *["world", 1, 1.21], *(1,"a"),a=1, b=2, **{"aa": "11", "bb": "22"})
