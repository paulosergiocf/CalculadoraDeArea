#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
from ferramentas import conversoes as cv

fonte = ['Arial 9 bold','Arial 12 bold', 'Arial 10']
cor = {"Fundo":'#252525',"Fonte Padrão":'#f9f9f9',"Fundo Display":'#181818',"ok":'green',"bad":'#D4424F' }

janela = tk.Tk()
janela.title('Conversão de Área')
janela.geometry("350x500")
janela["bg"]=cor["Fundo"]
photo = tk.PhotoImage(file ='icones/icon.png')
janela.iconphoto(False, photo)

digitos = []
menu =''
escolha =[]

def bt_press(e):
    s = ((f'{repr(e.char)}').replace("'",""))
    if s.isalpha():
        pass
    else:
        if s == ',' and ','in digitos:
            pass
        elif s == r'\x08':
            delete()
        elif s == r'\r':
            converter(digitos, menu)
        elif s == r' ':
            pass
        elif s == '':
            delete_all()
        else:
            if len(digitos) <= 20:
                digitos.append(s)
                updateDisplay(digitos)


def tecladoNum(bt):
    if bt == ',' and ','in digitos:
        pass
    else:
        if len(digitos) <= 20:
            digitos.append(bt)
    updateDisplay(digitos)


def updateDisplay(d):
    texto =''.join(d)
    lb_display_input["text"]=texto


def delete():
    if digitos == []:
        delete_all()
    else:
        digitos.pop()
        updateDisplay(digitos)


def delete_all():
    digitos.clear()
    bt_m2["bg"]= bt_alq["bg"] = bt_ha["bg"] = cor["Fundo"];lb_display_r1["text"]='';lb_display_r2["text"]='';lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"]
    updateDisplay(digitos)

def converter(a=0, d=''):
    if a != []:
        numero =''.join(a)
        numero = numero.replace(",",".")
        numero = float(numero)
        if menu == 1:
            lb_display_r1["fg"]=lb_display_r2["fg"]=cor["ok"];lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"]
            lb_display_r1["text"]=cv.M2Format(cv.convHatoM2(numero))
            lb_display_r2["text"]=cv.AlqFormat(cv.convHatoAlq(numero))
        elif menu == 2:
            lb_display_r1["fg"]=lb_display_r2["fg"]=cor["ok"];lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"]
            lb_display_r1["text"]=cv.M2Format(cv.convAlqtoM2(numero))
            lb_display_r2["text"]=cv.HaFormat(cv.convAlqtoHa(numero))
        elif menu == 3:
            lb_display_r1["fg"]=lb_display_r2["fg"]=cor["ok"];lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"]
            lb_display_r1["text"]=cv.HaFormat(cv.convM2toHa(numero))
            lb_display_r2["text"]=cv.AlqFormat(cv.convM2toAlq(numero))
        else:
            lb_display_r1["fg"]=lb_display_r2["fg"]='white'
            lb_display_r1["bg"]=lb_display_r2["bg"]=bt_ha["bg"]= bt_alq["bg"] = bt_m2["bg"]= cor["bad"]
            lb_display_r1["text"]='Erro! Escolha uma'
            lb_display_r2["text"]='das alternativas de conversão'

def check():
    global menu
    menu = var.get()
    if menu == 1:
        bt_ha["bg"]=cor["ok"]; bt_alq["bg"] = bt_m2["bg"]= cor["Fundo"];lb_display_r1["fg"]=lb_display_r2["fg"]=cor["ok"];lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"];lb_display_r1["text"]='';lb_display_r2["text"]=''
    elif menu ==2:
        bt_alq["bg"]=cor["ok"];bt_ha["bg"]  = bt_m2["bg"]= cor["Fundo"];lb_display_r1["fg"]=lb_display_r2["fg"]=cor["ok"];lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"];lb_display_r1["text"]='';lb_display_r2["text"]=''
    elif menu==3:
        bt_m2["bg"]=cor["ok"]; bt_alq["bg"] = bt_ha["bg"] = cor["Fundo"];lb_display_r1["fg"]=lb_display_r2["fg"]=cor["ok"];lb_display_r1["bg"]=lb_display_r2["bg"]=cor["Fundo Display"];lb_display_r1["text"]='';lb_display_r2["text"]=''

container_geral = tk.Frame(janela, bg=cor["Fundo"], padx=20, pady=20)
container_geral.pack()

