#__slots__, @property, 多重继承, 定制类, 枚举类, 元类
#动态绑定方法和属性；用__slots__限制实例的动态绑定
class Student(object):
    __slots__ = ('name', 'age', 'set_age')
    pass

phil = Student()
phil.age = 24
phil.name = 'phil'
print('name %s, age %s' % (phil.name, phil.age))

def set_age(self, age):
    self.age = age
from types import MethodType
#把set_age()转换为(phil实例的方法)类型
#只绑定到该instance
phil.set_age = MethodType(set_age, phil)
phil.set_age(25)
print('name %s, age %s' % (phil.name, phil.age))

#绑定到class
Student.set_age = set_age

#限制能够动态绑定的属性和方法
'''
class Student(object):
    __slots__ = ('name', 'age', 'set_age')
'''
#如此，Student类只能绑定name和age属性
#但是对子类没有限制
try:
    phil.score = 90
except AttributeError:
    print('atrribute error')

print("###################################")

# @property装饰器，让调用者可以像访问属性一样调用getter、setter函数
class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, _width):
        if(not isinstance(_width, int)):
            print('must be an integar')
            return
        self._width = _width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, _height):
        if(not isinstance(_height, int)):
            print('must be an integar')
            return
        self._height = _height

    @property
    def resolution(self):
        return self._width * self._height
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

print('#################################')
#多重继承
'''蝙蝠类 可以同时继承 飞行类 和 哺乳类，
这样不用在飞行类下面再去分哺乳类，广度代替深度，
像这样 组合出需要的类 的设计叫MinIn，单一继承语言如Java就不能用MixIn'''

print('#################################')
'''定制类：要把类作为某种类型来使用，需要添加特定的方法来实现'''
class Custom(object):
    def __init__(self):
        pass
    def __str__(self): #返回用户视角字符串
        pass
    __repr__ = __str__ #返回调试视角字符串
    def __len__(self): #可用于len()函数
        pass

class Fib(object): #可迭代的fibonacci类
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self): #要作为迭代对象使用类实例，需要定义这个
        return self #含__next__方法，自己就是迭代对象
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
    def __getitem__(self, n): #当成list来用
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a
    
for n in Fib():
    print(n)

for i in range(10):
    print(Fib()[i])
#还可以传入切片对象，需要另外在__getitem__里实现

#__getattr__实现链式调用
class Chain(object):
    def __init__(self, path = ''):
        self._path = path
    def __str__(self):
        return self._path
    __repr__ = __str__

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

print(Chain().status.user.timeline.list)

print('###############################')
#调用实例本身，增加__call__方法，调用类本质上就是调用该方法
class Hehe(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, *args, **kwds):
        print('suprise mXX fXX, it\'s %s' % self.name)

s = Hehe('Michael')
s()
print('########################')
#枚举
from enum import Enum, unique
class Gender(Enum):
    Male = 0 #类属性
    Female = 1

class Student1(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student1('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
