#**********FRONT-END FOR WEATHER GROYP APP*****************************
#
#**********MARVIS #140620**********************************************



#**********INCLUDES****************************************************
#PUBLIC LIBRARIES
import tkinter as tk
import tkinter.font as tkfont
from datetime import date
import pygame

#NON-PUBLIC LIBRARIES
from weather_functions import get_weather
#*********************************************************************



#**********GLOBAL VAR/OBJECTS*****************************************
#MAIN WINDOW
main_win = tk.Tk()
main_win.title("The Weather Groyp")
main_win.geometry("640x360")
main_win.resizable(False, False)
main_win.iconphoto(False, tk.PhotoImage(file="icon.gif"))

#MAIN CANVAS
main_win_canvas = tk.Canvas(main_win, width=640, height=360)
main_win_canvas.grid(rows=1, columns=1)

#MAIN WINDOW BACKGROUND IMAGE
main_win_image = tk.PhotoImage(file="background.gif")

#CREATE DICTIONARY FOR PARSED RESULTS TO PASS TO FUNCTIONS
weather_results = {}

#FONT OBJECTS
title_font_bold = tkfont.Font(weight="bold", size=20)
main_text_bold = tkfont.Font(weight="bold", size=12)
main_text_normal = tkfont.Font(size=12)
small_text_bold = tkfont.Font(weight="bold", size=10)
small_text_normal = tkfont.Font(size=10)
#*********************************************************************



#**********FUNCTION TO DRAW MAIN CANVAS**********************
def draw_canvas(canvas, weather_data):
    #CLEAR EVERYTHING FROM THE CANVAS
    main_win_canvas.delete("all")
    
    #DRAW BACKGROUND IMAGE TO CANVAS
    main_win_canvas.create_image(0, 0, image=main_win_image, anchor=tk.NW)
    
    #DRAW TITLE TEXT
    draw_text(main_win_canvas, 140, 25, 2, title_font_bold, "#C8B502", "Your Local Weather")

    #DRAW DATE TEXT
    my_date = date.today()
    draw_text(main_win_canvas, 510, 20, 1, small_text_bold, "white", my_date.strftime("%A"))
    draw_text(main_win_canvas, 510, 40, 1, small_text_bold, "white",
                                my_date.strftime("%b" + " " + "%d" + " " + "%Y"))

    #DRAW LOCATION AND DATA TIME UPDATE
    draw_text(main_win_canvas, 10, 305, 1, title_font_bold, "#F0F0F0", weather_data['location'])
    draw_text(main_win_canvas, 10, 340, 1, small_text_normal, "#F0F0F0",
        "WEATHER LOCATION DATA UPDATED: " + weather_data['time'])

    #DRAW CONDITION DATA (THE BIG ONE)
    draw_text(main_win_canvas, 220, 80, 1, main_text_bold, "#F0F0F0",
        "It is currently " + weather_data['weather'] + " and " +
        weather_data['temp'] + "\u2109" + ".")
    draw_text(main_win_canvas, 220, 100, 1, main_text_bold, "#F0F0F0",
        weather_data['humid'] + " humidity with a " + weather_data['precip'] +
        " chance of precip")
    draw_text(main_win_canvas, 220, 120, 1, main_text_bold, "#F0F0F0",
        "and wind speeds up to " + weather_data['wind'] + ".")

    return
#*********************************************************************



#**********FUNCTION TO DRAW TEXT ON CANVAS***********************
def draw_text(canvas, x, y, shift, font, color, text):
    #DRAW BACKGROUND/SHADOW TEXT FIRST
    canvas.create_text(x+shift, y+shift, anchor=tk.NW, fill="black",
    font=font, text=text)
    #DRAW MAIN TEXT
    canvas.create_text(x, y, anchor=tk.NW, fill=color,
    font=font, text=text)
    return
#*********************************************************************



#**********GET WEATHER DATA ******************************************
get_weather(weather_results)
#*********************************************************************



#**********DRAW WEATHER DATA/IMAGES TO CANVAS*************************
draw_canvas(main_win_canvas, weather_results)
#*********************************************************************



#**********PLAY BACKGROUND MUSIC*************************************
pygame.init() 
main_music = pygame.mixer.music.load("g_song.wav")
pygame.mixer.music.play(loops=-1)
#********************************************************************



#**********MAIN PROGRAM LOOP*****************************************
main_win.mainloop()
#********************************************************************



#**********RELEASED TO GITHUB BY MARVIS 160620**********************
#https://github.com/YaBoiMarvis/the-weather-groyp
#********************************************************************
