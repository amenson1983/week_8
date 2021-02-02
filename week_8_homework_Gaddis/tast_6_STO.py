import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.font

class MyCheckbuttonGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        my_font = tkinter.font.Font(family='Arial',size=14,weight='bold')

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
        self.total_cost = 0


        self.chb1 = tkinter.Checkbutton(self.top_frame, text='Замена масла - 500 грн', variable=self.check_var1,font=my_font)
        self.chb2 = tkinter.Checkbutton(self.top_frame, text='Смазочные работы - 300 грн', variable=self.check_var2,font=my_font)
        self.chb3 = tkinter.Checkbutton(self.top_frame, text='Промывка радиатора - 700 грн', variable=self.check_var3,font=my_font)
        self.chb4 = tkinter.Checkbutton(self.top_frame, text='Замена жидкости трансмиссии - 1000 грн', variable=self.check_var4,font=my_font)
        self.chb5 = tkinter.Checkbutton(self.top_frame, text='Осмотр - 800 грн', variable=self.check_var5,font=my_font)
        self.chb6 = tkinter.Checkbutton(self.top_frame, text='Замена грушителя - 1300 грн', variable=self.check_var6,font=my_font)
        self.chb7 = tkinter.Checkbutton(self.top_frame, text='Перестановка шин - 300 грн', variable=self.check_var7,font=my_font)

        self.ok_button = tkinter.Button(self.button_frame, text='Calculate cost', command=self.show_result,font=my_font)
        self.ok_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy,font=my_font)
        self.quit_button.pack(side='left')

        self.chb1.pack()
        self.chb2.pack()
        self.chb3.pack()
        self.chb4.pack()
        self.chb5.pack()
        self.chb6.pack()
        self.chb7.pack()
        self.top_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def show_result(self):
        self.message = 'Total cost: \n'
        self.total_cost = 0
        if self.check_var1.get() == 1:
            self.total_cost += 500
        if self.check_var2.get() == 1:
            self.total_cost += 300
        if self.check_var3.get() == 1:
            self.total_cost += 700
        if self.check_var4.get() == 1:
            self.total_cost += 1000
        if self.check_var5.get() == 1:
            self.total_cost += 800
        if self.check_var6.get() == 1:
            self.total_cost += 1300
        if self.check_var7.get() == 1:
            self.total_cost += 1300
        tkinter.messagebox.showinfo('Your total cost: ',self.total_cost)



if __name__ == '__main__':
    my_gui = MyCheckbuttonGUI()