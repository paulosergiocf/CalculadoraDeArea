#!/usr/bin/python
#Criado por Paulo Sergio de Campos Filho
#----------modulos--------
from tkinter import *
#----------Cores----------
back_ground = '#252525'
back_ground_2 = '#181818'
back_ground_display = '#151515'
cor_fonte = '#EBEBEB'
cor_ok = 'green'
cor_bad = 'red'
#----------App-----------
janela = Tk()
janela.geometry("300x450")
janela["bg"]=back_ground
janela.title("Calculadora de Área")
photo = PhotoImage(file ='icones/icon.png')
janela.iconphoto(False, photo)
#--------conveções------
digitos = [] # lista que guardará os numeros digitados.
texto ='' # variavel para tratar os numeros da lista.
menu ='' # escolha do calculo.
#--------Funções--------
def frase():
    texto = ''.join(digitos)
    lb_display["text"]=texto #atualizar en_display
#------teclado numerico--------
def bt_01():
    digitos.append('1')
    frase()
def bt_02():
    digitos.append('2')
    frase()
def bt_03():
    digitos.append('3')
    frase()
def bt_04():
    digitos.append('4')
    frase()
def bt_05():
    digitos.append('5')
    frase()
def bt_06():
    digitos.append('6')
    frase()
def bt_07():
    digitos.append('7')
    frase()
def bt_08():
    digitos.append('8')
    frase()
def bt_09():
    digitos.append('9')
    frase()
def bt_00():
    digitos.append('0')
    frase()
def bt_virg():
    digitos.append(',')
    frase()
#-----funções da lista---------
def delete():
    if digitos == []:
        pass
    else:
        digitos.pop()
        frase()
def delete_all():
    digitos.clear()
    frase()
    convert_de["bg"]=back_ground
    bt_m2["bg"]=back_ground;bt_alq["bg"]= back_ground;bt_ha["bg"]= back_ground
    global menu
    menu =''
    lb_display_02["text"]=''
    lb_display_03["text"]=''
#-----calculos--------------
global bt_ha
def bt_ha():
    global menu
    menu = 'ha'
    convert_de["bg"]=back_ground
    bt_ha["bg"]='Green';bt_alq["bg"]= back_ground;bt_m2["bg"]= back_ground;lb_display_02["text"]="";lb_display_03["text"]="";lb_display_02["fg"]=cor_ok
def bt_alq():
    global menu
    menu = 'alq'
    convert_de["bg"]=back_ground
    bt_alq["bg"]='Green';bt_ha["bg"]= back_ground;bt_m2["bg"]= back_ground;lb_display_02["text"]="";lb_display_03["text"]="";lb_display_02["fg"]=cor_ok
def bt_m2():
    global menu
    menu = 'm2'
    convert_de["bg"]=back_ground
    bt_m2["bg"]='Green';bt_alq["bg"]= back_ground;bt_ha["bg"]= back_ground;lb_display_02["text"]="";lb_display_03["text"]="";lb_display_02["fg"]=cor_ok
def bt_igual():
    if digitos == []:
        pass
    else:
        numero = ''.join(digitos)
        numero = numero.replace(",",".")
        numero = float(numero)

        if menu == 'ha':
            resultado_a = ('{:.2f} m²'.format(numero*10000))
            resultado_b = ('{:.2f} Alq Pta'.format( numero/2.42))
            lb_display_02["text"]=resultado_a
            lb_display_03["text"]=resultado_b
        elif menu == 'alq':
            resultado_a = ('{:.4f} ha'.format(numero*2.42))
            resultado_b = ('{:.2f} m²'.format(numero*24200))
            lb_display_02["text"]=resultado_a
            lb_display_03["text"]=resultado_b
        elif menu == 'm2':
            resultado_a = ('{:.4f} ha'.format(numero/10000))
            resultado_b = ('{:.2f} Alq Pta'.format(numero/24200))
            lb_display_02["text"]=resultado_a
            lb_display_03["text"]=resultado_b
        else:
            lb_display_02["text"]="Erro! Escolha uma opção!"
            lb_display_02["fg"]=cor_bad
            convert_de["bg"]=cor_bad
# Teclado
def apertar_o_botao(event):

    texto = f'{repr(event.char)}'
    texto =texto.replace("'","")
    text1 = texto.isalpha()

    if text1 == True:
        pass
    elif texto =='1':
        digitos.append('1')
        frase()
    elif texto =='2':
        digitos.append('2')
        frase()
    elif texto =='3':
        digitos.append('3')
        frase()
    elif texto =='4':
        digitos.append('4')
        frase()
    elif texto =='5':
        digitos.append('5')
        frase()
    elif texto =='6':
        digitos.append('6')
        frase()
    elif texto =='7':
        digitos.append('7')
        frase()
    elif texto =='8':
        digitos.append('8')
        frase()
    elif texto =='9':
        digitos.append('9')
        frase()
    elif texto =='0':
        digitos.append('0')
        frase()
    elif texto ==',':
        digitos.append(',')
        frase()
    elif texto =='.':
        digitos.append(',')
        frase()
    elif texto ==r'\x08':
        delete()
    elif texto ==r'\r':
        bt_igual()
    else:
        pass
