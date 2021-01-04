# TASKS ------>>>>
  # if user is not signed in -->> create signin method
  # if already signed in by system -->>
     #   




from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from time import sleep
import pyautogui



chromedriver_path = 'C:/Users/Nitesh Prajapati/Downloads/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.maximize_window()

driver.get("https://meet.google.com/")
sleep(2)


def sign_in(email, pwd):
    try:
        email_input = driver.find_element(By.ID, 'identifierId')
        email.send_keys(email, Keys.ENTER)

        pwd_input = driver.find_element(By.NAME, 'password')     #  XPATH = '//*[@id="password"]/div[1]/div/div[1]/input'
        pwd_input.send_keys(pwd, Keys.ENTER)


    except Exception as e:
        print(f"Error :: {e}")


email = pyautogui.prompt("Enter your Email to sign in ")
pwd = pyautogui.prompt("Enter your Password to sign in ")
# sign_in(email, pwd)



def LETS_START_MEETING():
    try:

        def enter_code(code):
            try:
                code_input = driver.find_element(By.ID, 'i3')
                code_input.send_keys(code, Keys.ENTER)

            except Exception as e:
                print(f"Error :: {e}")

    except Exception as e:
        print(f"Error :: {e}")