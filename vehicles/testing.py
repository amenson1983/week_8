from vehicles.amfibia_class import Amfibia
from vehicles.batmobile_class import BatMobile
from vehicles.ccar_class import CCar
from vehicles.cplane_class import CPlane
from vehicles.cship_class import CShip
from vehicles.interfaces_class import ISwimAble, IMoveAble, IFlyAble

#9. добавить классы Amfibia, BatMobile
#10. создать интерфейсы
#MoveAble{ int move()},
#SwimAble{ int swim()},
#FlyAble { int fly()}
#и создать три массива
#11. в каждом масиве подсчитать
#среднюю цену,
#максимальную скорость,
#минимальный год выпуска,
#даны GPS-координаты кто ближе к указаной точке.

if __name__ == '__main__':
    veh = [CCar(10000, 150, 2000,4),
           CShip(500000, 70, 2019, 'Odessa', 1050),
           CPlane(1000000, 1050, 2010, 180, 10000),
           Amfibia(10500, 140, 2000, 5),
           BatMobile(500000, 170, 2019, 4, 1050),
           CPlane(1000000, 960, 2020, 200, 10000)
           ]

    swims = []
    for v in veh:
        if isinstance(v,ISwimAble):
            swims.append(v)
    print('**********************************' * 2)
    print('SwimAble vehicles:')
    print('**********************************' * 2)
    for s in swims:
        print(s.__str__())
    movers = []
    for v in veh:
        if isinstance(v,IMoveAble):
            movers.append(v)
    print('**********************************' * 2)
    print('MoveAble vehicles:')
    print('**********************************' * 2)
    for m in movers:
        print(m.__str__())

    flyers = []
    for f in veh:
        if isinstance(f, IFlyAble):
            flyers.append(f)
    print('**********************************' * 2)
    print('FlyAble vehicles:')
    print('**********************************' * 2)
    for f in flyers:
        print(f.__str__())
