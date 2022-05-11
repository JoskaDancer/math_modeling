from tkinter import *
def chislo():
    window = Tk()
    window.title("Добро")
    window.geometry('600x250')
    window.mainloop()

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
lbl = Label(window, text="привет", font=("Book Antiqua", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Нажми", bg="blue", fg="black",command=chislo)
btn.grid(column=1, row=0)
window.geometry('600x250')
window.mainloop()
