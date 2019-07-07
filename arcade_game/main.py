import pygame as pg
pg.init()
import os, sys
sys.path.append(os.path.join(os.getcwd(), "modules"))
sys.path.append(os.path.join(os.getcwd(), "python_pictures"))
import randGameHub
from GUI_elements import*
import clr
import tictactoe
import flappy_bird
textCol = clr.white
screenCol = clr.black


pg.display.set_caption('Hub')

###################################################################################################################################################################################################

def mainLoop():
    global textCol, screenCol
    screenWd, screenHt = 1120, 630
    screen = pg.display.set_mode((screenWd, screenHt))
    clock = pg.time.Clock()
    FPS = 25
    background = black_background = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "background.png"))
    white_background = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "white_background.png"))
    randGameImage = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "randGame.png"))
    randGameImage_hovour =pg.image.load(os.path.join(os.getcwd(), "python_pictures", "randGame_hovour.png"))
    tictactoe_image = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "tictactoe.png"))
    tictactoe_hovour = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "tictactoe_hovour.png"))
    flappybird_img = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "bird_icon.png"))
    flappybird_hov = pg.image.load(os.path.join(os.getcwd(), "python_pictures", "bird_icon_hovour.png"))

    randCircle = Button(50, 50, 200, 200, 'Circle Game', randGameImage, randGameImage_hovour, textColour = clr.white)
    tictactoe_button = Button(350, 50, 200, 200, 'Tic-Tac-Toe', tictactoe_image, tictactoe_hovour)
    flappybird = Button(650, 50, 200, 200, 'Flappy Bird', flappybird_img, flappybird_hov)
    
    exit_button = Button(1050, 600, 50, 30, "Exit", textHeight = 30, textColour = clr.white, opaque = False)
    butt_mode = Button(1075, 15, 20, 20)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                Quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    Quit()
        if randCircle.get_click():
            temp = screenCol
            screenCol, textCol, speed, size = randGameHub.difficultyChoice(screenCol, textCol)
            if temp != screenCol:
                if screenCol == clr.black:
                    background = black_background
                    exit_button.textColour = textCol
                else:
                    background = white_background
                    exit_button.textColour = textCol
            if speed:
                screenCol, textCol = randGameHub.mainLoop(screenCol, textCol, speed, size)
                pg.display.set_caption('Hub')

        elif tictactoe_button.get_click():
            temp = screenCol
            screenCol, textCol = tictactoe.mainLoop(screenCol, textCol)
            if temp != screenCol:
                if screenCol == clr.black:
                    background = black_background
                    exit_button.textColour = textCol
                else:
                    background = white_background
                    exit_button.textColour = textCol
            pg.display.set_caption('Hub')

        elif flappybird.get_click():
            Bool = True
            while Bool:
                Bool = flappy_bird.mainLoop()
            pg.display.set_caption('Hub')

        elif exit_button.get_click():
            Quit()

        elif butt_mode.get_click():
            if screenCol == clr.black:
                background = white_background
                exit_button.textColour = textCol = clr.black
                screenCol = clr.white
            else:
                background = black_background
                exit_button.textColour = textCol = clr.white
                screenCol = clr.black
        
        screen.blit(background, (0, 0))

        if randCircle.onButton():
            text(screen, 30, 585, 30, "Circle Game: Click on the red circle to win the game!", textCol)
        elif tictactoe_button.onButton():
            text(screen, 30, 585, 30, "Tic-Tac-Toe: Classic game where you need to get 3 in a row. With 2-player and 1 player.", textCol)
        elif flappybird.onButton():
            text(screen, 30, 585, 30, "Flappy Bird: Classic game where you need to last as long as you can without crashing.", textCol)
             
        if screenCol == clr.black:
            sun(screen)
        else:
            moon(screen)
        
        randCircle.show(screen)
        tictactoe_button.show(screen)
        flappybird.show(screen)
        exit_button.show(screen)
        pg.display.update()

        clock.tick(FPS)
        
        
        

###################################################################################################################################################################################################

mainLoop()
