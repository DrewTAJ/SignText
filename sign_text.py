#!/usr/bin/python 
import Image
import ImageDraw
import time
from rgbmatrix import Adafruit_RGBmatrix
 
matrix = Adafruit_RGBmatrix(32, 3)
matrix.SetWriteCycles(5)
image = Image.new("1", (64 * 10, 32))
draw  = ImageDraw.Draw(image) 

def drawByCoords(coords, colour):
        for index, coord in enumerate(coords): 
                if index == (len(coords) - 1):
                        draw.line((coords[0], coords[index]), fill=colour)
                else:
                        draw.line((coords[index], coords[index + 1]), fill=colour)

def drawA(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + (height / 2)),
                (maxX - 4, minY + (height / 2)),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY)
        ]
        draw.rectangle((minX + 4, minY + 4, maxX - 4, minY + 4 + 7), fill=0, outline=colour)
        drawByCoords(coords, colour)

def drawB(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX - 4, maxY),
                (maxX, maxY - 4),
                (maxX, minY + (height / 2) + 4),
                (maxX - 4, minY + (height / 2)),
                (maxX, minY + (height / 2) - 4),
                (maxX, minY + 4),
                (maxX - 4, minY)
        ]
        drawByCoords(coords, colour)
        coords = [
                (minX + 4, minY + 4),
                (minX + 4, minY + (height / 2) - 2),
                (maxX - 8, minY + (height / 2) - 2),
                (maxX - 4, minY + (height / 2) - 4),
                (maxX - 4, minY + 8),
                (maxX - 8, minY + 4)
        ]
        drawByCoords(coords, colour)
        coords = [
                (minX + 4, minY + (height / 2) + 2),
                (minX + 4, maxY - 4),
                (maxX - 8, maxY - 4),
                (maxX - 4, maxY - 8),
                (maxX - 4, minY + (height / 2) + 6),
                (maxX - 8, minY + (height / 2) + 2)
        ]
        drawByCoords(coords, colour)
                        
def drawC(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawD(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX - 4, maxY),
                (maxX, maxY - 4),
                (maxX, minY + 4),
                (maxX - 4, minY)
        ]
        drawByCoords(coords, colour)
        coords = [
                (minX + 4, minY + 4),
                (minX + 4, maxY - 4),
                (maxX - 8, maxY - 4),
                (maxX - 4, maxY - 8),
                (maxX - 4, minY + 8),
                (maxX - 8, minY + 4),
        ]
        drawByCoords(coords, colour)

def drawE(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY + (height / 2) + 2),
                (maxX, minY + (height / 2) + 2),
                (maxX, minY + (height / 2) - 2),
                (minX + 4, minY + (height / 2) - 2),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)
        

def drawF(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, (minY + (height / 2)) + 4),
                (maxX, (minY + (height / 2)) + 4),
                (maxX, minY + (height / 2)),
                (minX + 4, (height / 2)),
                (minX + 4,  minY + (height / 4)),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawG(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - (height / 2)),
                (minX + 8, maxY - (height / 2)),
                (minX + 8, maxY - (height / 2) + 4),
                (maxX - 4, maxY - (height / 2) + 4),

                (maxX -4, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawH(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, (minY + (height / 2)) + 1),
                (maxX - 4, (minY + (height / 2)) + 1),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, (minY + (height / 2)) - 2),
                (minX + 4, (minY + (height / 2)) - 2),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawI(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),

                (minX + (width / 2) - 2, minY + 4),
                (minX + (width / 2) - 2, maxY - 4),

                (minX, maxY - 4),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),

                (minX + (width / 2) + 2, maxY - 4),
                (minX + (width / 2) + 2, minY + 4),

                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawJ(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),
                (minX + (width / 2) - 1, minY + 4),
                (minX + (width / 2) - 1, maxY - 4),
                (minX + 3, maxY - 4),
                (minX + 3, minY + (height / 2) - 2),
                (minX, minY + (height / 2) - 2),
                (minX, maxY),
                (minX + (width / 2) + 3, maxY),
                (minX + (width / 2) + 3, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawK(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, maxY - (height / 2) + 2),
                (maxX - 5, maxY - (height / 2) + 2),
                (maxX - 4, maxY - (height / 2) + 4),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY + (height / 2) + 4),
                (maxX - 2, minY + (height / 2) + 1),
                (maxX, minY + (height / 2) - 3),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, minY + (height / 2) - 4),
                (maxX - 5, minY + (height / 2) - 1),
                (minX + 4, minY + (height / 2) - 1),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawL(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawM(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + 6),
                (minX + (width / 2) - 1, minY + 8),
                (minX + (width / 2) - 1, maxY),
                (minX + (width / 2) + 2, maxY),
                (minX + (width / 2) + 2, minY + 8),
                (maxX - 4, minY + 6),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (minX + (width / 2), minX + 4),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawN(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + 12),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, maxY - 12),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawO(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        draw.rectangle((minX, minY, maxX, maxY), fill=0, outline=colour)
        draw.rectangle((minX + 4, minY + 4, maxX - 4, maxY - 4), fill=0, outline=colour)

def drawP(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + (4 * 3)),
                (maxX, minY + (4 * 3)),
                (maxX, minY)
        ]
        draw.rectangle((minX + 4, minY + 4, maxX - 4, minY + 8), fill=0, outline=colour)
        drawByCoords(coords, colour)

def drawQ(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY - 5),
                (maxX - 6, maxY - 5),
                (maxX - 4, maxY),
                (maxX, maxY),
                (maxX - 2, maxY - 5),
                (maxX - 2, minY)
        ]
        drawByCoords(coords, colour)
        coords = [
                (minX + 3, minY + 3),
                (minX + 3, maxY - 7),
                (maxX - 5, maxY - 7),
                (maxX - 5, minY + 3)
        ]
        drawByCoords(coords, colour)

