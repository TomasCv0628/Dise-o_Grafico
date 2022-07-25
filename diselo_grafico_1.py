import cmath
from cmath import sqrt
import math
from tkinter import Tk , Label, Button, Frame, Toplevel, Entry, StringVar, INSERT, Text, IntVar, messagebox
import tkinter as tk
from fractions import Fraction


def datos_usuario():
    def imprimir_texto():
        at_resultado.insert(INSERT,"\nBienvenid@ " + str(x.get())+ " nuestro programa se \nbasa en la solución de ecuaciones\nde primer a cuarto grado, espero \nsea de utilidad")
        ventana.destroy() 
    ventana=Toplevel()
    ventana.title("DATOS DEL USUARIO")
    ventana.resizable(False,False)
    ancho_ventana = 450
    alto_ventana = 150
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    ventana.config(bg="PeachPuff2")
    boton_guardar=Button(ventana,text="Guardar",command=imprimir_texto)
    boton_guardar.place(x=185,y=100)


    # Etiqueta Nombre

    label_x= tk.Label(ventana, text = "Usuario:")
    label_x.config(fg="white",bg="PeachPuff2", font = "Arial, 14")
    label_x.place(x=50,y=50)

    # Texto nombre
    x = StringVar()
    usuario=Entry(ventana,textvariable=x)
    usuario.config(font="Arial, 12",bg="white")
    usuario.focus_set()
    usuario.place(x=155,y=50)

def abrirventana_primergrado():
    ventana=Toplevel()
    ventana.title("PRIMER GRADO")
    ancho_ventana = 450
    alto_ventana = 450
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    ventana.config(bg="PeachPuff2")
    ventana.resizable(False,False)
    etiqueta=Label(ventana,text="Bienvenid@, en esta ventana podras resolver \necuaciones de la forma \naX + B = 0", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 90,y= 10)
    boton_atras=Button(ventana,text="Atras",command=ventana.destroy)
    boton_atras.place(x=20,y=350)
    # etiquetas
    a = IntVar()
    b = IntVar()
    bet = Label(ventana,text="B=",bg="PeachPuff2")
    bet.place(x=250,y=150)
    entry_b=Entry(ventana,textvariable=b)
    entry_b.config(font="Arial, 12",bg="white",width= 5)
    entry_b.focus_set()
    entry_b.place(x=285,y=150)
    Aet = Label(ventana,text="A= ",bg="PeachPuff2")
    Aet.place(x= 140,y= 150)
    entry_a=Entry(ventana,textvariable=a)
    entry_a.config(font="Arial, 12",bg="white",width= 5)
    entry_a.focus_set()
    entry_a.place(x=175,y=150)


    resultado = Label(ventana, text="X = ", bg="PeachPuff2")
    resultado.place(x=200,y=240)
  
    # Respuesta

    def res():
        r = -(b.get())/(a.get())
        z = Fraction(r).limit_denominator()
        respuesta.insert(INSERT, str(z))
    respuesta=Text(ventana,width=10,height=1)
    respuesta.place(x=235,y=240)
    boton_resolver=Button(ventana,text="Resolver",command=res)
    boton_resolver.place(x=235,y=280)

    # Limpiar

    def limpiar():
        a.set(0)
        b.set(0)
        respuesta.delete("1.0","end")
    boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
    boton_limpiar.place(x= 235, y= 325)
   
