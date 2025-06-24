import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import threading
import sys
import os
import winsound

def load_image(url, size):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

def play_beep(frequency, duration):
    threading.Thread(target=winsound.Beep, args=(frequency, duration), daemon=True).start()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class SciFiCronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("CRONÔMETRO - STAR COMMAND")
        self.root.configure(bg="#0a0a0a")
        self.tempo_decorrido = 0
        self.rodando = False

        self.display = tk.Label(root, text="00:00:00", font=("Consolas", 48, "bold"),
                                fg="#00FFCC", bg="#0a0a0a")
        self.display.pack(pady=20)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("StarCommand.Horizontal.TProgressbar", troughcolor="#111111", bordercolor="#222222",
                        background="#00FFCC", lightcolor="#00FFCC", darkcolor="#00AA88")

        self.energy_bar = ttk.Progressbar(root, style="StarCommand.Horizontal.TProgressbar",
                                          orient="horizontal", mode="determinate", length=300, maximum=100)
        self.energy_bar.pack(pady=10)

        # Botões com imagens externas
        self.img_start = load_image("https://cdn-icons-png.flaticon.com/512/786/786425.png", (60, 60))
        self.img_pause = load_image("https://cdn-icons-png.flaticon.com/512/786/786426.png", (60, 60))
        self.img_reset = load_image("https://cdn-icons-png.flaticon.com/512/786/786427.png", (60, 60))

        btn_frame = tk.Frame(root, bg="#0a0a0a")
        btn_frame.pack(pady=10)

        self.btn_start = tk.Button(btn_frame, image=self.img_start, command=self.start, bg="#0a0a0a", borderwidth=0, activebackground="#112233")
        self.btn_start.grid(row=0, column=0, padx=10)

        self.btn_pause = tk.Button(btn_frame, image=self.img_pause, command=self.pause, bg="#0a0a0a", borderwidth=0, activebackground="#112233")
        self.btn_pause.grid(row=0, column=1, padx=10)

        self.btn_reset = tk.Button(btn_frame, image=self.img_reset, command=self.reset, bg="#0a0a0a", borderwidth=0, activebackground="#112233")
        self.btn_reset.grid(row=0, column=2, padx=10)

        self.update_timer()
        self.update_energy_bar()

    def update_timer(self):
        if self.rodando:
            self.tempo_decorrido += 1
        horas, resto = divmod(self.tempo_decorrido, 3600)
        minutos, segundos = divmod(resto, 60)
        self.display.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
        self.root.after(1000, self.update_timer)

    def update_energy_bar(self):
        if self.rodando:
            current = self.energy_bar["value"]
            next_value = (current + 5) % 105
            self.energy_bar["value"] = next_value
        self.root.after(100, self.update_energy_bar)

    def start(self):
        self.rodando = True
        play_beep(1200, 150)

    def pause(self):
        self.rodando = False
        play_beep(800, 150)

    def reset(self):
        self.rodando = False
        self.tempo_decorrido = 0
        self.display.config(text="00:00:00")
        self.energy_bar["value"] = 0
        play_beep(600, 300)

if __name__ == "__main__":
    root = tk.Tk()
    app = SciFiCronometro(root)
    root.mainloop()
