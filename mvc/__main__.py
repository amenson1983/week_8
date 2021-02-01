import tkinter
from tkinter import *
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.main_window, text='Press me, please', command=self.button_react)
        self.my_button.pack(side='top')
        self.quit_button = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)
        self.quit_button.pack(side='bottom')
        self.label1 = tkinter.Label(self.top_frame,text='Мигнуть')
        self.label2 = tkinter.Label(self.top_frame,text='Моргнуть')
        self.label3 = tkinter.Label(self.top_frame, text='Кивнуть')
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame,text='Мигнуть')
        self.label5 = tkinter.Label(self.bottom_frame,text='Моргнуть')
        self.label6 = tkinter.Label(self.bottom_frame, text='Кивнуть')
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def button_react(self):
        tkinter.messagebox.showinfo('Reaction', 'Thank you for pressing button!')







if __name__ == '__main__':
    my_gui = MyGUI()