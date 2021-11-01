import time
import pytesseract as tess
import urllib.request
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

tess.pytesseract.tesseract_cmd = r'Tesseract Files/Tesseract-OCR/tesseract.exe'

service = Service(r'Web Drivers/firefoxdriver.exe')

driver = webdriver.Firefox(service=service)

url = r'https://loginpagebsg.herokuapp.com/'

driver.get(url)

urllib.request.urlretrieve(
    driver.find_element(By.ID, 'captchaImage').get_attribute('className'),
    "captcha.png")

img = Image.open("captcha.png")
text = ((tess.image_to_string(img)).strip()).replace(' ', '')

time.sleep(1)
driver.find_element(By.ID, 'InputFullName').send_keys('Name Surname')
driver.find_element(By.ID, 'InputPhoneNumber').send_keys('0 000 000 0000')
driver.find_element(By.ID, 'InputCity').send_keys('City')
driver.find_element(By.ID, 'InputCaptcha').send_keys(text)
time.sleep(2)
driver.find_element(By.ID, 'subBtn').click()
time.sleep(1.5)
driver.quit()
