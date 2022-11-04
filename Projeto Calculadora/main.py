import math
from tkinter import *

#Cores
preto = "#080808" #Cor Preto
branco = "#ffffff" #Cor Branco
azul =  "#4e4961" #Cor Azul
cinza = "#999999" #Cor Cinza
laranja = "#fc9330" #Cor Laranja

#Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("238x320")
janela.config(bg=preto)

#Frame
frameTela = Frame(janela, width=238, height=60, bg=azul)
frameTela.grid(row=0, column=0)

frameCorpo = Frame(janela, width=238, height=260)
frameCorpo.grid(row=1, column=0)

todosValores = ''

def entradadaDados(event):

    global todosValores
    todosValores += str(event)
    #Valor Tela
    valorTexto.set(todosValores)

def calcula():
    global todosValores
    resultado = eval(todosValores)
    valorTexto.set(resultado)
    todosValores = str(resultado)

def limparTela():

    global todosValores
    todosValores = ""
    valorTexto.set("")

def raizQuadrada():
    global todosValores
    resultado = eval(todosValores)
    valorTexto.set(math.sqrt(resultado))
    todosValores = str(math.sqrt(resultado))

#Label

valorTexto = StringVar()
appLabel = Label(frameTela, textvariable=valorTexto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18 italic"), bg=azul, fg=branco)
appLabel.place(x=0, y=0)

#Botões
buttonClear = Button(frameCorpo, command=limparTela, text="C", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonClear.place(x=0, y=0)

buttonMod = Button(frameCorpo, command=lambda: entradadaDados("%"), text="%", width=5,height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonMod.place(x=60, y=0)

buttonRaiz = Button(frameCorpo, command=raizQuadrada, text="√", width=5,height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonRaiz.place(x=120, y=0)

buttonDivisao = Button(frameCorpo, command=lambda: entradadaDados("/"), text="÷", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
buttonDivisao.place(x=180, y=0)

buttonMult = Button(frameCorpo, command=lambda: entradadaDados("*"), text="*", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonMult.place(x=180, y=52)

buttonSub = Button(frameCorpo, command=lambda: entradadaDados("-"), text="-", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSub.place(x=180, y=104)

buttonSoma = Button(frameCorpo, command=lambda: entradadaDados("+"), text="+", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonSoma.place(x=180, y=156)

buttonIgual = Button(frameCorpo, command=calcula, text="=", width=5, height=2, bg=laranja, fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonIgual.place(x=180, y=208)

buttonPonto = Button(frameCorpo, command=lambda: entradadaDados("."), text=".", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
buttonPonto.place(x=120, y=208)

button0 = Button(frameCorpo, command=lambda: entradadaDados("0"), text="0", width=11, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button0.place(x=0, y=208)

button_1 = Button(frameCorpo, command=lambda: entradadaDados("1"), text="1", width=5, height=2, bg=cinza, font=('Ivt 13 bold'), relief=RAISED, overrelief=RIDGE)
button_1.place(x=0, y=156)

button_2 = Button(frameCorpo, command=lambda: entradadaDados("2"), text="2", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_2.place(x=60, y=156)

button_3 = Button(frameCorpo, command=lambda: entradadaDados("3"), text="3", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_3.place(x=120, y=156)

button_4 = Button(frameCorpo, command=lambda: entradadaDados("4"), text="4", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_4.place(x=0, y=104)

button_5 = Button(frameCorpo, command=lambda: entradadaDados("5"), text="5", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_5.place(x=60, y=104)

button_6 = Button(frameCorpo, command=lambda: entradadaDados("6"), text="6", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_6.place(x=120, y=104)

button_7 = Button(frameCorpo, command=lambda: entradadaDados("7"), text="7", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_7.place(x=0, y=52)

button_8 = Button(frameCorpo, command=lambda: entradadaDados("8"), text="8", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_8.place(x=60, y=52)

button_9 = Button(frameCorpo, command=lambda: entradadaDados("9"), text="9", width=5, height=2, bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
button_9.place(x=120, y=52)

janela.mainloop()