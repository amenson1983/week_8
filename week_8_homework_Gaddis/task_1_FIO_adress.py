import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.font

class Fio_adress:
    def __init__(self):
        self.main_win = tkinter.Tk()
        self.main_win.geometry('400x300')
        self.main_win.title('Program for task 1')
        my_font = tkinter.font.Font(family='Arial', size=14)
        title_font = tkinter.font.Font(family='Arial', size=16)
        self.top_frame = tkinter.Frame(self.main_win)
        self.button_frame = tkinter.Frame(self.main_win)

        self.label_top_frame = tkinter.Label(self.top_frame,text='User`s information: ',font=title_font)
        self.user_data = tkinter.StringVar()
        self.label_user_data = tkinter.Label(self.top_frame,textvariable=self.user_data,font=my_font)
        self.ok_button = tkinter.Button(self.button_frame, text='Show info', command=self.show_result1,font=my_font)
        self.ok_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_win.destroy,font=my_font)
        self.quit_button.pack(side='left')
        self.top_frame.pack(side='top')
        self.button_frame.pack(side='bottom')
        self.label_top_frame.pack()
        self.label_user_data.pack(side='left')

        tkinter.mainloop()
    def show_result1(self):
        self.user_data.set('City: Zhitomir\nStreet: Zamkova\nIndex: 10014\nBuilding: 1\nFlat: 4')





if __name__ == '__main__':
    my_gui = Fio_adress()

