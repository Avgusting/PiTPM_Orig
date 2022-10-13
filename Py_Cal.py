from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys


class calculate():

    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.root.geometry("360x280")

        self.root.maxsize(405, 260)
        self.root.minsize(405, 260)
        self.root.config(bg="Grey")

        self.resultwindow = Entry(self.root,borderwidth=5, relief=SUNKEN)
        self.resultwindow.grid(row=0,column=0,columnspan=7,pady=6)
        self.resultwindow.config(font=("Arial", 18))
        self.resultwindow.focus_set() 

        self.button1 = Button(self.root, text="1", width=3, command=lambda:self.calc('1'),relief=RAISED,bg='Light blue')
        self.button1.grid(row=1,column=0, padx=3, pady=3)
        self.button1.config(font=("Arial", 18))

        self.button2 = Button(self.root, text="2", width=3, command=lambda:self.calc('2'),relief=RAISED,bg='Light blue')
        self.button2.grid(row=1, column=1, padx=3, pady=3)
        self.button2.config(font=("Arial", 18))

        self.button3 = Button(self.root, text="3", width=3, command=lambda:self.calc('3'),relief=RAISED,bg='Light blue')
        self.button3.grid(row=1, column=2, padx=3, pady=3)
        self.button3.config(font=("Arial", 18))

        self.button4 = Button(self.root, text="4", width=3, command=lambda:self.calc('4'),relief=RAISED,bg='Light blue')
        self.button4.grid(row=2, column=0, padx=3, pady=3)
        self.button4.config(font=("Arial", 18))

        self.button5 = Button(self.root, text="5", width=3, command=lambda:self.calc('5'),relief=RAISED,bg='Light blue')
        self.button5.grid(row=2, column=1, padx=3, pady=3)
        self.button5.config(font=("Arial", 18))

        self.button6 = Button(self.root, text="6", width=3, command=lambda:self.calc('6'),relief=RAISED,bg='Light blue')
        self.button6.grid(row=2, column=2, padx=3, pady=3)
        self.button6.config(font=("Arial", 18))

        self.button7 = Button(self.root, text="7", width=3, command=lambda:self.calc('7'),relief=RAISED,bg='Light blue')
        self.button7.grid(row=3, column=0, padx=3, pady=3)
        self.button7.config(font=("Arial", 18))

        self.button8 = Button(self.root, text="8", width=3, command=lambda:self.calc('8'),relief=RAISED,bg='Light blue')
        self.button8.grid(row=3, column=1, padx=3, pady=3)
        self.button8.config(font=("Arial", 18))

        self.button9 = Button(self.root, text="9", width=3, command=lambda:self.calc('9'),relief=RAISED,bg='Light blue')
        self.button9.grid(row=3, column=2, padx=3, pady=3)
        self.button9.config(font=("Arial", 18))

        self.button0 = Button(self.root, text="0", width=3, command=lambda: self.calc('0'),relief=RAISED,bg='Light blue')
        self.button0.grid(row=4, column=1, padx=3, pady=3)
        self.button0.config(font=("Arial", 18))

        self.button_open = Button(self.root, text="(", width=3, command=lambda: self.calc('('),relief=RAISED, bg='White')
        self.button_open.grid(row=4, column=0, padx=3, pady=3)
        self.button_open.config(font=("Arial", 18))

        self.button_close = Button(self.root, text=")", width=3, command=lambda: self.calc(')'),relief=RAISED, bg='White')
        self.button_close.grid(row=4, column=2, padx=3, pady=3)
        self.button_close.config(font=("Arial", 18))

      

        self.buttonplus = Button(self.root, text="+", width=3, command=lambda:self.calc('+'),relief=RAISED, bg='White')
        self.buttonplus.grid(row=1, column=3, padx=3, pady=3)
        self.buttonplus.config(font=("Arial", 18))

        self.buttonminus = Button(self.root, text="-", width=3, command=lambda:self.calc('-'),relief=RAISED, bg='White')
        self.buttonminus.grid(row=1, column=4, padx=3, pady=3)
        self.buttonminus.config(font=("Arial", 18))

        self.buttondivide = Button(self.root, text="/", width=3, command=lambda:self.calc('/'),relief=RAISED, bg='White')
        self.buttondivide.grid(row=2, column=3, padx=3, pady=3)
        self.buttondivide.config(font=("Arial", 18))

        self.buttonmultiply = Button(self.root, text="*", width=3, command=lambda:self.calc('*'),relief=RAISED, bg='White')
        self.buttonmultiply.grid(row=2, column=4, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))

        self.buttonmultiply = Button(self.root, text="√2", width=3, command=lambda:self.calc('√2'),relief=RAISED, bg='White')
        self.buttonmultiply.grid(row=3, column=4, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))

        self.buttonmultiply = Button(self.root, text="sin", width=3, command=lambda:self.calc('sin'),relief=RAISED, bg='White')
        self.buttonmultiply.grid(row=1, column=6, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))

        self.buttonmultiply = Button(self.root, text="cos", width=3, command=lambda:self.calc('cos'),relief=RAISED, bg='White')
        self.buttonmultiply.grid(row=2, column=6, padx=3, pady=3)
        self.buttonmultiply.config(font=("Arial", 18))


        self.buttoncancel = Button(self.root, text="C", width=6, command=lambda: self.calc('C'),relief=RAISED,bg='#EF5350',fg='white')
        self.buttoncancel.grid(row=3, column=5, columnspan=6, padx=3, pady=3)
        self.buttoncancel.config(font=("Arial", 18))


        self.buttoncancel = Button(self.root, text=".", width=3, command=lambda: self.calc('.'),relief=RAISED, bg='White')
        self.buttoncancel.grid(row=4, column=3, padx=3, pady=3)
        self.buttoncancel.config(font=("Arial", 18))

        self.buttoncancel = Button(self.root, text="n!", width=3, command=lambda: self.calc('n!'),relief=RAISED, bg='White')
        self.buttoncancel.grid(row=3, column=3, padx=3, pady=3)
        self.buttoncancel.config(font=("Arial", 18))

        self.buttondeleteall = Button(self.root, text="±", width=3, command=lambda: self.calc('±'),relief=RAISED, bg='White')
        self.buttondeleteall.grid(row=1, column=5, padx=3, pady=3)
        self.buttondeleteall.config(font=("Arial", 18))

        self.buttondeleteall = Button(self.root, text="π", width=3, command=lambda: self.calc('π'),relief=RAISED, bg='White')
        self.buttondeleteall.grid(row=2, column=5, padx=3, pady=3)
        self.buttondeleteall.config(font=("Arial", 18))

        self.buttonresult = Button(self.root, text="=", width=10,command=lambda:self.calc('='),relief=RAISED,bg='Yellow')
        self.buttonresult.grid(row=4, column=4, padx=3, pady=3, columnspan=3)
        self.buttonresult.config(font=("Arial", 18))

        self.root.mainloop()

    def calc(self, key):
        global memory
        str1 = "-+0123456789.*/)(" 
        if key == "=":
            if self.resultwindow.get()[0] not in str1:
                self.resultwindow.insert(END, "Первый символ - это не число!")
                messagebox.showerror("Ошибка!", "Вы не ввели число!")
            try:
                result = eval(self.resultwindow.get())
                self.resultwindow.insert(END, "=" + str(result))
            except:
                self.resultwindow.insert(END, "Ошибка!")
                messagebox.showerror("Ошибка! Проверьте правильность данных!")


        elif key == "C":
            self.resultwindow.delete(0, END)
    
        elif key == "±":
            if "=" in self.resultwindow.get():
                self.resultwindow.delete(0, END)
            try:
                if self.resultwindow.get()[0] == "-":
                    self.resultwindow.delete(0)
                else:
                    self.resultwindow.insert(0, "-")
            except IndexError:
                pass
    
        elif key == "π":
            self.resultwindow.insert(END, math.pi)
        elif key == "Exit":
            self.root.after(1,self.root.destroy)
            sys.exit
        elif key == "xⁿ":
            self.resultwindow.insert(END, "**")
        elif key == "sin":
            self.resultwindow.insert(END, "=" + str(math.sin(int(self.resultwindow.get()))))
        elif key == "cos":
            self.resultwindow.insert(END, "=" + str(math.cos(int(self.resultwindow.get()))))
        elif key == "(":
            self.resultwindow.insert(END, "(")
        elif key == ")":
            self.resultwindow.insert(END, ")")
        elif key == "n!":
            self.resultwindow.insert(END, "=" + str(math.factorial(int(self.resultwindow.get()))))
        elif key == "√2":
            self.resultwindow.insert(END, "=" + str(math.sqrt(int(self.resultwindow.get()))))
        else:
            if "=" in self.resultwindow.get():
                self.resultwindow.delete(0, END)
            self.resultwindow.insert(END, key)

 

if __name__ == "__main__":
    calculate()