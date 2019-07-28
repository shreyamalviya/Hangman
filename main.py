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
        self.temp_word = []
        for _ in range(len(self.playing_word)):
            self.temp_word.append('_ ')
        self.already_guessed = []
        self.wrong = 0
        self.draw_screen()

    def submit_click(self, event):
        self.l = self.guess_entry.get()
        self.guess_entry.delete(0, 'end')
        state, game_end = self.check_progress(self.l)
        self.msg_label['text'] = MESSAGES[state]['msg']
        
        path = IMG_PATH[self.wrong]
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.figure_label = tk.Label(self.window, image=self.img)
        self.figure_label.image = self.img
        self.figure_label.place(relx=.5, rely=.3, anchor='center')
    
        show = "".join(ch for ch in self.temp_word)
        self.word_label['text'] = show

        show = " ".join(ch for ch in self.already_guessed)
        self.already_label['text'] = show

        if game_end == True:
            self.word_label['text'] = self.playing_word.upper()
            self.already_label.destroy()
            self.guess_entry.destroy()
            self.submit_btn.destroy()

    def draw_screen(self, state='NEXT'):
        path = IMG_PATH[self.wrong]
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.figure_label = tk.Label(self.window, image=self.img)
        self.figure_label.image = self.img
        self.figure_label.place(relx=.5, rely=.3, anchor='center')
        
        show = "".join(ch for ch in self.temp_word)
        self.word_label = tk.Label(self.window, text=show)
        self.word_label.place(relx=.5, rely=.65, anchor='center')
        
        show = ''
        show = show + " ".join(ch for ch in self.already_guessed)
        self.already_label = tk.Label(self.window, text=show)
        self.already_label.place(relx=0.05, rely=.7, anchor='w')

        self.msg_label = tk.Label(self.window, text=MESSAGES[state]['msg'])
        self.msg_label.place(relx=.5, rely=.8, anchor='s')

        self.guess_entry = tk.Entry(self.window)
        self.guess_entry.place(relx=.5, rely=.8, anchor='n')
        self.guess_entry.bind('<Return>', self.submit_click)
    
        self.submit_btn = tk.Button(self.window, text = "Submit")
        self.submit_btn.place(relx=.5, rely=.9, anchor='center')
        self.submit_btn.bind('<Button-1>', self.submit_click)

    def check_progress(self, letter):
        state = ''
        if len(letter) == 1 and (ord(letter) in range(65, 91) or\
                                 ord(letter) in range(97, 123)):
            found = False
            if letter.upper() not in self.already_guessed:
                self.already_guessed.append(letter.upper())
                for index, character in enumerate(self.playing_word):
                    if letter.lower() == character:
                        found = True
                        self.temp_word[index] = letter.upper() + ' '
                        state = 'CORRECT'
                        if self.temp_word.count("_ ") == 0:
                            state = 'GAME_WON'
                            return state, True
                if not found:
                    self.wrong += 1
                    state = 'INCORRECT'
                    if self.wrong > 5:
                        state = 'GAME_OVER'
                        return state, True
            elif letter.upper() in self.already_guessed:
                state = 'ALREADY_GUESSED'
                return state, False
        else:
            state = 'INVALID'
        return state, False


def main():
    window = tk.Tk()
    window.title("Hangman")
    window.geometry('600x500')
    window.resizable(False, False)
    Game(window)
    window.mainloop()

if __name__ == '__main__':
    main()