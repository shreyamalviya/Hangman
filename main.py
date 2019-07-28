import time
import random
import os

import tkinter as tk
from PIL import ImageTk, Image

from dictionary import GAME_WORDS, MESSAGES, IMG_PATH


class Game:
    def __init__(self, window):
        self.window = window
        self.playing_word = random.choice(GAME_WORDS)
        self.temp_word = ['_ '*len(self.playing_word)] + ["\n"]
        self.already_guessed = []
        self.wrong = 0
        self.draw_screen()

    def submit_click(self, event):
        state = self.check_progress(self.l)
        self.draw_screen(state)

    def draw_screen(self, state='NEXT'):
        path = IMG_PATH[self.wrong]
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.figure_label = tk.Label(self.window, image=self.img)
        self.figure_label.image = self.img
        self.figure_label.place(relx=.5, rely=.3, anchor='center')
        
        show = ""
        show = show.join(ch for ch in self.temp_word)
        self.word_label = tk.Label(self.window, text=show)
        self.word_label.place(relx=.5, rely=.65, anchor='center')
        
        # show = "Already guessed: "
        show = " ".join(ch for ch in self.already_guessed)
        self.already_label = tk.Label(self.window, text=show)
        self.already_label.place(relx=0.05, rely=.7, anchor='w')

        self.msg_label = tk.Label(self.window, text=MESSAGES[state]['msg'])
        self.msg_label.place(relx=.5, rely=.8, anchor='s')

        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.place(relx=.5, rely=.8, anchor='n')
        self.l = self.guess_entry.get()
    
        self.submit_btn = tk.Button(self.window, text = "Submit")
        self.submit_btn.place(relx=.5, rely=.9, anchor='center')
        self.submit_btn.bind('<Button-1>', self.submit_click)

        self.window.mainloop()

    def check_progress(self, letter):
        state = ''
        if len(letter) == 1:
            letter.lower()
            if letter not in self.already_guessed:
                found = False
                self.already_guessed.append(letter)
                for index, character in enumerate(self.playing_word):
                    if letter == character:
                        found = True
                        self.temp_word[index] = letter.upper() + ' '
                        state = 'CORRECT'
            if not found:
                self.wrong += 1
                state = 'INCORRECT'
                if self.wrong > 5:
                    state = 'GAME_OVER'
        else:
            state = 'INVALID'
        return state


def main():
    window = tk.Tk()
    window.title("Hangman")
    window.geometry('400x400')
    window.resizable(False, False)
    # window.grid_rowconfigure(1, minsize=((1/2)*window.winfo_height()))
    # window.grid_rowconfigure(2, minsize=((1/4)*window.winfo_height()))
    # window.grid_rowconfigure(3, minsize=((1/4)*window.winfo_height()))
    Game(window)
    # window.mainloop()

if __name__ == '__main__':
    main()