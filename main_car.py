import time
#导入time,用到系统当前时间
'''使用面向对象的思路实现『停车收费』场景：
1. 车主开车进入停车场，产生停车记录，
2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
3. 车主停车完成，
一段时间(购物、吃饭...)之后，车主驾车准备离开停车场，
4. 车主开车离开车位，修改停车记录，
5. 车主开车到达出口，系统根据停车的时间生成订单，
6. 车主缴纳停车费，
7. 车主离开停车场。
至此，整个停车收费的场景完成。
'''
#定义car类,属性包含车牌号,车主,联系方式,入库时间,出库时间
class Car():
    #模拟,定义车位数,存出车列表
    max_car = 8
    car_lst = []
    def __init__(self, platenumber, owner, contantway, time_start=0, time_end=0):
        self.platenumber = platenumber
        self.owner = owner
        self.contantway = contantway
        self.time_start = time_start
        self.time_end = time_end
#定义进车方法
    def in_car(self):
        if len(self.car_lst) < self.max_car:
            self.time_start = time.time()
            self.car_lst.append(self)
            print('停车成功.')
        else:
            print('车库已满.')
#定义出库方法
    def exit(self):
        a = len(self.car_lst) - 1 if len(self.car_lst) == self.max_car else  len(self.car_lst)
        for i in range(0, a):
            if self.car_lst[i].platenumber == self.platenumber:
                carex = self.car_lst[i]
                self.car_lst.remove(self.car_lst[i])
                carex.time_end = time.time()
                tt = float((carex.time_end - carex.time_start) / 3600)
                print('停车时间%f小时,停车费用%f元.' % (tt, float(tt / 5)))
            else:
                if i == len(self.car_lst) - 1:
                    print('该汽车从未进入， 请联系管理员.')

#主方法
while True:
    chose = input(
        '''
        请选择功能：
        1.停车
        2.出车
        3.退出系统   
        '''
    )
    if chose == '3':
        break
    elif chose == '1':
        if len(Car.car_lst) >= Car.max_car:
            print('车库已满.')
        else:
            pla = input('输入车牌号：')
            own = input('输入车主名：')
            cw = input('输入联系方式：')
            c = Car(pla, own, cw)
            c.in_car()
    elif chose == '2':
        if len(Car.car_lst) == 0:
            print('车库为空， 请联系管理员.')
        else:
            pl = input('输入车牌号：')
            carr = Car(pl, 0, 0)
            carr.exit()
    else:
        print('输入错误，请重新选择.')
    time.sleep(2)
    continue


