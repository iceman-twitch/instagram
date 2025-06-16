import time
import requests
import random 
import string
import re
import json
import sys
import os, platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


capabilities = {
    "browserName": "chrome",
    "version": "78.0",
    "enableVNC": True,
    "enableVideo": False
}

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return str(''.join(random.choice(lettersAndDigits) for i in range(stringLength)))

def check_proxy(proxy):

    code=404

    try:
        proxydict = {
            'http': proxy
        }
        r =requests.get("https://instagram.com",proxies=proxydict)
        
        # print(r.status_code)
        code=r.status_code

    except Exception as e:

        print("ERROR:" + str(e))

    return code

def get_proxy():
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open( cwd + "\proxy4777.txt" ) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    
        
    return lines[random.randint(0,len(lines)-2)]



class Bot:
    def __init__( self, a = '', b = '', c = '', d = '', l = 'https://instagram.com' ):
        self.a = a
        self.b = randomStringDigits(12)
        self.d = c
        self.host = d
        self.s = requests.Session()
        self.success=False
        self.driver=0
        self.private=False
        self.stream=l
        #self.proxy = get_proxy()
        self.like=""
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

        self.user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        self.user_agent = self.user_agent_rotator.get_random_user_agent()

    def Browser_Quit( self ):
        time.sleep(3)
        self.driver.close()
        exit()

    def Browser_StartHeadless( self ):
        chrome_options = Options()
        # chrome_options.add_argument(f'--proxy-server={self.proxy}')
        chrome_options.add_argument("--headless") 
        self.driver = webdriver.Remote(
            command_executor="http://"+ self.host +":4444/wd/hub",
            desired_capabilities=capabilities,
            options=chrome_options
            )
        
        self.driver.implicitly_wait(55)
        self.driver.set_page_load_timeout(55)
        self.driver.get(self.stream)

    def Browser_StartHeadless_Local( self ):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        if platform.system() == 'Windows':
            chromepath = BASE_DIR + r'\chromedriver.exe'
            chromepath = chromepath.replace("\\","/")
        # print("1")
        options = Options()
        # print("2")
        # options.add_argument(f'proxy-server={ self.proxy }')
        # print("3")
        options.add_argument('--headless')
        # print("4")
        options.add_argument('--disable-gpu')
        # print("5")
        options.add_argument('--lang=en')
        options.add_argument("user-agent="+self.user_agent+"")
        # print("6")
        # self.driver = webdriver.Remote(
        #     command_executor="http://"+ self.host +":4444/wd/hub",
        #     desired_capabilities=capabilities,
        #     chrome_options=options
        #     )
        self.driver = webdriver.Chrome(executable_path=chromepath, options=options)
        # print("7")
        self.driver.implicitly_wait(55)
        # print("8")
        self.driver.set_page_load_timeout(55)
        # print("9")
        self.driver.get(self.stream)
        print("BROWSER STARTED")

    def Browser_Start( self ):
        chrome_options = Options()
        # options.add_argument(f'--proxy-server={self.proxy}')
        chrome_options.add_argument("user-agent="+self.user_agent+"")
        self.driver = webdriver.Remote(
            command_executor="http://"+ self.host +":4444/wd/hub",
            desired_capabilities=capabilities,
            options=chrome_options
            )
        
        self.driver.implicitly_wait(55)
        self.driver.set_page_load_timeout(55)
        self.driver.get(self.stream)
        print("BROWSER STARTED")

    def Browser_Start_Local( self ):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        if platform.system() == 'Windows':
            chromepath = r'd:\\0\\python\\chromedriver.exe'
            chromepath = chromepath.replace("\\","/")
        options = Options()
        #options.add_argument( f'--proxy-server={ self.proxy }' )
        options.add_argument( "user-agent=" + self.user_agent )
        self.driver = webdriver.Chrome(executable_path=chromepath, 
        # options=options
        )
        
        self.driver.implicitly_wait(55)
        self.driver.set_page_load_timeout(55)

        

        self.driver.get(self.stream)
        #self.driver.add_cookie( { 'expiry': 4773923917, 'httpOnly': False, 'name': 'ig_cb', 'path': '/', 'secure': False, 'value': '2'} )

    def Get( self, url = '' ):
        self.driver.get( url )

    def Browser_Register( self):
        time.sleep(3)
    
    def Browser_Login( self ):
        time.sleep(3)

    def Browser_Report( self ):
        # '//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/svg'

        # check = self.driver.find_element_by_xpath('//*[@id="omlet-bar"]/div[2]/div[5]')        
        # self.driver.get(self.like)
        time.sleep(3)
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
        #     )
            
        # finally:
        #     print("Failed to Like")
        # like = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[6]/div[2]/div[1]')
        # like.click()

        class_name1="AFWDX"
        class_name2="wpO6b "
        classnames=[class_name1,class_name2]
        
        xpath1 = '//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/svg'
        xpath2 = '/html/body/div[1]/section/main/div/header/section/div[1]/div'
        xpaths=[xpath1,xpath2]
        check=False
        timeout=2
        try:
            for i in range(0,4):
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, classnames[i]))).click()
                check=True
        except:
            check=False
            try:
                for i in range(0,7):
                    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpaths[i]))).click()
                    check=True
            except:
                check=False

        if check:
            print("IG OPTIONS CLICKED ( "+ self.a +" )")
        else:
            print("FAILED TO CLICK OPTIONS ( "+ self.a +" )")

        # 'aOOlW -Cab_   '
        # '/html/body/div[4]/div/div/div/button[3]'

        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]'

        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[2]/div/div[1]'


        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]/div'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]'

        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[7]/div/div[1]'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[7]/div'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[7]'


        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]'
        # '/html/body/div[4]/div/div/div[2]/div/div/div/div[3]/button[1]/div'
        
        # '/html/body/div[4]/div/div/div[2]/div/div/div[4]'
        # '/html/body/div[4]/div/div/div[2]/div/div/button'

        # self.Browser_Quit()
        # self.Browser_Watch()

    def GetCookies( self ):
        
        cookies_list = list( json.dumps( self.driver.get_cookies() ) )
        print( str( self.driver.get_cookies() ) )

    def AcceptCookies( self ):
        time.sleep( 1 )
        clicked = False
        button = '/html/body/div[2]/div/div/div/div[2]/button[1]'
        timeout = 10
        try:
            WebDriverWait( self.driver, timeout ).until( EC.element_to_be_clickable( ( By.XPATH, button) ) ).click()
            clicked = True
        except:
            print( 'No Accept Cookies Button' )
            return

        print( 'Cookies Accepted' )
        return

    def Login( self ):
        time.sleep( 1 )
        url = 'https://www.instagram.com/accounts/login/'

        self.Get( url )
        
        input_u = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        input_p = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        button_l = '/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button'
        timeout = 10
        try:
            x = WebDriverWait( self.driver, timeout ).until( EC.element_to_be_clickable( ( By.XPATH, input_u ) ) )
            x.click()
            x.send_keys( '123456' ) # send keys to simulate keyboard
            try:
                x = WebDriverWait( self.driver, timeout ).until( EC.element_to_be_clickable( ( By.XPATH, input_p ) ) )
                x.click()
                x.send_keys( '123456' ) # send keys to simulate keyboard
                try:
                    x = WebDriverWait( self.driver, timeout ).until( EC.element_to_be_clickable( ( By.XPATH, button_l ) ) )
                    x.click()
                except:
                    a = 1
            except:
                a = 1
        except:
            a = 1

def test_1():

    ig = Bot()
    ig.Browser_Start_Local()
    ig.AcceptCookies()
    ig.Login()
    time.sleep(15)

test_1()