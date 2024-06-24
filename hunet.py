import time
from tkinter import *
from tkinter import ttk
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.alert import Alert # 얼럿창(=알림창) 처리 라이브러리

window = Tk()
window.title("TROSSJO")
user_id, password = StringVar(), StringVar()

def start():
    try:
        run()
    except:
        start()

def run():

    try:
        os.system('taskkill /f /im chromedriver.exe')
    except:
        pass

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get('http://yeram.hunet.co.kr/Login/LoginGate')
    driver.implicitly_wait(15)
    driver.find_element(By.NAME, 'ID').send_keys(user_id.get())
    driver.find_element(By.NAME, 'PW').send_keys(password.get())
    driver.find_element(By.CLASS_NAME, 'btn-login').click()
    driver.implicitly_wait(15)
    driver.get('https://yeram.hunet.co.kr/classroom/online')
    driver.implicitly_wait(15)
    driver.find_element(By.CLASS_NAME, 'button-set').click()
    driver.implicitly_wait(15)


    while True:
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@id="content"]/div[8]/a').click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[2])
        driver.implicitly_wait(15)
        try:
            alert = driver.switch_to.alert.accept()
            alert.accept()
        except:
            pass
        time.sleep(1300)
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(15)
        driver.find_element(By.CLASS_NAME, 'button-set').click()

def set_chrome_driver():
    #chrome_options = webdriver.ChromeOptions()
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver


ttk.Label(window, text = "yeram- 제외한 아이디 : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "비밀번호 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Label(window, text = "  계정 비밀번호 설정 후 이용 \n             에러시 재실행").grid(row = 2, column = 0, padx = 10, pady = 10)
ttk.Button(window, text = "실행", command = run).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()
