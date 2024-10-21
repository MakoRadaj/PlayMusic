import tkinter as tk
from tkinter import filedialog
import pygame
from pygame import mixer
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Odtwarzacz muzyczny")
        master.configure(bg="#5d5c61") 

        self.playlist = []
        self.current_song_index = -1

        mixer.init()  

        self.create_ui()

    def create_ui(self):
  
        self.play_icon = tk.PhotoImage(file="files\play.png")
        self.stop_icon = tk.PhotoImage(file="files\stop.png")
        self.add_icon = tk.PhotoImage(file="files\plus.png")

        playlist_frame = tk.Frame(self.master, bg="#379683", bd=0, relief="flat")
        playlist_frame.grid(row=0, column=0, columnspan=5, pady=10, padx=10, sticky="ew")
        self.listbox = tk.Listbox(playlist_frame, selectmode=tk.SINGLE, bg="#379683", selectbackground="#7395ae",
                                  bd=0, highlightthickness=0, relief="flat", font=("Helvetica", 12), fg="#333333")
        self.listbox.pack(fill="both", expand=True, ipadx=5, ipady=5, padx=5, pady=5, side="left")


        self.listbox.configure(highlightthickness=0, relief='flat')


        buttons_frame = tk.Frame(self.master, bg="#5d5c61")
        buttons_frame.grid(row=1, column=0, columnspan=5, pady=5, padx=10)
        button_color = "#379683" 
        self.add_button = tk.Button(buttons_frame, image=self.add_icon, command=self.add_song, padx=10, pady=5,
                                     bg=button_color, bd=0, highlightthickness=0, relief="flat")
        self.add_button.pack(side="left", padx=10)

        self.play_button = tk.Button(buttons_frame, image=self.play_icon, command=self.play_music, padx=10, pady=5,
                                      bg=button_color, bd=0, highlightthickness=0, relief="flat")
        self.play_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(buttons_frame, image=self.stop_icon, command=self.stop_music, padx=10, pady=5,
                                      bg=button_color, bd=0, highlightthickness=0, relief="flat")
        self.stop_button.pack(side="left", padx=10)


        volume_frame = tk.Frame(self.master, bg="#379683")
        volume_frame.grid(row=2, column=0, columnspan=5, pady=10, padx=10, sticky="ew")
        self.volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume,
                                       bg="#379683", bd=0, highlightthickness=0, troughcolor="#7395ae", relief="flat", sliderrelief="flat", sliderlength=30)
        self.volume_slider.set(50)  
        self.volume_slider.pack(fill="both", expand=True, ipadx=5, ipady=5, padx=5, pady=5, side="left")

       
        self.volume_slider.configure(highlightthickness=0, bd=0)


        self.current_label = tk.Label(self.master, text="Aktualnie odtwarzany utwór: ", anchor="w", justify="left",
                                       bg="#5d5c61", fg="#333333")
        self.current_label.grid(row=3, column=0, columnspan=5, pady=5, padx=10, sticky="w")

    def add_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            file_name = os.path.basename(file_path)
            self.playlist.append(file_path)
            self.listbox.insert(tk.END, file_name) 

    def play_music(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            self.current_song_index = selected_index
            file_path = self.playlist[selected_index]
            mixer.music.load(file_path)
            mixer.music.play()
            self.update_current_label(file_path)

    def stop_music(self):
        mixer.music.stop()
        self.update_current_label("")

    def set_volume(self, val):
        volume = int(val)
        mixer.music.set_volume(volume / 100) 

    def update_current_label(self, file_path):
        if file_path:
            file_name = os.path.basename(file_path)
            self.current_label.config(text=f"Aktualnie odtwarzany utwór: {file_name}")
        else:
            self.current_label.config(text="Aktualnie odtwarzany utwór: ")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
