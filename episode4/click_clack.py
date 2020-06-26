import pyautogui as pg
import keyboard as key
import time

pg.FAILSAFE = True # при резком движении курсора в верхний левый укгол
					# программа выключается

start_key = input('Клавиша запуска: ')
stop_key = input('Клавиша остановки: ')

while True:
	if key.is_pressed(start_key):
		pg.hotkey('ctrl', 'a')
		time.sleep(0.5)
		
		pg.typewrite(['backspace']) # убрать все символы
		time.sleep(0.5)

		pg.click() # нажать на ключик
		time.sleep(2.2)

		pg.click(866, 339)# нажать на дополнительное
		time.sleep(1)
		
		pg.click(890, 625)# нажать на выпадающий список
		time.sleep(1)
		
		pg.click(888, 659)# выбрать из выпадающего списка
		time.sleep(0.5)
		
		pg.click(1014, 650)# нажать на поле макс. лимит скорости
		time.sleep(1)
		
		pg.hotkey('ctrl', 'a')
		time.sleep(0.5)
		
		pg.typewrite(['backspace']) # убрать все символы
		time.sleep(0.5)
		
		pg.typewrite("120")# вписать 120 в поле
		time.sleep(0.5)
		
		pg.click(1012, 674)# hажать на "время"
		time.sleep(0.5)
		
		pg.hotkey('ctrl', 'a')
		time.sleep(0.5)
		
		pg.typewrite(['backspace']) # убрать все символы
		time.sleep(0.5)
		
		pg.typewrite("60")# вписать 60 в поле
		time.sleep(0.5)
		
		pg.click (1368, 829, clicks=3, interval=0.25)# трипл клик
		time.sleep(0.5)
		
		pg.click(878, 780) #выбор первого лимита
		time.sleep(0.6)
		
		pg.click(958, 810) #выбор поля первого лимита
		time.sleep(0.6)
		
		pg.hotkey('ctrl', 'a')
		time.sleep(0.5)
		
		pg.typewrite(['backspace']) # убрать все символы
		time.sleep(0.5)
		
		pg.typewrite("120")# вписать 120 в поле
		time.sleep(0.6)
		
		pg.click(824, 974)#выбор цвета (зеленый)
		time.sleep(1) 
		
		pg.click(934, 1012)# ОК
		time.sleep(0.6)
		
		pg.click(1080, 780)
		time.sleep(0.6)
		
		pg.click(1206, 810)
		time.sleep(0.6)
		
		pg.hotkey('ctrl', 'a')
		time.sleep(0.5)
		
		pg.typewrite(['backspace']) # убрать все символы
		time.sleep(0.5)
		
		pg.typewrite("150")# вписать 150 в поле
		time.sleep(0.6)
		
		pg.click(1224, 980)# выбор цвета (желтый)
		time.sleep(1)
		
		pg.click(1196, 1015)# ОК
		time.sleep(0.6)
		
		pg.click(590, 781)# по скорости
		time.sleep(1)
		
		pg.click(1340, 861)# ОК
		time.sleep(1)

	if key.is_pressed(stop_key):
		break


