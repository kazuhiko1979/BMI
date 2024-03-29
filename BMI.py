from tkinter import *


class Application(Tk):
    def __init__(self):
        super().__init__()
        # self.createWidgets()
        # self= Tk()
        self.title("BMI Calculator")
        self.configure(width=100, height=100)
        self.configure(bg="black")

        def calc():
            BMI = BMI_val(mass.get(), height.get())
            Stat = getStatus(BMI)
            stat.set(Stat)
            bmi_Val.set(format(BMI, ".2f"))

        def BMI_val(mass, height):
            # return mass / height ** 2
            return mass / ((height / 100) ** 2)
        def getHeight():
            return height

        def getWidth():
            return mass

        def clear():
            stat.set('')
            bmi_Val.set('0.0')
            mas.delete(0, 'end')
            heigh.delete(0, 'end')

        def getStatus(bmi):
            if bmi > 40:
                return "You are Obess Class 3"
            elif 35 <= bmi < 40:
                return "Your are Obess Class 2"
            elif 27 <= bmi < 35:
                return "Your are OverWeight"
            elif 18.5 <= bmi < 27:
                return "Your are Normal"
            elif 17 <= bmi < 18.5:
                return "Your are Mild Thin"
            else:
                return "You are Moderately Thin"

        height = DoubleVar()
        h_label = Label(self, text="Height", fg="red", bg="black", font=("Calibri 14 bold"),
                        pady=5, padx=8)
        heigh = Entry(self, textvariable=height)
        h_label.grid(row=2)
        heigh.grid(row=2, column=1, columnspan=2, padx=5)

        mass = DoubleVar()
        w_label = Label(self, text="Mass", fg="red", bg="black", font=("Calibri 14 bold"),
                        pady=10, padx=2)

        mas = Entry(self, textvariable=mass)
        w_label.grid(row=4)
        mas.grid(row=4, column=1)

        bmi_Val = DoubleVar()
        stat = StringVar()
        bmi = Label(self, text="BMI: ", fg="blue", bg="black", font="Calibri 14 bold", padx=2,
                    pady=10, justify=LEFT)
        status = Label(self, text="Status", fg="blue", bg="black", font="Calibri 14 bold", padx=2,
                    pady=10)

        status_msg = Label(self, textvariable=stat, fg="white", bg="black", font="Calibri 14 bold",
                           pady=10, padx=2)

        BMI_total = Label(self, textvariable=bmi_Val, fg="white", bg="black", font="Calibri 14 bold",
                           pady=10, padx=2)
        bmi.grid(row=6)
        status.grid(row=7)
        BMI_total.grid(row=6, column=1)
        status_msg.grid(row=7, column=1)

        calculate = Button(self, text="Calculate", command=calc, fg="black", bg="white", font="Calibri 14 bold")
        clear = Button(self, text="Reset", command=clear, fg="black", bg="white", font="Calibri 14 bold")

        calculate.grid(row=8)
        clear.grid(row=8, column=3)



app = Application()
app.mainloop()