container_display = tk.Frame(container_geral, bg=cor["Fundo"], padx=20, pady=20)
container_display.pack()
lb_display_input = tk.Label(container_display, bg=cor["Fundo Display"],fg=cor["Fonte Padrão"], text="0", font=fonte[0], width=34, height=3)
lb_display_input.pack()
lb_display_r1 = tk.Label(container_display, bg=cor["Fundo Display"],fg=cor["Fonte Padrão"], text="", font=fonte[0], width=34, height=1)
lb_display_r1.pack()
lb_display_r2 = tk.Label(container_display, bg=cor["Fundo Display"],fg=cor["Fonte Padrão"], text="", font=fonte[0], width=34, height=1)
lb_display_r2.pack()

container_telcadonumerico = tk.Frame(container_geral, bg=cor["Fundo"], padx=20, pady=20)
container_telcadonumerico.pack()

container_telcadonumerico_a = tk.Frame(container_geral, bg=cor["Fundo"], padx=2, pady=2)
container_telcadonumerico_a.pack()
bt_num = tk.Button(container_telcadonumerico_a, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="07", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('7'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_a, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="08", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('8'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_a, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="09", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('9'))
bt_num.pack(side=tk.LEFT)

container_telcadonumerico_b = tk.Frame(container_geral, bg=cor["Fundo"], padx=2, pady=2)
container_telcadonumerico_b.pack()
bt_num = tk.Button(container_telcadonumerico_b, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="04", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('4'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_b, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="05", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('5'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_b, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="06", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('6'))
bt_num.pack(side=tk.LEFT)

container_telcadonumerico_c = tk.Frame(container_geral, bg=cor["Fundo"], padx=2, pady=2)
container_telcadonumerico_c.pack()
bt_num = tk.Button(container_telcadonumerico_c, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="01", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('1'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_c, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="02", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('2'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_c, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="03", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('3'))
bt_num.pack(side=tk.LEFT)

container_telcadonumerico_d = tk.Frame(container_geral, bg=cor["Fundo"], padx=2, pady=2)
container_telcadonumerico_d.pack()
bt_num = tk.Button(container_telcadonumerico_d, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="0", font=fonte[0], width=10, height=2, command=lambda:tecladoNum('0'))
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_telcadonumerico_d, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text=",", font=fonte[0], width=10, height=2, command=lambda:tecladoNum(','))
bt_num.pack(side=tk.LEFT)

container_opcoes = tk.Frame(container_geral, bg=cor["Fundo"], padx=20, pady=20)
container_opcoes.pack()
container_opcoes_a = tk.Frame(container_geral, bg=cor["Fundo"])
container_opcoes_a.pack()
lb_converter_de = tk.Label(container_opcoes_a, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="Selecione o tipo de área a converter", font=fonte[0])
lb_converter_de.pack()
container_opcoes_b = tk.Frame(container_geral, bg=cor["Fundo"])
container_opcoes_b.pack()

var = tk.IntVar()
bt_ha = tk.Radiobutton(container_opcoes_b, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="HA", font=fonte[0], width=10, height=2,variable=var, value=1, command=check)
bt_ha.pack(side=tk.LEFT)

bt_alq = tk.Radiobutton(container_opcoes_b, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="ALQ", font=fonte[0], width=10, height=2,variable=var, value=2, command=check)
bt_alq.pack(side=tk.LEFT)

bt_m2 = tk.Radiobutton(container_opcoes_b, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="M2", font=fonte[0], width=10, height=2,variable=var, value=3, command=check)
bt_m2.pack(side=tk.LEFT)

container_funcoes = tk.Frame(container_geral, bg=cor["Fundo"], padx=10, pady=10)
container_funcoes.pack()

bt_num = tk.Button(container_funcoes, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="C", font=fonte[0], width=10, height=2, command=delete_all)
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_funcoes, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="DEL", font=fonte[0], width=10, height=2,command=delete)
bt_num.pack(side=tk.LEFT)
bt_num = tk.Button(container_funcoes, bg=cor["Fundo"], fg=cor["Fonte Padrão"], text="=", font=fonte[0], width=10, height=2, command=lambda:converter(digitos, menu))

bt_num.pack(side=tk.LEFT)
janela.bind(sequence="<Key>", func=bt_press)
janela.mainloop()
