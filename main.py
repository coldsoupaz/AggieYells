from tkinter import*
import pygame

root = Tk()
root.title('gordon fck off emporium')
root.iconbitmap('melody.ico')
root.geometry('500x400')

pygame.mixer.init()
pygame.mixer.music.load("off.mp3")


def play():
    pygame.mixer.music.play()
    print("worked")


my_button = Button(root, text="Play it", font=("Helvetica", 32), command=play)
my_button.pack(pady=20)

root.mainloop()

