import tkinter
import tkinter.font
import tkinter.messagebox


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
class VehiclesGUI:
    def __init__(self,veh):
        self.main_window = tkinter.Tk()
        self.main_window.title('GUI for Vehicles')
        my_font = tkinter.font.Font(family='Arial',size=11)
        my_font2 = tkinter.font.Font(family='Arial', size=12, weight='bold')
        self.top_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.veh = veh

        self.check_var1 = tkinter.IntVar()
        self.check_var1.set(0)
        self.check_var2 = tkinter.IntVar()
        self.check_var2.set(0)
        self.check_var3 = tkinter.IntVar()
        self.check_var3.set(0)
        self.check_var4 = tkinter.IntVar()
        self.check_var4.set(0)
        self.check_var5 = tkinter.IntVar()
        self.check_var5.set(0)
        self.check_var6 = tkinter.IntVar()
        self.check_var6.set(0)
        self.check_var7 = tkinter.IntVar()
        self.check_var7.set(0)
        self.check_var8 = tkinter.IntVar()
        self.check_var8.set(0)
        self.total_cost = 0
        self.check_var9 = tkinter.IntVar()
        self.check_var9.set(0)
        self.check_var10 = tkinter.IntVar()
        self.check_var10.set(0)
        self.check_var11 = tkinter.IntVar()
        self.check_var11.set(0)

        self.chb1 = tkinter.Checkbutton(self.top_frame, text='SwimAble Vehicles', variable=self.check_var1,font=my_font)
        self.chb2 = tkinter.Checkbutton(self.top_frame, text='MoveAble Vehicles', variable=self.check_var2,font=my_font)
        self.chb3 = tkinter.Checkbutton(self.top_frame, text='FlyAble Vehicles', variable=self.check_var3,font=my_font)
        self.chb4 = tkinter.Checkbutton(self.top_frame, text='The most expensive vehicle', variable=self.check_var4,font=my_font)
        self.chb5 = tkinter.Checkbutton(self.top_frame, text='The cheapest vehicle', variable=self.check_var5,font=my_font)
        self.chb6 = tkinter.Checkbutton(self.top_frame, text='Vehicles with price less 16000 and year after 2000', variable=self.check_var6,font=my_font)
        self.chb7 = tkinter.Checkbutton(self.top_frame, text='Vehicles starting year 2000 till 2010', variable=self.check_var7,font=my_font)
        self.chb8 = tkinter.Checkbutton(self.top_frame, text='Vehicles not elder than 5 years and speed in range from 100 till 200', variable=self.check_var8,font=my_font)
        self.chb9 = tkinter.Checkbutton(self.top_frame, text='Quantity of cars and planes', variable=self.check_var9,font=my_font)
        self.chb10 = tkinter.Checkbutton(self.top_frame, text='Car by the lowest price', variable=self.check_var10,font=my_font)
        self.chb11 = tkinter.Checkbutton(self.top_frame, text='Ships year from 2000 till 2020', variable=self.check_var11,font=my_font)

        self.ok_button = tkinter.Button(self.button_frame, text='Show', command=self.show_result,font=my_font2)
        self.ok_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy,font=my_font2)
        self.quit_button.pack(side='left')

        self.chb1.pack()
        self.chb2.pack()
        self.chb3.pack()
        self.chb4.pack()
        self.chb5.pack()
        self.chb6.pack()
        self.chb7.pack()
        self.chb8.pack()
        self.chb9.pack()
        self.chb10.pack()
        self.chb11.pack()
        self.top_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def show_result(self):
        if self.check_var1.get() == 1:
            self.swims = []
            for v in self.veh:
                if isinstance(v, ISwimAble):
                    self.swims.append(v)
            for s in self.swims:
                tkinter.messagebox.showinfo('Vehicles: ', s.__str__())
        if self.check_var2.get() == 1:
            movers = []
            for v in self.veh:
                if isinstance(v, IMoveAble):
                    movers.append(v)
            for m in movers:
                tkinter.messagebox.showinfo('Vehicles: ', m.__str__())
        if self.check_var3.get() == 1:
            flyers = []
            for f in self.veh:
                if isinstance(f, IFlyAble):
                    flyers.append(f)
            for f in flyers:
                tkinter.messagebox.showinfo('Vehicles: ', f.__str__())

        if self.check_var4.get() == 1:
            max_ = self.veh[0]
            for i in self.veh:
                if i.price > max_.price:
                    max_ = i
            for i in self.veh:
                if i.price == max_.price:
                    tkinter.messagebox.showinfo('The most expensive vehicle: ', i.__str__())
        if self.check_var5.get() == 1:
            min_ = self.veh[0]
            for i in self.veh:
                if i.price < min_.price:
                    min_ = i.price
            tkinter.messagebox.showinfo('The cheapest vehicle: ', min_.__str__())
        if self.check_var6.get() == 1:
            less_price=16000
            after_year=2000
            for i in self.veh:
                if i.price < less_price and i.year >= after_year:
                    tkinter.messagebox.showinfo('The cheapest vehicle: ', i)
        if self.check_var7.get() == 1:
            start_year=2000
            end_year=2010
            for i in self.veh:
                if i.year <= end_year and i.year >= start_year:
                   tkinter.messagebox.showinfo('Vehicles starting year 2000 till 2010: ', i.__str__())
        if self.check_var8.get() == 1:
            age_year=5
            start_speed=100
            end_speed=200
            list_=[]
            curr_year = 2020
            summa_price = 0
            count = 0
            for vehicle in self.veh:
                summa_price += vehicle.price
                count += 1
            average_20_price = summa_price / count
            start_price = average_20_price - (average_20_price * 0.2)
            end_price = average_20_price + (average_20_price * 0.2)
            for vehicle in self.veh:
                if (curr_year - vehicle.year) <= age_year and start_speed < vehicle.speed < end_speed and start_price < vehicle.price < end_price:
                    list_.append(vehicle)
            for v in list_:
                tkinter.messagebox.showinfo('Vehicles starting year 2000 till 2010: ', v.__str__())
        if self.check_var9.get() == 1:
            cars_count = 0
            planes_count = 0
            for vehicle in self.veh:
                if isinstance(vehicle,CCar):
                    cars_count += 1
                elif isinstance(vehicle,CPlane):
                    planes_count += 1
            tkinter.messagebox.showinfo('Cars quantity',cars_count)
            tkinter.messagebox.showinfo('Planes quantity', planes_count)

        if self.check_var10.get() == 1:
            cars=[]
            cars_price_min = 500000
            for vehicle in self.veh:
                if isinstance(vehicle,CCar):
                   cars.append(vehicle)
            for i in cars:
                if i.price <cars_price_min:
                    cars_price_min = i.price
                    tkinter.messagebox.showinfo('Car by lowest price', i)

        if self.check_var11.get() == 1:
            ships=[]
            for vehicle in self.veh:
                if isinstance(vehicle, CShip):
                    ships.append(vehicle)
            for g in ships:
                if 2000 < g.year < 2020:
                    tkinter.messagebox.showinfo('Ships', g)




if __name__ == '__main__':
    veh = [CCar(10000, 150, 2000,4),
           CShip(500000, 70, 2019, 'Odessa', 1050),
           CPlane(1000001, 1050, 2010, 180, 10000),
           Amfibia(10500, 140, 2000, 5),
           BatMobile(500000, 170, 2019, 4, 1050),
           CPlane(1000000, 960, 2020, 200, 10000)
           ]
    my_veh_gui = VehiclesGUI(veh)