#-------Interface--------
container_00 = Frame(janela, bg=back_ground, padx=10, pady=10)
container_00.pack()
container_01 = Frame(container_00, bg= back_ground_display, padx=10, pady=10)
container_01.pack()

lb_display = Label(container_01, text='', bg= back_ground_display, fg=cor_fonte, width=25, height=3, font=('DejaVu Sans Mono', 12))
lb_display.pack()
lb_display_02 = Label(container_01, text='',fg=cor_ok, bg= back_ground_display, width=31, font=('DejaVu Sans Mono', 9))
lb_display_02.pack()
lb_display_03 = Label(container_01, text='',fg=cor_ok, bg= back_ground_display, width=31,  font=('DejaVu Sans Mono', 9))
lb_display_03.pack()

container_02 = Frame(container_00, bg=back_ground, padx=10, pady=10)
container_02.pack()

container_02_op_1 = Frame(container_02, bg=back_ground, padx=10,)
container_02_op_1.pack()
convert_de = Label(container_02_op_1, bg=back_ground, relief=FLAT,fg=cor_fonte, text='converter de', width=20, font=('Arial', 10))
convert_de.pack()
container_02_op_2 = Frame(container_02, bg=back_ground, padx=10)
container_02_op_2.pack()
bt_ha = Button(container_02_op_2,bg=back_ground, fg=cor_fonte, text='ha', font='Arial 10', width=4, command=bt_ha)
bt_ha.pack(side=LEFT)
bt_alq = Button(container_02_op_2,bg=back_ground, fg=cor_fonte, text='Alq', font='Arial 10', width=4, command=bt_alq)
bt_alq.pack(side=LEFT)
bt_m2 = Button(container_02_op_2, bg=back_ground, fg=cor_fonte, text='M²', font='Arial 10', width=4, command=bt_m2)
bt_m2.pack(side=LEFT)

container_03 = Frame(container_00, bg=back_ground, padx=10, pady=10)
container_03.pack()

container_03a = Frame(container_03, bg=back_ground, padx=10)
container_03a.pack()
container_03b = Frame(container_03, bg=back_ground, padx=10)
container_03b.pack()
container_03c = Frame(container_03, bg=back_ground, padx=10)
container_03c.pack()
container_03d = Frame(container_03, bg=back_ground, padx=10)
container_03d.pack()
container_03e = Frame(container_03, bg=back_ground, padx=10, pady=10)
container_03e.pack()
#-------------------Teclado Numerico--------------------
bt_01 = Button(container_03c, text='1',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_01)
bt_01.pack(side=LEFT)
bt_02 = Button(container_03c, text='2',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_02)
bt_02.pack(side=LEFT)
bt_03 = Button(container_03c, text='3',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_03)
bt_03.pack(side=LEFT)
bt_04 = Button(container_03b, text='4',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_04)
bt_04.pack(side=LEFT)
bt_05 = Button(container_03b, text='5',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_05)
bt_05.pack(side=LEFT)
bt_06 = Button(container_03b, text='6',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_06)
bt_06.pack(side=LEFT)
bt_07 = Button(container_03a, text='7',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_07)
bt_07.pack(side=LEFT)
bt_08 = Button(container_03a, text='8',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_08)
bt_08.pack(side=LEFT)
bt_09 = Button(container_03a, text='9',bg=back_ground, fg=cor_fonte,font='Arial 12', width=4, height=1, command=bt_09)
bt_09.pack(side=LEFT)
#
bt_00 = Button(container_03d, text='0', font='Arial 12', bg=back_ground, fg=cor_fonte,width=3, command=bt_00)
bt_00.pack(side=LEFT)
bt_virgula = Button(container_03d, text=',', font='Arial 12', bg=back_ground, fg=cor_fonte,width=3, command=bt_virg)
bt_virgula.pack(side=LEFT)
#-------------------Operações--------------------
bt_del_all = Button(container_03e, text='C', font='Arial 12', width=3, bg=back_ground_2, fg=cor_fonte,command=delete_all)
bt_del_all.pack(side=LEFT)
bt_del = Button(container_03e, text='Del', font='Arial 12', width=3, bg=back_ground_2, fg=cor_fonte,command=delete)
bt_del.pack(side=LEFT)
bt_del_resultado = Button(container_03e, text='=', font='Arial 12', bg=back_ground_2, width=3,fg=cor_fonte, command=bt_igual)
bt_del_resultado.pack(side=LEFT)

janela.bind(sequence="<Key>", func=apertar_o_botao)

mainloop()
