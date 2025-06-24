import tkinter as tk

# Configuração da janela principal
root = tk.Tk()
root.title("Contador de Tempo")
root.geometry("310x190")
root.resizable(False, False)
root.configure(bg='black')
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='cronometro/cronometro.png'))

# Variáveis globais
tempo_atual = '00:00:00'
contador = -3
executando = False

# Função responsável por atualizar o tempo
def atualizar_tempo():
    def contar():
        if executando:
            global contador, tempo_atual

            if contador < 0:
                mensagem = f"Início em {abs(contador)}"
                visor['text'] = mensagem
                visor['font'] = ('Arial', 25)
            else:
                visor['font'] = ('Arial', 50)
                horas, minutos, segundos = map(int, tempo_atual.split(":"))
                segundos = contador

                if segundos == 59:
                    contador = -1
                    minutos += 1

                tempo_atual_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
                visor['text'] = tempo_atual_formatado
                tempo_atual = tempo_atual_formatado

            visor.after(1000, contar)
            contador += 1

    contar()

# Comandos dos botões
def iniciar_contagem():
    global executando
    executando = True
    atualizar_tempo()

def pausar_contagem():
    global executando
    executando = False

def reiniciar_contagem():
    global contador, tempo_atual
    contador = -3
    if not executando:
        tempo_atual = '00:00:00'
        visor['text'] = tempo_atual
    else:
        visor['font'] = ('Times', 30)
        visor['text'] = 'Reiniciando...'

# Interface do visor
visor = tk.Label(root, text=tempo_atual, font=('Arial', 50), bg='black', fg='white')
visor.grid(row=0, column=0, padx=15, pady=20, sticky='nsew')

# Frame com os botões
botoes_frame = tk.Frame(root, bg='black', width=310, height=350)
botoes_frame.grid(row=1, column=0, padx=30, sticky='nsew')

# Botões
btn_iniciar = tk.Button(botoes_frame, text="Iniciar", command=iniciar_contagem,
                        bg='green', fg='white', font=('Ivy', 8, 'bold'), width=10, height=2,
                        relief=tk.RAISED, overrelief=tk.RIDGE)
btn_iniciar.grid(row=0, column=0, padx=2, pady=10)

btn_pausar = tk.Button(botoes_frame, text="Pausar", command=pausar_contagem,
                       bg='red', fg='white', font=('Ivy', 8, 'bold'), width=10, height=2,
                       relief=tk.RAISED, overrelief=tk.RIDGE)
btn_pausar.grid(row=0, column=1, padx=2, pady=10)

btn_reiniciar = tk.Button(botoes_frame, text="Reiniciar", command=reiniciar_contagem,
                          bg='blue', fg='white', font=('Ivy', 8, 'bold'), width=10, height=2,
                          relief=tk.RAISED, overrelief=tk.RIDGE)
btn_reiniciar.grid(row=0, column=2, padx=2, pady=10)

# Início do loop da aplicação
root.mainloop()
