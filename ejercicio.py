from tkinter import *



ventana = Tk()
ventana.geometry("600x500")
ventana.title("Aplicacion")
var=StringVar()

etiqueta =Label(ventana,text= "Calificacion 1")
etiqueta.pack()
cajaTexto1= Entry(ventana)
cajaTexto1.pack()

etiqueta =Label(ventana,text= "Calificacion 2")
etiqueta.pack()
cajaTexto2= Entry(ventana)
cajaTexto2.pack()

etiqueta =Label(ventana,text= "Calificacion 3")
etiqueta.pack()
cajaTexto3= Entry(ventana)
cajaTexto3.pack()

etiqueta =Label(ventana,text= "Examen final")
etiqueta.pack()
cajaTexto4= Entry(ventana)
cajaTexto4.pack()

etiqueta =Label(ventana,text= "Trabajo final")
etiqueta.pack()
cajaTexto5= Entry(ventana)
cajaTexto5.pack()

def calificacion():
    calificacion = a = float(cajaTexto1.get()) + float(cajaTexto2.get()) + float(cajaTexto3.get()) / float(3) * float(0.55)
    calificacion = b = float(cajaTexto4.get()) * float(0.30)
    calificacion = c = float(cajaTexto5.get()) * float(0.15)
    calificacion = float(a) + float(b) + float(c)
    return var.set(calificacion)

boton1= Button(ventana,text="Calcular", command=calificacion)
boton1.pack()
result =Label(ventana, textvariable=var)
result.pack()


ventana.mainloop()