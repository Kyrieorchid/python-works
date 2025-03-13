#functools.partial 就是把某函数的部分partial参数给固定住
import functools

int2 = functools.partial(int, base = 2)
print(int2('1111'))
print(int2('1111', base = 10))