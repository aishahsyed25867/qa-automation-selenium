import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def saucedemo_login():
    driver = webdriver.Chrome() # 1. Open chrome browser

    try:
        driver.get("https://www.saucedemo.com/") # 2. Navigate to intended website

        username = driver.find_element(By.ID, "user-name") # 3. Navigate the Username Field using ID and enter the username: "standard_user"
        username.send_keys("standard_user")

        password = driver.find_element(By.ID, "password") # 4. Navigate the Password Field using ID and enter the password: "sauce_demo"
        password.send_keys("secret_sauce")

        login = driver.find_element(By.ID, "login-button") # 5. Navigate to the button using ID and click it
        login.click()

        time.sleep(3) # 6. Pause the execution so you can see visually what happened

        current_url = driver.current_url
        
        if "inventory.html" in current_url:
            print(" TEST SUCCESS ")
        else:
            print(" TEST FAIL ")


    finally:
        driver.quit() #8. Close browser

saucedemo_login()