"""Modulis env variable iegūšanai"""
import os
import time
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

def get_salary():
    """funkcija, lai saņemtu algu par pēdējo mēnesi"""

    driver.get('https://hop.visma.lv/#!/login')

    time.sleep(1)

    input_email = driver.find_element(By.ID, "username")
    input_password = driver.find_element(By.ID, "password_hidden")

    email = os.environ.get("email")
    input_email.send_keys(email)

    password = os.environ.get("password")
    input_password.send_keys(password)

    input_email.submit()


    salary_box =  WebDriverWait(driver,6).until(EC.presence_of_element_located((
        By.XPATH,
        "//h2[text()='Mana alga']"
    )))
    salary_box.click()

    salary = WebDriverWait(driver,6).until(EC.presence_of_element_located((
        By.XPATH,
        '//span[text()="Izmaksa:"]/following-sibling::span'
    )))
    salary = float(salary.text[4:].replace(",","."))

    return salary
