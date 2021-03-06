from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select

end=False

driver=webdriver.Chrome(executable_path="./../chromedriver_win32/chromedriver.exe")
loginurl="https://ost.benesse.ne.jp/ol/member/login/login_ost"
driver.get(loginurl)
customerId=driver.find_element_by_id("customerId")
customerId.send_keys('414895050469')
password=driver.find_element_by_id("password")
with open(r"./../password.txt") as f:
    mypassword=f.read()
print(mypassword)
password.send_keys(mypassword)
loginbutton=driver.find_element_by_class_name("loginForm--bottom")
loginbutton.click()
while True:
    driver.get('https://ost.benesse.ne.jp/ol/member/TakeLesson/takeLesson')
    try:
        cancel=driver.find_element_by_css_selector(".button.crucial")
    except NoSuchElementException:
        end=1
    if end:
        break
    javas=cancel.get_attribute('href')
    if "button crucial"!=javas:
        print(javas)
        driver.execute_script(javas)
        ok=driver.find_element_by_id("session-id-check-submit-btn")
        ok.click()
    