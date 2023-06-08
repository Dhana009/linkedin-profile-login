from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key, Controller
import codecs
from selenium.webdriver.common.action_chains import ActionChains


# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

# Set the path to the ChromeDriver executable
driver_path = "F://all_pycharm_files//chromedriver.exe"


class linked_in:

    def __init__(self):
        self.encoded_text = None
        self.text = None
        self.image_file = None
        self.path = None

    def call_allvariables(self,text,filename):
        self.login()
        self.post_box()
        self.typing_text(text)
        self.image_upload(filename)
        self.post_buttons()

    def login(self):
        # Create a new instance of the WebDriver with the configured options
        self.driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
        # driver.maximize_window()
        # Open the LinkedIn website
        try:
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(2)

            email_field = self.driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')
            password_field = self.driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')

            '''email_field = driver.find_element(By.XPATH, '//*[@id="session_key"]')
            password_field = driver.find_element(By.XPATH, '//*[@id="session_password"]')'''
            # Enter your LinkedIn login credentials
            email_field.send_keys("dhanamani817@gmail.com")
            time.sleep(1)
            password_field.send_keys("Qwerty123")
            time.sleep(1)
            # Submit the login form
            password_field.send_keys(Keys.RETURN)
            # Wait for the LinkedIn home page to load
            # WebDriverWait(driver, 10).until(EC.title_contains("LinkedIn"))
            time.sleep(3)
        except:
            print('login error check')

    def post_box(self):

        try:
            # Locate and click on the new post input box
            self.driver.find_element(By.CLASS_NAME,
                                     "artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger").click()
        except:
            try:
                print('postbox1 failed checking next one ')
                time.sleep(1)
                self.driver.find_element(By.XPATH,
                                         "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div[1]/div[2]/div[2]/button").click()
                time.sleep(1)
            except:
                print('postbox2 failed checking next one ')
                try:
                    self.driver.find_element(By.XPATH,
                                             "/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/div[1]/div[2]/div[2]/button").click()
                    time.sleep(1)
                except:
                    print('postbox3 failed checking next one ')
                    self.driver.refresh()
                    time.sleep(5)
                    self.driver.find_element(By.CLASS_NAME,
                                             "artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger").click()
                    time.sleep(1)


    def typing_text(self,text):
        self.text = text
        try:
            post_input = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div/div/div[1]")
            self.driver.execute_script("arguments[0].innerHTML = arguments[1];", post_input, self.text)
            time.sleep(6)

        except:
            print('post_input_key1 failed checking next')
            try:
                post_input = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]")
                self.driver.execute_script("arguments[0].innerHTML = arguments[1];", post_input, self.text)
                time.sleep(6)
            except:
                try:
                    post_input = self.driver.find_element(By.CLASS_NAME, "ql-editor ql-blank")
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", post_input, self.text)
                    time.sleep(6)

                except :
                    print('post_input_key3 failed checking next')
                    post_input = self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]")
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", post_input, self.text)
                    time.sleep(6)

    def image_upload(self, filename):
        self.image_file = filename
        try:
            time.sleep(1)
            # Locate and click on the file upload button
            self.driver.find_element(By.XPATH,
                                     '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/span[1]/div[1]/button').click()
            time.sleep(2)
            keyboard = Controller()
            time.sleep(1)
            keyboard.type(self.image_file)
            time.sleep(1)
            keyboard.press(Key.enter)
            time.sleep(1)
            keyboard.release(Key.enter)
            time.sleep(1)

        except:
            print('image button failed trying next')
            self.driver.find_element(By.XPATH,
                                     '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/section/div[2]/ul/li[1]/div/div/span/button/span[1]').click()
            time.sleep(2)
            try:
                keyboard = Controller()
                time.sleep(1)
                keyboard.type(self.image_file)
                time.sleep(1)
                keyboard.press(Key.enter)
                time.sleep(1)
                keyboard.release(Key.enter)
                time.sleep(1)

            except:
                print('image upload failed check once.')

    def post_buttons(self):
        try:
            self.driver.find_element(By.CLASS_NAME,
                                     'share-box-footer__primary-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view').click()
            time.sleep(1)
        except:
            try:
                print('image done failed trying next')
                self.driver.find_element(By.XPATH,
                                         '/ html / body / div[3] / div / div / div / div[2] / div / div[2] / div / button[2]').click()
                time.sleep(1)
            except:
                print('image done failed check once')

        try:
            time.sleep(1)
            self.driver.find_element(By.CLASS_NAME,
                                     'share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view').click()
            time.sleep(1)
        except:
            try:
                print('post button failed trying next ')
                self.driver.find_element(By.XPATH,
                                         '/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/button').click()
                time.sleep(1)
            except:
                try:
                    print('post button failed 1 trying next ')
                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/button').click()
                    time.sleep(1)
                except:
                    print('post fail failed 1 trying next')
                    self.driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/div[3]/div/div[2]/button').click()
