from tkinter import *
import tkinter.messagebox

def mensaje():
    #tkinter.messagebox.showinfo("Me picaron","Probando la funcion")
    try:
        lableResultado['text'] = "Resultado = \n" + entrya.get() + "+" + entryb.get() + "=" + str(float(entrya.get()) + float(entryb.get()))+"\n"+"Resultado = \n" + entrya.get() + "-" + entryb.get() + "=" + str(float(entrya.get()) - float(entryb.get()))+"\n"+"Resultado = \n" + entrya.get() + "/" + entryb.get() + "=" + str(float(entrya.get()) / float(entryb.get()))+"\n"+"Resultado = \n" + entrya.get() + "*" + entryb.get() + "=" + str(float(entrya.get()) * float(entryb.get()))
    except ValueError:
        tkinter.messagebox.showerror("Error","Solamente numeros")
#aquí inicia el código principal
ventana = Tk()
ventana.title('Operaciones Ariméticas amikos')
ventana['bg'] = '#58d1c5'
ventana.geometry('500x500')
labela = Label(ventana,text="introduzca el valor de 'a'", font="BOLD")
labela.place(x = 10 , y = 0)
labelb = Label(ventana,text="introduzca el valor de 'b'", font= "BOLD")
labelb.place(x = 10 , y = 50)
#obtenemos la información de x y y
pos_x = labela.winfo_x()
pos_y = labelb.winfo_y()
nuevoAncho = pos_x + 250
entrya = Entry(ventana, font="BOLD")
entrya.insert(END,"5")
entrya.place(x = nuevoAncho, y = 7)
entryb = Entry(ventana, font="BOLD")
entryb.place(x=nuevoAncho,y=55)
bottonSuma = Button(ventana,text="Operaciones ariméticas", font="BOLD",command = lambda : mensaje())
bottonSuma.place(x= 0, y =150)
lableResultado = Label(ventana, text= "Resultados", font="BOLD")
lableResultado.place(x = 0, y = 200)
#Esta línea siempre va al final de las ventanas. 
ventana.mainloop()