def abrirventana_segundogrado():
    ventana=Toplevel()
    ventana.title("SEGUNDO GRADO")
    ancho_ventana = 450
    alto_ventana = 450
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    ventana.config(bg="PeachPuff2")
    ventana.resizable(False,False)
    etiqueta=Label(ventana,text="Bienvenid@, en esta ventana podras resolver \necuaciones de la forma \nAX² + BX + C = 0", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 100,y= 10)
    boton_atras=Button(ventana,text="Atras",command=ventana.destroy)
    boton_atras.place(x=20,y=350)
    a = IntVar()
    b = IntVar()
    c = IntVar()
    C_label = Label(ventana, text= "C= ",bg="PeachPuff2")
    C_label.place(x= 320 , y= 150)
    Entry_C = Entry(ventana,textvariable=c,width=5)
    Entry_C.place(x= 345 ,y= 150)
    B_label = Label(ventana, text= "B= ",bg="PeachPuff2")
    B_label.place(x= 210 , y= 150)
    Entry_B = Entry(ventana,textvariable=b, width=5)
    Entry_B.place(x= 235 ,y= 150)    
    A_label = Label(ventana, text= "A= ",bg="PeachPuff2")
    A_label.place(x= 100 , y= 150)
    Entry_A = Entry(ventana,textvariable=a,width=5)
    Entry_A.place(x= 125 ,y= 150)
    resultado1 = Label(ventana, text="X1 = ", bg="PeachPuff2")
    resultado1.place(x=200,y=240)
    resultado2 = Label(ventana, text="X2 = ", bg="PeachPuff2")
    resultado2.place(x=200,y=268)

    
    # Respuesta
    

    def res():
        d = float((b.get()*b.get())-(4*(a.get())*(c.get())))
        if d > 0:
            if a != 0:
                if b != 0:
                    x1 = (-(b.get()) + math.sqrt((b.get()*b.get())-(4*(a.get())*(c.get())))) / (2*(a.get()))
                    x2 = (-(b.get()) - math.sqrt((b.get()*b.get())-(4*(a.get())*(c.get())))) / (2*(a.get()))
                    z1 = round(x1,3)
                    z2 = round(x2,3)                    
                    respuesta1.insert(INSERT, str(z1))
                    respuesta2.insert(INSERT, str(z2))
                else: 
                    messagebox.showinfo("ERROR","Lo siento, la ecuacion tiene solucion en los complejos Prueba una ecuación diferente")
                    limpiar()
            else: 
                messagebox.showinfo("ERROR","Lo siento, la ecuacion tiene solucion en los complejos Prueba una ecuación diferente")
                limpiar()        
        else: 
            messagebox.showinfo("ERROR","Lo siento, la ecuacion tiene solucion en los complejos Prueba una ecuación diferente")
            limpiar()

    respuesta1 =Text(ventana,width=10,height=1)
    respuesta1.place(x=235,y=240)
    boton_r1=Button(ventana,text="Resolver",command=res)
    boton_r1.place(x=235,y=300)
    respuesta2=Text(ventana,width=10,height=1)
    respuesta2.place(x=235,y=268)
    def limpiar():
        a.set(0)
        b.set(0)
        c.set(0)
        respuesta1.delete("1.0","end")
        respuesta2.delete("1.0","end")
    boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
    boton_limpiar.place(x= 235, y= 345)

