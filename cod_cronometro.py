from tkinter import *
import tkinter as tk

janela = Tk()
janela.title("Cronômetro")
janela.geometry('310x190')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background='black')
janela.tk.call('wm', 'iconphoto', janela._w, tk.PhotoImage(file='cronometro/cronometro.png'))


global tempo
tempo = '00:00:00'

count = -3
run = False


# Funcao iniciar
def iniciar():
    def valor():
        if run:
            global count
            global tempo
            # antes de comecar
            if count <= -1:
                inicio = "começando em " + str(abs(count))
                label_time['text'] = inicio
                label_time['font'] = 'Arial 25'
            else:
                label_time['font'] = 'Arial 50'
                d = str(tempo)
                h, m, s = map(int, d.split(":"))
                h = int(h)
                m = int(m)
                s = int(count)

                if(s == 59):
                    count = -1
                    m += 1

                s = str(0)+str(s)
                m = str(0)+str(m)
                h = str(0)+str(h)

                d = str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
                label_time['text'] = d
                tempo = d

                s = int(count)
                m = int(m)
                h = int(h)

            label_time.after(1000, valor)
            count += 1
    valor()

# Funcao para iniciar cronômetro
def start():
    global run
    run = True
    iniciar()

# Funacao para pausar
def stop():
    global run
    run = False

# funcao para reiniciar
def reset():
    global count
    count = -3

    # Se estiver pausado ira reiniciar do zero
    if run == False:
        global tempo
        tempo = '00:00:00'
        label_time['text'] = tempo

    # Se nao estiver pausado ira continuar onde parou antes
    else:
        label_time['font'] = 'Times 30 '
        label_time['text'] = 'Iniciando...'

label_time = Label(janela, text=tempo, font=(
    'Arial 50'), bg='black', fg='white')
label_time.grid(row=0, column=0, sticky=NSEW, padx=15, pady=20)

frameBaixo = Frame(janela, width=310, height=350, bg='black', relief="flat")
frameBaixo.grid(row=1, column=0, pady=0, padx=30, sticky=NSEW)

botao_iniciar = Button(frameBaixo, command=start, text="Iniciar", width=10, height=2,
                     bg='green', fg='white', font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_iniciar.grid(row=0, column=0, sticky=NSEW, padx=2, pady=10)

botao_pausar = Button(frameBaixo, command=stop, text="Pausar", width=10, height=2,
                    bg='red', fg='white', font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_pausar.grid(row=0, column=1, sticky=NSEW, padx=2, pady=10)

botao_reiniciar = Button(frameBaixo, command=reset, text="Reiniciar", width=10, height=2,
                     bg='blue', fg='white', font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
botao_reiniciar.grid(row=0, column=2, sticky=NSEW, padx=2, pady=10)


janela.mainloop()
