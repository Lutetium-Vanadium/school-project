import pygame as pg
pg.init
import math
import clr


class Button():
    def __init__(self, x, y, wd, ht, text = '', img = None, hovourImg = None, textHeight = None, textColour = clr.black,
                 colour = pg.Color(32, 32, 32, 1), hovourColour = pg.Color(75, 75, 75, 1), opaque = True, activated = True):
        if not textHeight:
            textHeight = ht//5
        self.textHeight = textHeight
        self.img = img
        self.hovourImg = hovourImg
        self.xy = (x, y)
        self.rect = pg.Rect(x, y, wd, ht)
        self.text = text
        self.textColour = textColour
        self.colour = colour
        self.hovourColour = hovourColour
        self.opaque = opaque
        self.activated = activated
        self.flag = False
    def onButton(self):
        return self.rect.collidepoint(pg.mouse.get_pos())
    def show(self, surface):
        if self.onButton():
            if self.img:
                image = self.hovourImg
            else:
                colour = self.hovourColour
        else:
            if self.img:
                image = self.img
            else:
                colour = self.colour
        if self.img:
            surface.blit(image, self.xy)
        else:
            if self.opaque:
                pg.draw.rect(surface, colour, self.rect)
        textSurf = pg.font.SysFont(pg.font.get_default_font(), self.textHeight).render(self.text, True, self.textColour)
        textRect = textSurf.get_rect()
        textRect.center = self.rect.center
        surface.blit(textSurf, textRect)
    def get_click(self):
        temp = (self.activated and pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos()))
        if self.flag == False and temp:
            self.flag = True
            return temp
        if self.flag and temp == False:
            self.flag = False

'''---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def Quit():
    pg.quit()
    quit()

def text(screen, x, y, size, text, colour = clr.white):
    textSurf = pg.font.SysFont(pg.font.get_default_font(), size).render(text, True, colour)
    screen.blit(textSurf, (x, y))

def sun(screen):
    surf = pg.Surface((200, 200))
    surf.fill(clr.black)
    surf.set_colorkey(clr.black)
    pg.draw.circle(surf, clr.white, (100, 100), 70)
    for i in range(12):
        start_x = 50 * (math.cos(i*math.pi/6))
        end_x = 100 * (math.cos(i*math.pi/6))
        start_y = 50 * (math.sin(i*math.pi/6))
        end_y = 100 * (math.sin(i*math.pi/6))
        pg.draw.line(surf, clr.white, ((100 + start_x),(100 + start_y)), ((100 + end_x),(100 + end_y)), 30)
    surf = pg.transform.smoothscale(surf, (20, 20))
    screen.blit(surf, (1075, 15))

def moon(screen):
    surf = pg.Surface((200, 200))
    surf.fill(screen.get_at((1085, 25)))
    pg.draw.circle(surf, clr.black, (100, 100), 100)
    pg.draw.circle(surf, screen.get_at((1085, 25)), (180, 100), 100)
    surf = pg.transform.smoothscale(surf, (20, 20))
    c = surf.get_at((0,0))
    surf.set_colorkey(c)
    screen.blit(surf, (1075, 15))
