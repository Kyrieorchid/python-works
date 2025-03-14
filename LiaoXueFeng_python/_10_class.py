class Student0(object):
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.__age = age #private私有
    
    def get_age(self):
        print(self.__age)
    
    def set_age(self, age):
        #可以做参数检查
        self.__age = age

phil = Student0('phil', 90, 24)
#phil.age = 24
#print(phil.age)

'''
需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
不是private变量，所以，不能用__name__、__score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，
这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，
请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了
_Student__name，所以，仍然可以通过_Student__name
来访问__name变量，不同版本会修改成不同的变量名
'''
###################################封装
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        if (gender != 'male' ) and (gender != 'female'):
            print("'male' or 'female', what the hell did you input?")
            return
        self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

bart.set_gender('weaponed helicopter')

print('##################################')#继承与多态
class Animal(object):
    def run(self):
        print("Animal is running.")

class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
        print("Cat is running.")

class Car(object):
    def run(self):
        print("Car is running.")

def run_run(whatEver):
    whatEver.run()
    whatEver.run()
'''多态，只要有run方法，不管是啥都能跑，而静态语言会限定一种传入的类型'''
run_run(Animal())
run_run(Dog())
run_run(Cat())
run_run(Car())

print('#########################################')
'''实例属性属于各个实例所有，互不干扰；

类属性属于类所有，所有实例共享一个属性；'''
class Test():
    name = 'test'   #类属性
    def __init__(self, name):   #创建实例时给实例绑定的实例属性
        self.name = name

class Atrributes():
    count = 0
    def __init__(self, name):
        self.name = name
        Atrributes.count += 1    #每创建一个实例将类属性count++

# 测试:
if Atrributes.count != 0:
    print('测试失败!')
else:
    bart = Atrributes('Bart')
    if Atrributes.count != 1:
        print('测试失败!')
    else:
        lisa = Atrributes('Bart')
        if Atrributes.count != 2:
            print('测试失败!')
        else:
            print('Students:', Atrributes.count)
            print('测试通过!')