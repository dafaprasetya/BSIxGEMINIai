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


def geminiai(soal, a,b,c,d,e):
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
        edge_options = Options()
        edge_options.add_experimental_option("debuggerAddress","127.0.0.1:3241")
        edge_options.use_chromium = True
        s = Service('msedgedriver.exe')
        response = client.generate_content(prompt)
        if str(a) in response.text[:50]:
            print("jawabannya A")
            driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[3]/table/tbody/tr/td[2]').click()
        elif str(b) in response.text[:50]:
            print("jawabannya B")
            driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[4]/table/tbody/tr/td[2]').click()
            # b.click()
        elif str(c) in response.text[:50]:
            driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[5]/table/tbody/tr/td[2]').click()
            print("jawabannya C")
            # c.click()
        elif str(d) in response.text[:50]:
            driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[6]/table/tbody/tr/td[2]').click()
            print("jawabannya D")
            # d.click()
        elif str(e) in response.text[:50]:
            driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[7]/table/tbody/tr/td[2]').click()
            print("jawabannya E")
            # e.click()
        else:
            print("Yahahah gagal")
        print(response.text[:50])
        notification.notify(title="jawabnmu telah datang!",message=response.text,app_name="",timeout=1)
        
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
        if str(a) in response.text[:50]:
            print("jawabannya A")
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[3]/table/tbody/tr/td[2]').click()
        elif str(b) in response.text[:50]:
            print("jawabannya B")
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[4]/table/tbody/tr/td[2]').click()
            # b.click()
        elif str(c) in response.text[:50]:
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[5]/table/tbody/tr/td[2]').click()
            print("jawabannya C")
            # c.click()
        elif str(d) in response.text[:50]:
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[6]/table/tbody/tr/td[2]').click()
            print("jawabannya D")
            # d.click()
        elif str(e) in response.text[:50]:
            driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[7]/table/tbody/tr/td[2]').click()
            print("jawabannya E")
            # e.click()
        else:
            print("Yahahah gagal")
        
        print(response.text)
        
# geminiai("hai")
