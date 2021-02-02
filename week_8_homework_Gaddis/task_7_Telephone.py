import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import font

class MytelefoneGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        my_font = tkinter.font.Font(family='Arial', size=14)
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        self.gross_minutes_prompt_label = tkinter.Label(self.bottom_frame, text="Время разговора: ", font=my_font)
        self.gross_minutes_entry = tkinter.Entry(self.bottom_frame, width=10, font=my_font)
        self.gross_minutes_prompt_label.pack(side='left')
        self.gross_minutes_entry.pack(side='left')

        self.rb1 = tkinter.Radiobutton(self.top_frame,text='Дневное время: с 6:00 до 17:59',variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, text='Вечернее время: с 18:00 до 23:59', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, text='Непиковое время: с полуночи до 5:59', variable=self.radio_var, value=3)



        self.ok_button = tkinter.Button(self.button_frame, text='OK', command=self.show_result)
        self.ok_button.pack(side='left')

        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.quit_button.pack(side='left')

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()


        tkinter.mainloop()

    def show_result(self):
        self.total_cost = 0

        rate1 = 10
        rate2 = 12
        rate3 = 5
        if self.radio_var.get() == 1:
            self.total_cost = rate1 * int(self.gross_minutes_entry.get())
            tkinter.messagebox.showinfo('BILL:','Общая стоимость '+ str(self.total_cost) + ' грн')
        if self.radio_var.get() == 2:
            self.total_cost = rate2 * int(self.gross_minutes_entry.get())
            tkinter.messagebox.showinfo('BILL:','Общая стоимость '+ str(self.total_cost) + ' грн')
        if self.radio_var.get() == 3:
            self.total_cost = rate3 * int(self.gross_minutes_entry.get())
            tkinter.messagebox.showinfo('BILL:','Общая стоимость '+ str(self.total_cost) + ' грн')

if __name__ == '__main__':
    my_gui = MytelefoneGUI()