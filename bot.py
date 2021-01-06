# TASKS ------>>>>
# if user is not signed in -->> create signin method
# if already signed in by system -->>
#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
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

        # XPATH = '//*[@id="password"]/div[1]/div/div[1]/input'
        pwd_input = driver.find_element(By.NAME, 'password')
        pwd_input.send_keys(pwd, Keys.ENTER)

    except Exception as e:
        print(f"Error :: {e}")


# email = pyautogui.prompt("Enter your Email to sign in ")
# pwd = pyautogui.prompt("Enter your Password to sign in ")
# sign_in(email, pwd)


def LETS_START_MEETING():
    try:

        def enter_code(code):
            try:
                code_input = driver.find_element(By.ID, 'i3')
                code_input.send_keys(code, Keys.ENTER)

            except Exception as e:
                print(f"Error :: {e}")

        code = pyautogui.prompt("Enter your Meeting Code to join ")
        # enter_code(code)

        def New_Meeting():
            try:

                new_meeting_btn = driver.find_element(
                    By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/button')
                new_meeting_btn.click()
                sleep(2)

                def create_new_meeting_later():
                    try:
                        link_btn = driver.find_element(
                            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div/ul/li[1]/span[2]/i')
                        link_btn.click()
                        sleep(2)

                        copy_link = driver.find_element(
                            By.XPATH, '//*[@id="yDmH0d"]/div[8]/div/div[2]/span/div/div[2]/div/div[2]/div/span/span/span/svg')
                        data = copy_link.click()  # CHECK THIS PROPERLY

                        whats_app = pyautogui.prompt(
                            "Wanna to send link to Whatsapp group (Y/y) ")

                        if whats_app == "Y" or whats_app == "y":
                            try:
                                driver.maximize_window()
                                driver.get("https://web.whatsapp.com/")
                                sleep(5)

                                name = pyautogui.prompt(
                                    "Enter group-name (must be same as whatsApp's contact) ")

                                search_box = driver.find_element(
                                    By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
                                search_box.send_keys(name, Keys.ENTER)

                                text_box = driver.find_element(
                                    By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                                text_box.send_keys(
                                    f"Here is your today's class link  \n{data}", Keys.ENTER)

                                sleep(2)

                                driver.close()

                            except Exception as e:
                                print(
                                    f"Unable to send link to whatsApp , Error  :: {e}")

                        else:
                            driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[2]/div[3]/div/span/span/svg/path[1]').click()



                    except Exception as e:
                        print(f"Error :: {e}")

                # create_new_meeting_later()

                def create_instatnt_meeting():
                    try:

                        add_btn = driver.find_element(
                            By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/div/ul/li[2]/span[2]/i')
                        add_btn.click()
                        sleep(5)

                        mute = pyautogui.prompt("Want to mute/unmute (Y/y)")
                        if mute == "Y" or mute == "y":
                            mute_btn = driver.find_element(
                                By.XPATH, '//*[@id="ow49"]/div/div')
                            mute_btn.click()
                        else:
                            pass

                        video = pyautogui.prompt(
                            "Wanna to turn Off/On the video (Y/y)")
                        if video == "Y" or video == "y":
                            video_btn = driver.find_element(
                                By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div')
                            video_btn.click()

                        else:
                            pass



                        def Join_Meeting():
                            try:
                                join_now_btn = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
                                join_now_btn.click()
                                data_link = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div[4]/div/span/span/span[1]/svg')                                    
                                data_link.click()
                                
                                joining_link = pyautogui.prompt("Want to share joining link (y/N) ")

                                if joining_link == "Y" or joining_link == "y":
    
                                    try:
                                        driver.maximize_window()
                                        driver.get("https://web.whatsapp.com/")
                                        sleep(5)

                                        name = pyautogui.prompt(
                                            "Enter group-name (must be same as whatsApp's contact) ")

                                        search_box = driver.find_element(
                                            By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')
                                        search_box.send_keys(name, Keys.ENTER)

                                        text_box = driver.find_element(
                                            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                                        text_box.send_keys(
                                            f"Here is your today's class link  \n{data_link}", Keys.ENTER)

                                        sleep(2)

                                        driver.close()

                                    except Exception as e:
                                        print(
                                            f"Unable to send link to whatsApp , Error  :: {e}")

                                else:
                                    driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[3]/div/div[2]/div[2]/div[3]/div/span/span/svg/path[1]').click()



                                chatt = pyautogui.prompt("Wanna to Chat with other forks (y/N)?")

                                if chatt == "Y" or chatt == "y":
                                    def student_msg():
                                        sleep(2)
                                        your_good_msg = pyautogui.prompt("Enter the message you wanna to share with other ")
                                        msg_icon = driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]/span/span/div/div/span/svg/path[2]')
                                        msg_icon.click()
                                        sleep(5)

                                        msg_input = driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea')
                                        sleep(2)
                                        msg_input.send_keys(your_good_msg, sleep(2) ,Keys.ENTER)
                                        sleep(2)
                                        close_cross = driver.find_element(By.XPATH, '//*[@id="ow3"]/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/button/i').click()


                                    student_msg()

                                    again_msg = pyautogui.prompt("Wanna to message again ?")
                                    if again_msg == "Y" or again_msg == "y":
                                        student_msg()
                                    else:
                                        pass

                                else:
                                    pass


                                present_your_window = pyautogui.prompt("Want to present your Screen (y/N)??")
                                if present_your_window == "Y" or present_your_window == "y":
                                    driver.find_element(By.XPATH, '//*[@id="ow137"]/div/span/span/div/div[1]/span/svg/path').click()
                                    sleep(2)

                                    def Entrie_Window():
                                        sleep(2)
                                        data_data = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/span[1]/div[3]/div').click()
                                        sleep(2)
                                        actions = ActionChains(driver)
                                        actions.double_click(data_data).perform()

                                    def A_window():
                                        yet to add here


                                    def A_tab():
                                        yet to add here
                                        

                                    asdf = int(pyautogui.prompt("1. Entire Window  2. A window  3. A tab"))

                                    if asdf == 1:
                                        Entrie_Window()

                                    elif 



                                    


                            except Exception as e:
                                print(f"Error :: {e}")


                        def Present_Screen():
                            try:
                                hfdgjshd

                            except Exception as e:
                                print(f"Error :: {e}")


                        
                        User_CHoice = int(pyautogui.prompt("1. Join Meeting   2. Present screen"))

                        if User_CHoice == 1:
                            Join_Meeting()

                        elif User_CHoice == 2:
                            Present_Screen()

                        else:
                            pass

                        



                    except Exception as e:
                        print(f"Error :: {e}")

                # create_instatnt_meeting()

                user_xy_choice = int(pyautogui.prompt("1. Create meeting later  2. Create instant meeting"))
                if user_xy_choice == 1:
                    create_new_meeting_later()

                elif user_xy_choice == 2:
                    create_instatnt_meeting()

                else:
                    pass

            except Exception as e:
                print(f"Error :: {e}")

        # New_Meeting()


        user_x_choice = int(pyautogui.prompt("1. Join via Meeting Code   2. Create new Meeting"))

        if __name__ == '__main__':

            if user_x_choice ==  1 :
                enter_code(code)
            
            elif user_x_choice == 2:
                New_Meeting()

            else:
                pass
                




            

    except Exception as e:
        print(f"Error :: {e}")


# LETS_START_MEETING()
