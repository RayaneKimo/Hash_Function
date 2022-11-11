import tkinter as tk
from math import *


def hash (message):
    encoded = ""
    produit = 1

    for i in range(0, len(message)):
        produit = produit * ord(message[i])

    for i in range(1, 19):
        segment = (produit ** i) % 122

        if segment in range(48, 58):
            encoded += chr(segment)
        elif segment in range(1, 48):
            segment = segment % 10 + ord('0')
            encoded += chr(segment)

        elif segment in range(65, 91):
            encoded += chr(segment)

        elif segment in range(58, 65):
            segment = segment % 26 + ord('A')
            encoded += chr(segment)
        elif segment in range(97, 122):
            encoded += chr(segment)
        elif segment in range(91, 97):
            segment = segment % 26 + ord('a')
            encoded += chr(segment)
        elif segment == '0':
            encoded += "z"
    return encoded

def evaluate():
    res.configure(text="Hash  : " + str(hash(entry.get())))


fenetre = tk.Tk()
fenetre.title('Vigener Encoder')
fenetre.geometry("400x160")
tk.Label(fenetre, text="Hasher votre msg en 18 caracteres :").pack(pady=20)
entry = tk.Entry(fenetre)
entry.pack()

res = tk.Label(fenetre)
res.pack()
b2 = tk.Button(fenetre, text='Quitter', command=fenetre.quit)
b2.pack(side=tk.LEFT,padx=40, pady=4)
b2 = tk.Button(fenetre, text='Hash', command=evaluate)
b2.pack(side=tk.RIGHT,padx=40, pady=4)
fenetre.mainloop()