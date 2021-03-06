from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
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
    driver.get('https://ost.benesse.ne.jp/ol/member/Reservation/selectTicket')
    try:
        buttonprimary=driver.find_element_by_css_selector(".button.primary")
    except NoSuchElementException:
        print("there is no tickets")
        end=True
    if end:
        break
    for i in range(2):
        buttonprimary=driver.find_element_by_css_selector(".button.primary")
        buttonprimary.click()
    driver.execute_script("goFreePlan();return false;")

    selectTime=driver.find_element_by_id("selectedItem")
    selectTimeValue = Select(selectTime)
    selectTimeValue.select_by_value('19:00～23:00')
    flag=False
    while True:  
        for elem in driver.find_elements_by_id('btnReserable'):
            if elem.get_attribute("value")[11:]=="19:30:00":
                elem.click()
                ok=driver.find_element_by_id("btnOk")
                ok.click()
                flag=True
                break
        if flag:
            break
        nxt=driver.find_element_by_name("btnNext")
        nxt.click()