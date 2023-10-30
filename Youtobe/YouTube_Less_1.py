from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.get("https://www.qa-practice.com/elements/button/simple")
# click_button = browser.find_element(By.ID, 'submit-id-submit')# Ищет по ID элемента
sleep(3) # делает отсрочку на заданное время
# click_button.click()# Клацает на єлемент

# click_button2 = browser.find_element(By.CLASS_NAME, 'btn') # Ищет элемент по названию класса
# click_button2.click() # Клацает на єлемент


browser.find_element(By.LINK_TEXT, 'Contact').click() #Можно не сохранять действия в переменную, а сразу писать
         #без переменной как в этом примере^

sleep(5) # делает отсрочку на заданное время