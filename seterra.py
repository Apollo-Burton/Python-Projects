import pyautogui as pag
from PIL import ImageGrab
import pytesseract
import time

# defining locations of states on screen
states = {"Click on Alabama\n": (950, 580), 
"Click on Alaska\n": (430, 700), 
"Click on Arizona i\n": (500, 530), 
"Click on Arkansas\n": (850, 540), 
"Click on California\n": (370, 420), 
"Click on Colorado\n": (630, 440), 
"Click on Connectict\n": (1150, 350), 
"Click on Delaware\n": (1125, 415), 
"Click on Florida >\n": (1050, 640), 
"Click on Georgia &\n": (1000, 580), 
"": (630, 770), 
"Click on idaho El\n": (500, 300), 
"Click on Illinois | *\n": (900, 400), 
"Click on Indiana &\n": (950, 420), 
"Click onlowa Pell\n": (820, 380), 
"Click on Kansas &\n": (750, 450), 
"Click on Kentucky\n": (980, 470), 
"Click on Louisiana\n": (840, 620), 
"Click on Maine El\n": (1180, 250), 
"Click on Maryland\n": (1100, 420), 
"Click on Massachus\n": (1160, 330), 
"Click on Michigan\n": (950, 350), 
"Click on Minnesota\n": (810, 300), 
"Click on Mississippi\n": (900, 600), 
"Click on Missouri :\n": (850, 450), 
"Click on Montana\n": (600, 250), 
"Click on Nebraska\n": (720, 400), 
"Click on Nevada &\n": (450, 400), 
"Click on New Hame\n": (1160, 300), 
"Click on New Jerse\n": (1135, 400), 
"Click on New Mexic\n": (600, 540), 
"Click on New York\n": (1110, 320), 
"Click on North Cara\n": (1060, 500), 
"Click on North Dak\n": (720, 260), 
"Click on Ohio\n": (1000, 400), 
"Click on Oklahoma\n": (750, 520), 
"Click on Oregon &\n": (400, 300), 
"Click on Pennsylva\n": (1085, 380), 
"Click on Rhode Isla\n": (1175, 345), 
"Click on South Carc\n": (1050, 540), 
"Click on South Dak\n": (720, 330), 
"Click on Tennessee\n": (950, 510), 
"Click on Texas [am\n": (730, 600), 
"Click on Utah El\n": (530, 420), 
"Click on Vermont |\n": (1140, 300), 
"Click on Virginia &\n": (1080, 450), 
"Click on Washingto\n": (430, 220), 
"Click on West Virgil\n": (1040, 440), 
"Click on Wisconsin\n": (875, 320), 
"Click on Wyoming\n": (600, 350)
}

# Defining the location of the box
box = (850, 745, 990, 770)
time.sleep(2)

def start():
    pag.click(815, 540)
    pag.click(1240, 930)
    # Reading the text in the box
    for i in range(len(states)):
        pag.moveTo(835, 725)
        image = ImageGrab.grab(box)
        text = pytesseract.image_to_string(image, lang = 'eng')
        # Clicking the state
        if text in states:
            pag.click(states[text])

start()
