from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui as gui
import os
from pathlib import Path

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

# wait_load = webdriver.ChromeOptions()
# wait_load.add_experimental_option("detach",True)
# web_service = Service(executable_path='/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Game-bot/chromedriver')
# driver = webdriver.Chrome(service=web_service,options=wait_load)

# driver.get("https://plays.org/whack-a-mole/")
moles = ['assets/mole1_mac.png','assets/mole2_mac.png']
continue_button = 'assets/continue_button_mac.png'
start_button = 'assets/start_button_mac.png'
try:
    sleep(10)
    gui.scroll(-20)
    wait = WebDriverWait(driver, 10)
    # Example: Wait for a specific element to be present
    element = wait.until(EC.presence_of_element_located((By.ID, 'gameCanvas')))
    print("Element found")
except Exception as e:
    print("An error occurred:", e)

def continue_button_click(continue_button):
    try:
        x,y = gui.locateOnScreen(continue_button,confidence=0.8,grayscale=True)
        gui.click(x/2,y/2)
        print("Continue botton clicked")
    except gui.ImageNotFoundException:
        print("Botton not found")
def start_button_click(start_button):
    try:
        x,y = gui.locateOnScreen(start_button,confidence=0.8,grayscale=True)
        gui.click(x/2,y/2)
        print("Start botton clicked")
    except gui.ImageNotFoundException:
        print("Botton not found")

def whack_mole():
    # screen_width, screen_height = gui.size()
    # # Define the region where moles are likely to appear
    # search_region = (screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2)
    for mole in moles:
        try:
            x,y =  gui.locateCenterOnScreen(mole,confidence=0.8,grayscale=True)
            gui.click(x/2,y/2)
            print("Mole Whacked")
            return
        except gui.ImageNotFoundException:
            print("No moles found")
sleep(3)
while True:
    start_button_click(start_button)
    continue_button_click(continue_button)
    whack_mole()
    sleep(0.01)
