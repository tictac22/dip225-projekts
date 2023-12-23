import os
import time
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

currentMonth = datetime.now().month
service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get('https://hop.visma.lv/#!/login')

driver.implicitly_wait(1)

input_email = driver.find_element(By.ID, "username")
input_password = driver.find_element(By.ID, "password_hidden")

email = os.environ.get("email")
input_email.send_keys(email)

password = os.environ.get("password")
input_password.send_keys(password)

input_email.submit()


salary_box =  WebDriverWait(driver,6).until(EC.presence_of_element_located((By.XPATH,"//h2[text()='Mana alga']")))
salary_box.click()
time.sleep(5)