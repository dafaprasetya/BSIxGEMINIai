from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium import webdriver
from time import sleep
from plyer import notification
from gemini import Gemini
from pynput.keyboard import Key, Listener
import os


def geminiai(soal):
    try:
        test = open('cookies.json')
        jonson = json.load(test)
        for i in jonson:
            if i['name'] == "__Secure-1PSIDCC":
                # print(i["value"])
                psidcc = i["value"]
            if i['name'] == "__Secure-1PSID":
                # print(i["value"])
                psid = i["value"]
            if i['name'] == "__Secure-1PSIDTS":
                # print(i["value"])
                psidts = i["value"]
            if i['name'] == "NID":
                # print(i["value"])
                nid = i["value"]


        cookies = {
            "__Secure-1PSIDCC" : psidcc,
            "__Secure-1PSID" : psid,
            "__Secure-1PSIDTS" : psidts,
            "NID" : nid,
        }

        client = Gemini(cookies=cookies)
        prompt = soal
        response = client.generate_content(prompt)
        print(response.text)
        notification.notify(title="jawabnmu telah datang!",message=response.text,app_name="",timeout=1 )
        
    except:
        options = webdriver.EdgeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        options.add_experimental_option("useAutomationExtension", False)
        # options.add_experimental_option("detach", True)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--log-level=3")
        # options.add_experimental_option("detach", True)
        if os.name != "nt":
            options.add_argument("user-data-dir=Ujang Shelby")
            options.add_argument("profile-directory=Ujang Shelby")

        options.add_argument('--remote-debugging-port=3251')
        options.add_argument('--start-maximized')
        path = Service('msedgedriver.exe')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
        driver.get("https://gemini.google.com/app")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id='gb']/div/div[1]/div[2]/div/a")))
        try : 
            cookies = driver.get_cookies()
            with open('cookies.json', 'w', newline='\n') as outputdata:
                json.dump(cookies, outputdata)
            test = open('cookies.json')
            jonson = json.load(test)
            for i in jonson:
                if i['name'] == "__Secure-1PSIDCC":
                    # print(i["value"])
                    psidcc = i["value"]
                if i['name'] == "__Secure-1PSID":
                    # print(i["value"])
                    psid = i["value"]
                if i['name'] == "__Secure-1PSIDTS":
                    # print(i["value"])
                    psidts = i["value"]
                if i['name'] == "NID":
                    # print(i["value"])
                    nid = i["value"]
            cookies = {
                "__Secure-1PSIDCC" : psidcc,
                "__Secure-1PSID" : psid,
                "__Secure-1PSIDTS" : psidts,
                "NID" : nid,
            }
            
        except UnboundLocalError:
            print("failed trying again.......")
            driver.get("https://gemini.google.com/app")
            sleep(10)
            cookies = driver.get_cookies()
            with open('cookies_1.json', 'w', newline='\n') as outputdata:
                json.dump(cookies, outputdata)
            test = open('cookies_1.json')
            jonson = json.load(test)
            for i in jonson:
                if i['name'] == "__Secure-1PSIDCC":
                    # print(i["value"])
                    psidcc = i["value"]
                if i['name'] == "__Secure-1PSID":
                    # print(i["value"])
                    psid = i["value"]
                if i['name'] == "__Secure-1PSIDTS":
                    # print(i["value"])
                    psidts = i["value"]
                if i['name'] == "NID":
                    # print(i["value"])
                    nid = i["value"]
            cookies = {
                "__Secure-1PSIDCC" : psidcc,
                "__Secure-1PSID" : psid,
                "__Secure-1PSIDTS" : psidts,
                "NID" : nid,
            }
        client = Gemini(cookies=cookies)
        prompt = soal
        response = client.generate_content(prompt)
        print(response.text)
        
# geminiai("hai")
