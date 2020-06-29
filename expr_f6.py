import numpy as np
import pyautogui as pg
import keyboard as key
import pyscreenshot as ImageGrab
import cv2
import os
import pytesseract
import time

filename1 = 'Image1.png'
filename2 = 'Image2.png'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

while (True):
    if key.is_pressed('F12'):
        pg.click()
        pg.hotkey('f2')
        time.sleep(1)
        pg.click(136, 239)

        screen1 = np.array(ImageGrab.grab(bbox=(1178, 337, 1310, 759)))			
        cv2.imwrite(filename1, screen1)
        img1 = cv2.imread('Image1.png')
        first_address = pytesseract.image_to_string(img1)
        print(first_address)
        
        screen2 = np.array(ImageGrab.grab(bbox=(1440, 359, 1596, 719)))			
        cv2.imwrite(filename2, screen2)
        img2 = cv2.imread('Image2.png') 
        second_address = pytesseract.image_to_string(img2) 
        print(second_address)

        if first_address == second_address:
            pg.click(610, 266)
            time.sleep(1)           
            pg.hotkey('insert')
            time.sleep(1)           
            pg.click(160, 356)
            time.sleep(1)           
            pg.hotkey('f3', press=4, interval=1.25)
            break

    else:
        if key.is_pressed('F11'):
            break
       

