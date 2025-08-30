import tkinter as tk
from tkinter import Entry, messagebox
def calcular ():

    if(tbcel.get() or tbfar.get or tbkel.get()):
        try:
            print("calculando temperatura")
            if(tbcel.get()):
                print("calculando desde celsius")
                ce= float(tbcel.get())
                fa = (ce * 9/5) + 32
                tbfar.delete(0, tk.END)
                tbfar.insert(0, str(round(fa,2)))
                ke=ce + 273.15
                tbkel.delete(0, tk.END)
                tbkel.insert(0, str(round(ke, 2)))
            elif(tbfar.get()):
                print("calculando desde celsius")
                fa= float(tbfar.get())
                ce = (fa - 32) * 5/9
                tbcel.delete(0, tk.END)
                tbcel.insert(0, str(round(fa,2)))
                ke=ce + 273.15
                tbkel.delete(0, tk.END)
                tbkel.insert(0, str(round(ke, 2)))
            elif(tbkel.get()):
                print("calculando desde celsius")
                ke= float(tbcel.get())
                ce = (ke - 274.15)
                tbcel.delete(0, tk.END)
                tbcel.insert(0, str(round(fa,2)))
                fa=(ce * 9/5) + 32
                tbfar.delete(0, tk.END)
                tbfar.insert(0, str(round(ke, 2)))
        except ValueError:
            messagebox.showerror(ttle =" Error", message="tipo de dato ingresado incompatible")
    else:
        messagebox.showwarning(title="advertencia", message="los contenedores estan vacios")

 
def limpiar ():
    print("limpiando")
    tbcel.delete(0,tk.END)
    tbfar.delete(0,tk.END)
    tbkel.delete(0,tk.END)
    messagebox.showinfo("Lmpiando", "se estan borrando los valores")


#crea una ventana pricipal
ventana = tk.Tk()
ventana.title("Conversor Básico de Temperatura")
#etiquetas 
#tk.label(ventana, text="Conversor Básico de Temperatura", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)
lbCelsius =tk.Label(ventana, text="Celsius :")
lbCelsius.grid(row=0, column=0, padx=10, pady=10)

lbFarenheit =tk.Label(ventana, text="Farenheit :")
lbFarenheit.grid(row=1, column=0, padx=10, pady=10)

lbKelvin =tk.Label(ventana, text="Kelvin :")
lbKelvin.grid(row=2, column=0, padx=10, pady=10)

#entrada
tbcel = tk.Entry(ventana)
tbfar= tk. Entry(ventana)
tbkel= tk.Entry(ventana)
tbcel.grid(row=0, column=1, padx=10, pady=10)
tbfar.grid(row=1,column=1, padx =10, pady=10)
tbkel.grid(row=2, column=1, padx=10, pady=10)

#botones
btmCalcular= tk.Button(ventana, text="Calcular", command=calcular)
btmLimpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btmCalcular.grid(row=3, column=0, columnspan=2, pady=10)
btmLimpiar.grid(row=4, column=0, padx=10, pady=10)
btmSalir = tk.Button(ventana, text= "Salir", command = ventana.quit)
btmSalir.grid(row=4, column=1, padx=10, pady=10)


ventana.mainloop()