def drawR(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + 4, minY + (height / 2)),
                (maxX - 8, minY + (height / 2)),
                (maxX - 8, maxY),
                (maxX - 4, maxY),
                (maxX - 4, minY + (height / 2)),
                (maxX, minY + (height / 2) - 4),
                (maxX, minY + 4),
                (maxX - 4, minY)
        ]
        drawByCoords(coords, colour)
        coords = [
                (minX + 4, minY + 3),
                (minX + 4, (minY + (height / 2)) - 3),
                (maxX - 7, (minY + (height / 2)) - 3),
                (maxX - 4, (minY + (height / 2)) - 6),
                (maxX - 4, minY + 6),
                (maxX - 7, minY + 3)
        ]
        drawByCoords(coords, colour)

def drawS(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + (height / 2) + 2),
                (maxX - 4, minY + (height / 2) + 2),
                (maxX - 4, maxY - 4),
                (minX, maxY - 4),
                (minX, maxY),
                (maxX, maxY),
                (maxX, minY + (height / 2) - 2),
                (minX + 4, minY + (height / 2) - 2),
                (minX + 4, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawT(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),
                (minX + (width / 2) - 2, minY + 4),
                (minX + (width / 2) - 2, maxY),
                (minX + (width / 2) + 2, maxY),
                (minX + (width / 2) + 2, minY + 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

def drawU(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (maxX - 4, maxY - 4),
                (minX + 4, maxY - 4),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawV(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                ((minX + (width / 2)) - 2, maxY),
                ((minX + (width / 2)) + 2, maxY),
                (maxX, minY),
                (maxX - 4, minY),
                (minX + (width / 2), maxY - 4),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawW(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, maxY),
                (maxX, maxY),
                (maxX, minY),
                (maxX - 3, minY),
                (maxX - 3, maxY - 4),
                (minX + (width / 2) + 2, maxY - 4),
                (minX + (width / 2) + 2, minY + 4),
                (minX + (width / 2) - 1, minY + 4),
                (minX + (width / 2) - 1, maxY - 4),
                (minX + 3, maxY - 4),
                (minX + 3, minY)
        ]
        drawByCoords(coords, colour)

def drawX(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                ((minX + (width / 2)) - 2, (height / 2)),
                (minX, maxY),
                (minX + 4, maxY),
                (minX + (width / 2), (height / 2) + 2),
                (maxX - 4, maxY),
                (maxX, maxY),
                (minX + (width / 2) + 2, (height / 2)),
                (maxX, minY),
                (maxX - 4, minY),
                (minX + (width / 2), (height / 2) - 2),
                (minX + 4, minY)
        ]
        drawByCoords(coords, colour)

def drawY(minX, minY, maxY, width, height, colour): 
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + (height / 2)),
                (minX + (width / 3), minY + (height / 2)),
                (minX + (width / 3), maxY),
                (minX + ((width / 3) * 2), maxY),
                (minX + ((width / 3) * 2), minY + (height / 2)),
                (maxX, minY + (height / 2)),
                (maxX, minY),
                (minX + ((width / 3) * 2), minY),
                (minX + ((width / 3) * 2), minY + (height / 3)),
                (minX + (width / 3), minY + (height / 3)),
                (minX + (width / 3), minY)
        ]
        drawByCoords(coords, colour)

def drawZ(minX, minY, maxY, width, height, colour):
        maxX = minX + width
        coords = [
                (minX, minY),
                (minX, minY + 4),
                (maxX - 4, minY + 4),
                (minX, maxY - 4),
                (minX, maxY),
                (maxX, maxY),
                (maxX, maxY - 4),
                (minX + 4, maxY - 4),
                (maxX, minY + 4),
                (maxX, minY)
        ]
        drawByCoords(coords, colour)

letterMethods = {
        "A":drawA,
        "B":drawB,
        "C":drawC,
        "D":drawD,
        "E":drawE,
        "F":drawF,
        "G":drawG,
        "H":drawH,
        "I":drawI,
        "J":drawJ,
        "K":drawK,
        "L":drawL,
        "M":drawM,
        "N":drawN,
        "O":drawO,
        "P":drawP,
        "Q":drawQ,
        "R":drawR,
        "S":drawS,
        "T":drawT,
        "U":drawU,
        "V":drawV,
        "W":drawW,
        "X":drawX,
        "Y":drawY,
        "Z":drawZ
}

def drawWord(word, index, word_starting_x):
        width = 15
        height = 31
        spacing = 2
        word_spacing = 10
        word_length = 0
        minX = word_starting_x
        minY = 0
        maxX = width
        maxY = height
        for index, letter in enumerate(word):
                if letter != "":
                        if letter in letterMethods:
                                letterMethods[letter](minX, minY, maxY, width, height, 1)
                                minX += width + spacing
                                word_length += width
                                if index < (len(word) - 1):
                                        word_length += 2

        return word_length

def drawText(text):
        text = text.upper()
        words = text.split(" ")
        spacing = 0
        word_spacing = 10
        new_word_start = 0

        for index, word in enumerate(words):
                if word != "":
                        new_word_start += drawWord(word, index, new_word_start)
                if index < (len(words) - 1):
                        new_word_start += word_spacing

        for n in range(64 * 2, -new_word_start, -1):
                matrix.Clear()
                matrix.SetImage(image.im.id, n, 0)

                if n > -new_word_start:
                        time.sleep(0.05)

        matrix.Clear()

def init():
        text = raw_input("Input the text you would like to see     ")
        drawText(text)

init()