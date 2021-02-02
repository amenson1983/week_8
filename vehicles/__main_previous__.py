from vehicles.cpoint_class import CPoint
from vehicles.vehicle_class import CVehicle


class CCar:
    def __init__(self,price,speed,year):
        CVehicle.__init__(self,price,speed,year)
    def __str__(self):
        return f"{CVehicle.__str__(self)}"
    def __repr__(self):
        return f"{CVehicle.__repr__(self)}"


class CShip:
    def __init__(self, price, speed, year, port, passangers):
        CVehicle.__init__(self, price, speed, year)
        self.port = port
        self.passangers = passangers

    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passangers}"
    def __repr__(self):
        return f"{CVehicle.__str__(self)}, {self.port}, {self.passangers}"


class CPlane:
    def __init__(self, price, speed, year,passangers, height):
        CVehicle.__init__(self, price, speed, year)
        self.height = height
        self.passangers = passangers



    def __str__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"
    def __repr__(self):
        return f"{CVehicle.__str__(self)}, {self.height}, {self.passangers}"

# 1. + вывести на екран механизм с наибольшей ценой
# 2. + получить механизм с наименьшей ценой
# 3. + получить механизм с ценой меньше 16000
# после 2000 года
# 4. + получить масив механизмов год
# выпуска с 2000 по 2010
# 5. + получить масив механизмов не
# старше 5 лет с средней ценой(+- 20%)
# и скоростью в диапазоне от 100 до 200
#6. + в масиве механизмов получить количество Car
#и Plane
#7. + получить из масива механизмов Car с
#наименьшей ценой
#8. + получить из масива механизмов масив Ship год
#выпуска с 2000 по 2010

class Vehicles:
    def __init__(self, vehicles_):
        self.vehicles_ = vehicles_

    def print_maxprice_vehicle(self):
        max_ = self.vehicles_[0]
        for i in self.vehicles_:
            if i.price > max_.price:
                max_ = i
        for i in self.vehicles_:
            if i.price == max_.price:
                print('The most expensive vehicle: ', i)



    def get_minprice_vehicle(self):
        min_ = self.vehicles_[0]
        for i in self.vehicles_:
            if i.price < min_.price:
                min_ = i.price
        return min_

    def get_price_less_after_vehicle(self, less_price=16000, after_year=2000):
        for i in self.vehicles_:
            if i.price < less_price and i.year >= after_year:
                return i

    def get_vehicles_in_range(self, start_year=2000, end_year=2010,list_=[]):
        for i in self.vehicles_:
            if i.year <= end_year and i.year >= start_year:
                list_.append(i)
        return list_

    def get_vehicles_less_with_aver_price_and_speed_in_range(self,age_year=5,start_speed=100, end_speed=200,list_=[]):
        curr_year = 2020
        summa_price = 0
        count = 0
        for vehicle in self.vehicles_:
            summa_price += vehicle.price
            count += 1
        average_20_price = summa_price / count
        start_price = average_20_price - (average_20_price*0.2)
        end_price = average_20_price + (average_20_price * 0.2)
        for vehicle in self.vehicles_:
            if (curr_year - vehicle.year) <= age_year and start_speed<vehicle.speed<end_speed and start_price<vehicle.price<end_price:
                list_.append(vehicle)
        return list_

    def get_cars_and_planes_quantity(self):
        cars_count = 0
        planes_count = 0
        for vehicle in self.vehicles_:
            if isinstance(vehicle,CCar):
                cars_count += 1
            elif isinstance(vehicle,CPlane):
                planes_count += 1
        return cars_count, planes_count

    def get_car_by_lowest_price(self, cars=[], lowest=[]):
        cars_price_min = 500000
        for vehicle in self.vehicles_:
            if isinstance(vehicle,CCar):
               cars.append(vehicle)
        for i in cars:
            if i.price <cars_price_min:
                cars_price_min = i.price
                lowest.append(i)
        return lowest

    def get_ships_from_2000_to_2020(self, ships=[], ships_in_range=[]):
        for vehicle in self.vehicles_:
            if isinstance(vehicle,CShip):
               ships.append(vehicle)
        for i in ships:
            if 2000 < i.year < 2020:
                ships_in_range.append(i)
        return ships_in_range

class Test_Vehicle:
    def test_get_minprice_vehicle(self):
        vehicles = Vehicles(
            [CCar(10000, 150, 1995),
             CShip(500000, 70, 2008, 'Odessa', 1050),
             CPlane(1000000, 960, 2020, 200, 10000),
             CCar(15000, 220, 2001),
             CShip(550000, 105, 2019, 'Chernomorsk', 1200),
             CPlane(800000, 780, 2015, 150, 10000),
             ]
        )
        min_price_exp = 10000
        min_price_act = vehicles.get_minprice_vehicle()
        if min_price_exp == min_price_act.price:
            print("Correct")
        else:
            print("Error")

    def test_price_less_after_vehicle(self):
        vehicles = Vehicles(
            [CCar(10000, 150, 1995),
             CShip(500000, 70, 2008, 'Odessa', 1050),
             CPlane(1000000, 960, 2020, 200, 10000),
             CCar(15000, 220, 2001),
             CShip(550000, 105, 2019, 'Chernomorsk', 1200),
             CPlane(800000, 780, 2015, 150, 10000),
             ]
        )
        year_exp = 2001
        price_exp = 15000
        veh_ = vehicles.get_price_less_after_vehicle()
        if price_exp == veh_.price and year_exp == veh_.year:
            print("Correct")
        else:
            print("Error")


if __name__ == '__main__':

    car1 = CCar(10000, 150, 1995)
    ship1 = CShip(500000, 70, 2008, 'Odessa', 1050)
    plane1 = CPlane(1000000, 960, 2020, 200, 10000)
    car2 = CCar(15000, 220, 2001)
    ship2 = CShip(550000, 105, 2019, 'Chernomorsk', 1200)
    plane2 = CPlane(800000, 780, 2015, 150, 10000)

    vehicles = [car1,ship1,plane1,car2,ship2,plane2]
    vehicles_ = Vehicles(vehicles)

    vehicles_.print_maxprice_vehicle()

    min_ = vehicles_.get_minprice_vehicle()
    print('Vehicle with lowest price: ', min_)
    Test_Vehicle().test_get_minprice_vehicle()

    vehs_ = vehicles_.get_price_less_after_vehicle()
    print('Vehicle with a price less than 16 000 and younger than year 2000: ', vehs_)
    Test_Vehicle().test_price_less_after_vehicle()

    list_range = vehicles_.get_vehicles_in_range()
    for i in list_range:
        print('Vehicle with manufacturing date in range from 2000 up to 2010: ', i)

    list_range_year_speed = vehicles_.get_vehicles_less_with_aver_price_and_speed_in_range()
    for i in list_range_year_speed:
        print('Vehicles younger than 5 years, \nin price range +-20% from average \nand speed range from 100 up to 200:\n', i)

    cars_count, planes_count = vehicles_.get_cars_and_planes_quantity()
    print('Number of cars: ', cars_count, '\nNumber of planes: ', planes_count)

    lowestpricecar = vehicles_.get_car_by_lowest_price()
    for i in lowestpricecar:
        print('A Car with a lowest price: ' , i)

    ships_in_range = vehicles_.get_ships_from_2000_to_2020()
    for i in ships_in_range:
        print('Ships from 2000 to 2020 manufacturing year: ', i)