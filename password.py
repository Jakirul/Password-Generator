import random
import tkinter as passwordGenerator

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTUVWYZ1234567890!£$%^&*()+_-'

root = passwordGenerator.Tk()

canvas1 = passwordGenerator.Canvas(root, width=400, height=300)
canvas1.pack()

# Text saying "Type your Password Length" #
label2 = passwordGenerator.Label(root, text='Type your Password Length:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

# Text saying passwords will be saved to clipboard #
label3 = passwordGenerator.Label(root, text='Note: Newly generated passwords will be copied to clipboard')
label3.config(font=('helvetica', 10))
canvas1.create_window(205, 220, window=label3)

entry1 = passwordGenerator.Entry(root, exportselection=0)

canvas1.create_window(200, 140, window=entry1)


def getPassword():
    x1 = entry1.get()
    pass1 = int(x1)
    password = ''

    for b in range(pass1):
        password += random.choice(characters)

    label4 = passwordGenerator.Label(root, text=password)
    label4.pack()

    label4.clipboard_append(password)


button1 = passwordGenerator.Button(text='Get your password:', command=getPassword)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
