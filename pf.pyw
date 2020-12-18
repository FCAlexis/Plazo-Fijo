from tkinter import *
from tkinter import ttk, font


# Funciones
def clicked():

    a = float(entrada.get())
    b = float(entrada1.get())
    c = float(entrada2.get())

    tna = (a * b / 365)

    interes = round((c * tna / 100), 2)

    res = "Interes ganado " + str(interes)

    r.configure(text=res)


# Inicio entorno grafico

window = Tk()


window.title("Plazo fijo")
window.geometry('600x250')

# Titulo
Label(window, text="Calculo plazo fijo", font=("bold", 20)).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Label
lbl = Label(window, text="Interes TNA")
lbl.grid(row=1, column=0, padx=10, sticky=E)
lbl1 = Label(window, text="Cantidad de dias")
lbl1.grid(row=2, column=0, padx=10, sticky=E)
lbl2 = Label(window, text="Importe")
lbl2.grid(row=3, column=0, padx=10, sticky=E)

# Entrada
entrada = Entry(window, width=20)
entrada.grid(row=1, column=1, padx=10, pady=10)
entrada1 = Entry(window, width=20)
entrada1.grid(row=2, column=1, padx=10, pady=10)
entrada2 = Entry(window, width=20)
entrada2.grid(row=3, column=1, padx=10, pady=10)

separ1 = ttk.Separator(window, orient=HORIZONTAL)
separ1.grid(column=0, row=4, columnspan=2, sticky="ew", padx=10, pady=10)
btn = Button(window, text="Procesar", command=clicked).grid(row=5, column=0)


# Separador Vertical
separ2 = ttk.Separator(window, orient=VERTICAL)
separ2.grid(row=1,column=2, rowspan=4, sticky="ns", padx=10, pady=10)


# Resultados
Label(window, text="Resultados", font=("bold", 20)).grid(row=0, column=3, columnspan=2, padx=10, pady=10)

r = lbl = Label(window, text="")
r.grid(row=1, column=3, padx=10)




window.mainloop()
