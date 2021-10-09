class Person:
    """
      此处是注释， 通过Person.__doc__来调用
    """

    country="China" # public ，无访问隐私, 类属性
    _money=23456 # protected 可以子孙被继承, 类属性
    __sex="Male" # private 不能继承和调用，只能自己用, 类属性， __开始的方法是 私有方法
    def __init__(self,name,age): #只能解释器可以调用,初始化， 实例方法  dunder方法
        self.name=name # 实例属性  带self的是实例
        age=age #左边age是局部变量，右边是形参
    def say_hello(self):#实例方法  必须通过实例来调用。 不能通过类调用
        print(self.name)
        #print(self.age)

# @开始的都叫做装饰器
    @classmethod    #装饰器  ，用classmethod装饰,作用是 把普通函数装饰成了类函数
    def class_func(cls):# 类方法， 指针必须是 cls  存储在类空间， 实例还没有时就已经存在。 可以通过实例来调用
        cls.country="CHINA"
        print("I love {}".format(cls.country))
    @staticmethod  #装饰器  ，用staticmethod 装饰，  存储在类空间， 实例还没有时就已经存在。,作用是 把普通函数装饰成了静态函数
    def static_func(x,y): #静态方法， 归属类。可以通过实例来调用
        print(x+y)
#类里面的属性只在类空间里面存储，实例里面没有，实例里面可以增加属性，保存在实例空间里，调用顺序为 先从实例里面寻找，如没有，再去类里找

p1=Person('tom',20)
p2=Person("peter",25)
p1.say_hello()
print(Person.__doc__)
p1.class_func()  #实例调用类方法
Person.class_func() #类调用类方法
p1.static_func("abc","edf")  #实例调用 静态方法
Person.static_func(3,4) #类调用类方法

#--------------类继承-------------------------------------------
class Teacher(Person):  # 继承，Person为父类，除了__sex="Male"之外，其他的都继承
    pass

Teacher.class_func()
t1=Teacher("Alice",13)
t1.say_hello()
Teacher.static_func(2,3)
print(Teacher.__name__, t1.__dict__)

#  __doc__, __name__

#  @property  作用：把类里面的一个函数装饰成属性
class Student:
    name="~"
    age=18   # 位置1
    def __init__(self):
        self.name="ZHANG"
        age=0 # 位置2

    @property # @property  作用：把类里面的一个函数装饰成属性. 增强安全性，以为是个属性，实际上是方法。 即后面没有小括号了。
    def get_name(self):
        print(self.__name)

s1=Student()
s2=Student()
s1.name="song"  # 更改了该实例的名字
s1.age=30  # 此处的age,与# 位置1，# 位置2 的age没有关系。 实例可以随时增加新的属性
Student.age=20
Student.name="li"
print(s1.name,s1.age, s2.name,s2.age)
# s1.get_name  装饰器的调用

