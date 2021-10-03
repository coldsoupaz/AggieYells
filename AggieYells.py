from tkinter import *
import pygame as pyg

root_object = Tk()

root_object.title("Aggie Yell Soundboard")
root_object.geometry("1000x1000")

pyg.mixer.init()



yell_box = Listbox(root_object, bg = "maroon",fg = "white", width = 100, height = 20 )
yell_box.pack(pady = 20)

#This will hold our control menu
player_frame = Frame(root_object)
player_frame.pack()

#These are our control menu buttons
play_image = PhotoImage(file = "Play.png")
play_button = Button(player_frame, image =play_image, borderwidth = 10)
play_button.grid(row = 0, column = 0, padx = 10, pady =10)

pause_image = PhotoImage(file = "Pause.png")
pause_button = Button(player_frame, image =pause_image, borderwidth = 10)
pause_button.grid(row = 0, column = 1, padx = 10, pady = 10)


yell_frame = Frame(root_object)
yell_frame.pack()


# These are the switch case's for our switch case that we use to call the correct audio file
def locomotive():
        pyg.mixer.music.load("c:/Users/colds/PycharmProjects/pythonProject/Locomotive.mp3")
        pyg.mixer.music.play(loops=0)

def old_army():
        pyg.mixer.music.load("c:/Users/colds/PycharmProjects/pythonProject/Old_Army.mp3")
        pyg.mixer.music.play(loops=0)

def farmer():
        pyg.mixer.music.load("c:/Users/colds/PycharmProjects/pythonProject/Farmer.mp3")
        pyg.mixer.music.play(loops=0)

def fifteen_for_team():
        pyg.mixer.music.load("c:/Users/colds/PycharmProjects/pythonProject/FifteenForTeam.mp3")
        pyg.mixer.music.play(loops=0)

def military():
        pyg.mixer.music.load("c:/Users/colds/PycharmProjects/pythonProject/Military.mp3")
        pyg.mixer.music.play(loops=0)

def war_hymn():
        pyg.mixer.music.load("c:/Users/colds/PycharmProjects/pythonProject/Farmer.mp3")
        pyg.mixer.music.play(loops=0)

# map the inputs to the function blocks
yell_options = {0 : old_army,
                1 : locomotive,
                2 : farmer,
                3 : fifteen_for_team,
                4 : military,
                5 : war_hymn,
}


#Song Buttons, these are the buttons the user will use to play the music.
#this one doesn't have a song yet
"""music_button = Button(yell_frame, text= "Aggie Theme", font = ("Arial"), command = yell_options[0])
music_button.grid(row = 0, column =0, padx =10)
"""

old_army_button = Button(yell_frame, text= "Old Army", font = ("Arial"), command = yell_options[0])
old_army_button.grid(row = 0, column = 0, padx=10)

locomotive_button = Button(yell_frame, text= "Locomotive", font = ("Arial"), command = yell_options[1])
locomotive_button.grid(row = 0, column = 1, padx=10)

farmers_button = Button(yell_frame, text= "Farmer Fight", font = ("Arial"), command = yell_options[2])
farmers_button.grid(row=1, column = 0, padx =10)

fifteen_for_team_button = Button(yell_frame, text= "Fifteen for Team", font = ("Arial"), command = yell_options[3])
fifteen_for_team_button.grid(row = 1, column = 1, padx=10)

military_button = Button(yell_frame, text= "Military", font = ("Arial"), command = yell_options[4])
military_button.grid(row=2, column = 0, padx =10)

war_hymn_button = Button(yell_frame, text= "War Hymn", font = ("Arial"), command = yell_options[4])
war_hymn_button.grid(row=2, column = 1, padx =10)

# Create Menu
yell_menu = Menu(root_object)
root_object.config(menu = yell_menu)

root_object.mainloop()