def abrirventana_tercergrado():
    ventana=Toplevel()
    ventana.title("TERCER GRADO")
    ancho_ventana = 450
    alto_ventana = 450
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    ventana.config(bg="PeachPuff2")
    ventana.resizable(False,False)
    etiqueta=Label(ventana,text="Bienvenid@, en esta ventana podras resolver \necuaciones de la forma \nAX³ + BX² + CX + D = 0", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 100,y= 10)
    boton_2=Button(ventana,text="Atras",command=ventana.destroy)
    boton_2.place(x=20,y=350)

    # Entradas
        
    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()

    D_label = Label(ventana, text= "D= ",bg="PeachPuff2")
    D_label.place(x= 355 , y= 150)
    Entry_D = Entry(ventana,textvariable=d,width=5)
    Entry_D.place(x= 375 ,y= 150)
    C_label = Label(ventana, text= "C= ",bg="PeachPuff2")
    C_label.place(x= 245 , y= 150)
    Entry_C = Entry(ventana,textvariable=c,width=5)
    Entry_C.place(x= 265 ,y= 150)
    B_label = Label(ventana, text= "B= ",bg="PeachPuff2")
    B_label.place(x= 135 , y= 150)
    Entry_B = Entry(ventana,textvariable=b, width=5)
    Entry_B.place(x= 155 ,y= 150)    
    A_label = Label(ventana, text= "A= ",bg="PeachPuff2")
    A_label.place(x= 25 , y= 150)
    Entry_A = Entry(ventana,textvariable=a,width=5)
    Entry_A.place(x= 45 ,y= 150)

    # Resultados
    resultado1 = Label(ventana, text="X1 = ", bg="PeachPuff2")
    resultado1.place(x=200,y=240)
    resultado2 = Label(ventana, text="X2 = ", bg="PeachPuff2")
    resultado2.place(x=200,y=268)
    resultado3 = Label(ventana, text="X3 = ", bg="PeachPuff2")
    resultado3.place(x=200,y=296)

    # Respuesta

    def res():
        i = sqrt(-1)
        x1 = -b.get()/(3*a.get()) - (2**(1/3)*(-b.get()**2 + 3*a.get()*c.get()))/(3*a.get()*(-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get() + sqrt(4*(-b.get()**2 + 3*a.get()*c.get())**3 + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get())**2))**(1/3)) + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get() + sqrt(4*(-b.get()**2 + 3*a.get()*c.get())**3 + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get())**2))**(1/3)/(3*2**(1/3)*a.get())
        
        x2 = -b.get()/(3*a.get()) + ((1+i*sqrt(3))*(-b.get()**2 + 3*a.get()*c.get()))/(3*2**(2/3)*a.get()*(-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get() + sqrt(4*(-b.get()**2 + 3*a.get()*c.get())**3 + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get())**2))**(1/3)) - (1-i*sqrt(3))*(-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get() + sqrt(4*(-b.get()**2 + 3*a.get()*c.get())**3 + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get())**2))**(1/3)/(6*2**(1/3)*a.get())
        
        x3 = -b.get()/(3*a.get()) + ((1-i*sqrt(3))*(-b.get()**2 + 3*a.get()*c.get()))/(3*2**(2/3)*a.get()*(-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get() + sqrt(4*(-b.get()**2 + 3*a.get()*c.get())**3 + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get())**2))**(1/3)) - (1+i*sqrt(3))*(-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get() + sqrt(4*(-b.get()**2 + 3*a.get()*c.get())**3 + (-2*b.get()**3 + 9*a.get()*b.get()*c.get() - 27*a.get()**2*d.get())**2))**(1/3)/(6*2**(1/3)*a.get())

        z1 = format(x1,'.3f')
        z2 = format(x2,'.3f')
        z3 = format(x3,'.3f')  
        
        respuesta1.insert(INSERT, str(z1))
        respuesta2.insert(INSERT, str(z2))
        respuesta3.insert(INSERT, str(z3))
    # Entradas_Respuesta

    respuesta1 =Text(ventana,width=20,height=1)
    respuesta1.place(x=235,y=240)
    respuesta2=Text(ventana,width=20,height=1)
    respuesta2.place(x=235,y=268)
    respuesta3=Text(ventana,width=20,height=1)
    respuesta3.place(x=235,y=296)
    boton_r1=Button(ventana,text="Resolver",command=res)
    boton_r1.place(x=235,y=350)

    # Limpiar

    def limpiar():
        a.set(0)
        b.set(0)
        c.set(0)
        d.set(0)
        respuesta1.delete("1.0","end")
        respuesta2.delete("1.0","end")
        respuesta3.delete("1.0","end")    
    boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
    boton_limpiar.place(x= 235, y= 385)

