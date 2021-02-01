import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font

class Translation:
    def __init__(self):
        self.main_win = tkinter.Tk()
        self.main_win.title('Program for task 2')

        my_font = tkinter.font.Font(family='Arial', size=14)

        self.top_frame = tkinter.Frame(self.main_win)
        self.button_frame = tkinter.Frame(self.main_win)

        self.button1 = tkinter.Button(self.button_frame, text='Sinister', command=self.show_trans1,font=my_font)
        self.button2 = tkinter.Button(self.button_frame, text='Dexter', command=self.show_trans2, font=my_font)
        self.button3 = tkinter.Button(self.button_frame, text='Medium', command=self.show_trans3, font=my_font)

        self.button1.pack(side='left')
        self.button2.pack(side='left')
        self.button3.pack(side='left')

        self.translate = tkinter.StringVar()
        self.label_translate = tkinter.Label(self.top_frame,textvariable=self.translate,font=my_font)

        self.top_frame.pack()
        self.label_translate.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show_trans1(self):
        self.translate.set('Левый')
    def show_trans2(self):
        self.translate.set('Правый')
    def show_trans3(self):
        self.translate.set('Центральный')



if __name__ == '__main__':
    tr1 = Translation()