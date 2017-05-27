# coding=UTF-8

class Robot:
    '''表示有一个带有名字的机器人'''

    # 一个类变量

    population=0


    def __init__(self,name):
        '''初始化数据'''
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population +=1

    @classmethod
    def say_hi(self):
        print('hello world')


Robot.say_hi()