def abrirventana_cuartogrado():

    ventana=Toplevel()
    ventana.title("CUARTO GRADO")
    ancho_ventana = 450
    alto_ventana = 450
    x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    ventana.config(bg="PeachPuff2")
    ventana.resizable(False,False)
    etiqueta=Label(ventana,text="Bienvenid@, en esta ventana podras resolver \necuaciones de la forma \nAX⁴ + BX³ + CX² + DX + E = 0", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 100,y= 10)
    boton_2=Button(ventana,text="Atras",command=ventana.destroy)
    boton_2.place(x=20,y=350)

    # Entradas
        
    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()

    E_label = Label(ventana, text= "E= ",bg="PeachPuff2")
    E_label.place(x= 335 , y= 150)
    Entry_E = Entry(ventana,textvariable=d,width=5)
    Entry_E.place(x= 365 ,y= 150)
    D_label = Label(ventana, text= "D= ",bg="PeachPuff2")
    D_label.place(x= 255 , y= 150)
    Entry_D = Entry(ventana,textvariable=d,width=5)
    Entry_D.place(x= 285 ,y= 150)
    C_label = Label(ventana, text= "C= ",bg="PeachPuff2")
    C_label.place(x= 175 , y= 150)
    Entry_C = Entry(ventana,textvariable=c,width=5)
    Entry_C.place(x= 205 ,y= 150)
    B_label = Label(ventana, text= "B= ",bg="PeachPuff2")
    B_label.place(x= 95 , y= 150)
    Entry_B = Entry(ventana,textvariable=b, width=5)
    Entry_B.place(x= 125 ,y= 150)    
    A_label = Label(ventana, text= "A= ",bg="PeachPuff2")
    A_label.place(x= 15 , y= 150)
    Entry_A = Entry(ventana,textvariable=a,width=5)
    Entry_A.place(x= 45 ,y= 150)

    # Resultados
    resultado1 = Label(ventana, text="X1 = ", bg="PeachPuff2")
    resultado1.place(x=200,y=240)
    resultado2 = Label(ventana, text="X2 = ", bg="PeachPuff2")
    resultado2.place(x=200,y=268)
    resultado3 = Label(ventana, text="X3 = ", bg="PeachPuff2")
    resultado3.place(x=200,y=296)
    resultado3 = Label(ventana, text="X4 = ", bg="PeachPuff2")
    resultado3.place(x=200,y=324)
    # Respuesta
    def error():
        messagebox.showinfo("ERROR", "Lo, sentimos en este momento no podemos solucionar ecuaciones de cuarto grado, prueba con una de grado inferior")
        ventana.destroy()
    # Entradas_Respuesta

    respuesta1 =Text(ventana,width=20,height=1)
    respuesta1.place(x=235,y=240)
    respuesta2=Text(ventana,width=20,height=1)
    respuesta2.place(x=235,y=268)
    respuesta3=Text(ventana,width=20,height=1)
    respuesta3.place(x=235,y=296)
    respuesta3=Text(ventana,width=20,height=1)
    respuesta3.place(x=235,y=324)
    boton_r1=Button(ventana,text="Resolver",command=error)
    boton_r1.place(x=235,y=355)

    # Limpiar

    def limpiar():
        a.set(0)
        b.set(0)
        c.set(0)
        d.set(0)
        respuesta1.delete("1.0","end")
        respuesta2.delete("1.0","end")
        respuesta3.delete("1.0","end")    
    boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
    boton_limpiar.place(x= 235, y= 390)

def cerrar_ventana():
    ventana_principal.destroy()

ventana_principal=Tk()
ventana_principal.resizable(False,False)
ancho_ventana = 600
alto_ventana = 600
x_ventana = ventana_principal.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana_principal.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana_principal.geometry(posicion)
ventana_principal.config(bg = "PeachPuff2")
ventana_principal.title("CALCULADORA DE FUNCIONES")

# INICIO

frame_1=Frame(ventana_principal)
frame_1.place(x=10,y=10)
frame_1.config(width=350, height= 350, bg="PeachPuff4")

titulo = tk.Label(frame_1,text="CALCULADORA \nDE \nECUACIONES")
titulo.config(bg = "PeachPuff4", fg="White", font= "TranscendsGames 42")
titulo.place(x=10,y=75)

frame_2=Frame(ventana_principal)
frame_2.place(x=370, y=10)
frame_2.config(width=220, height=580,bg="PeachPuff3")


frame_3=Frame(ventana_principal)
frame_3.place(x=10,y=370)
frame_3.config(width=350,height=220)

at_resultado=tk.Text(frame_3,width=43,height=13)
at_resultado.place(x=0,y=0)

# Atajos

boton_1=Button(frame_2,text="Primer grado",font="Arial, 12", command=abrirventana_primergrado)
boton_1.place(x=43,y=120)

boton_2=Button(frame_2,text="Segundo grado",font="Arial, 12", command=abrirventana_segundogrado)
boton_2.place(x=43,y=220)

boton_3=Button(frame_2,text="Tercer grado",font="Arial, 12", command=abrirventana_tercergrado)
boton_3.place(x=43,y=320)

boton_4=Button(frame_2,text="Cuarto grado",font="Arial, 12", command=abrirventana_cuartogrado)
boton_4.place(x=43,y=420)

boton_5=Button(frame_2,text="Salir",font="Arial, 12", command=cerrar_ventana)
boton_5.place(x=75,y=520)

boton_iC=Button(frame_2,text="Iniciar Sesión",font="Arial 12",command=datos_usuario)
boton_iC.place(x=50,y=20)

ventana_principal.mainloop()