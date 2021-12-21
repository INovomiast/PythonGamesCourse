#Information
__license__ = "GNU"
__author__ = "INovomiast"


#Various Modules
import os

#Games
from games import pong
from games import snake
from games import c_four
from games import tetris
from games import ompgame

def exec():
    os.system('cls')
    print("Welcome to PythonGames Course")
    print("This is a list of various games developed on Python with different" + '\n' + "technics, so be sure to have fun!.")
    print(__license__)
    print('\n')
    print("GAMES")
    print("=====")
    print('\n')
    print("1. Pong")
    print("2. Snake")
    print("3. Connect Four")
    print("4. Tetris")
    print("5. Online Multiplayer Game")
    print('\n')
    option = int(input("Select a Game to Play:"))
    
    
    
    #Menu Logic
    if(option == 1):
        os.system('cls')
        pong.start()
    elif(option == 2):
        os.system('cls')
        snake.start()
    elif(option == 3):
        os.system('cls')
        c_four.start()
    elif(option == 4):
        os.system('cls')
        tetris.start()
    elif(option == 5):
        os.system('cls')
        ompgame.start()
    

exec()