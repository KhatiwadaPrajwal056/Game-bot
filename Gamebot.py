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
# print(os.getcwd())

wait_load = webdriver.ChromeOptions()
wait_load.add_experimental_option("detach",True)
web_service = Service(executable_path='/Users/khatiwadaprajwal22icloud.com/Desktop/Visual studio code/Game-bot/chromedriver')
driver = webdriver.Chrome(service=web_service,options=wait_load)

driver.get("https://plays.org/whack-a-mole/")
try:
    wait = WebDriverWait(driver, 10)
    # Example: Wait for a specific element to be present
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="game"]')))
    gui.scroll(-100)
    print("Element found")
except Exception as e:
    print("An error occurred:", e)


moles = ['assets/mole1_mac.png','assets/mole2_mac.png']

# def whack_mole():
#     for mole in moles:
#         try:
#             x,y = gui.locateCenterOnScreen(mole,confidence=0.8,grayscale=True)
#             gui.click(x/2,y/2)
#             print("Mole Whacked")
#         except gui.ImageNotFoundException:
#             print("No moles found")

# if __name__ == "__main__":
#     while True:
#         whack_mole()
