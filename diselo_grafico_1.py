from tkinter import Tk , Label, Button, Frame, Toplevel, Entry, StringVar, INSERT, Text
import tkinter as tk



def abrirventana_1():
    def imprimir_texto():
        at_resultado.insert(INSERT,"\nBienvenid@ " + str(x.get())+ " nuestro programa se \nbasa en la solución de ecuaciones\nde primer a cuarto grado, espero \nsea de utilidad")
        ventana.destroy() 
    ventana=Toplevel()
    ventana.title("DATOS DEL USUARIO")
    ventana.geometry("450x150")
    ventana.config(bg="PeachPuff2")
    boton_2=Button(ventana,text="Guardar",command=imprimir_texto)
    boton_2.place(x=185,y=100)


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



def abrirventana_2():
    ventana=Toplevel()
    ventana.title("PRIMER GRADO")
    ventana.geometry("450x450")
    ventana.config(bg="PeachPuff2")
    etiqueta=Label(ventana,text="Bienvenid@, en esta ventana podras resolver \necuaciones de la forma \naX + B = 0", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 90,y= 10)
    boton_2=Button(ventana,text="Atras",command=ventana.destroy)
    boton_2.place(x=20,y=350)
    # etiquetas
    a = Label(ventana,text="A= ",bg="PeachPuff2")
    a.place(x= 140,y= 150)
    entry_a=Entry(ventana,textvariable=a)
    entry_a.config(font="Arial, 12",bg="white",width= 5)
    entry_a.focus_set()
    entry_a.place(x=175,y=150)
    b = Label(ventana,text="B=",bg="PeachPuff2")
    b.place(x=250,y=150)
    entry_b=Entry(ventana,textvariable=b)
    entry_b.config(font="Arial, 12",bg="white",width= 5)
    entry_b.focus_set()
    entry_b.place(x=285,y=150)
    resultado = Label(ventana, text="X = ", bg="PeachPuff2")
    resultado.place(x=200,y=240)
    # Respuesta

    at_resultado=Text(ventana,width=10,height=1)
    at_resultado.place(x=235,y=240)
    boton_2=Button(ventana,text="Resolver")
    boton_2.place(x=235,y=280)

def abrirventana_3():
    ventana=Toplevel()
    ventana.title("SEGUNDO GRADO")
    ventana.geometry("450x450")
    ventana.config(bg="PeachPuff2")
    etiqueta=Label(ventana,text="Bienvenid@", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 200,y= 10)
    boton_2=Button(ventana,text="Atras",command=ventana.destroy)
    boton_2.place(x=20,y=350)


def abrirventana_4():
    ventana=Toplevel()
    ventana.title("TERCER GRADO")
    ventana.geometry("450x450")
    ventana.config(bg="PeachPuff2")
    etiqueta=Label(ventana,text="Bienvenid@", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 200,y= 10)
    boton_2=Button(ventana,text="Atras",command=ventana.destroy)
    boton_2.place(x=20,y=350)



def abrirventana_5():
    ventana=Toplevel()
    ventana.title("CUARTO GRADO")
    ventana.geometry("450x450")
    ventana.config(bg="PeachPuff2")
    etiqueta=Label(ventana,text="Bienvenid@", bg="PeachPuff4", fg="black")
    etiqueta.place(x= 200,y= 10)
    boton_2=Button(ventana,text="Atras",command=ventana.destroy)
    boton_2.place(x=20,y=350)


def cerrar_ventana():
    ventana_principal.destroy()

texto = "¡Hola Mundo!"
intervalo = 200

texto_auxiliar = texto + " " * len(texto)

def avanza():
    global texto_auxiliar

    ultimo_caracter = texto_auxiliar[len(texto_auxiliar) - 1]
    texto_auxiliar = texto_auxiliar[:-1]
    texto_auxiliar = ultimo_caracter + texto_auxiliar
    ventana_principal.set(texto_auxiliar[0:len(texto)])
    ventana_principal.after(intervalo, avanza)

ventana_principal=Tk()
ventana_principal.resizable(False,False)
ventana_principal.geometry("600x600")
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

boton_1=Button(frame_2,text="Primer grado",font="Arial, 12", command=abrirventana_2)
boton_1.place(x=43,y=120)

boton_2=Button(frame_2,text="Segundo grado",font="Arial, 12", command=abrirventana_3)
boton_2.place(x=43,y=220)

boton_3=Button(frame_2,text="Tercer grado",font="Arial, 12", command=abrirventana_4)
boton_3.place(x=43,y=320)

boton_4=Button(frame_2,text="Cuarto grado",font="Arial, 12", command=abrirventana_5)
boton_4.place(x=43,y=420)

boton_5=Button(frame_2,text="Salir",font="Arial, 12", command=cerrar_ventana)
boton_5.place(x=75,y=520)

boton_iC=Button(frame_2,text="Iniciar Sesión",font="Arial 12",command=abrirventana_1)
boton_iC.place(x=50,y=20)

ventana_principal.mainloop()