import time
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from gemini import Gemini
import pynput
from geminih import geminiai
from pynput.keyboard import Key, Listener
from pyfiglet import Figlet
import os

#RUN EDGE WITH PORT 3241
print("checking cookie.....")
f = Figlet(font='slant')
print(f.renderText('UBSI x GEMINIAI'))
print("by: dafa_prstya")
print("Checking for cookie........")    
geminiai("Hai") #check cookie
print("Cookie success!")
# os.system('cls' if os.name == 'nt' else 'clear')

pil = input("Run edge?(y/n, default n)\n# ")

if pil == "y":
    print("Running edge")
    options = webdriver.EdgeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--log-level=3")
    options.add_experimental_option("detach", True)
    options.add_argument('--remote-debugging-port=3241')
    options.add_argument('--start-maximized')
    path = Service('msedgedriver.exe')
    driver2 = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options) #windows user change "service=EdgeService(EdgeChromiumDriverManager().install())" to "service=PATH TO EDGEWEBDRIVER"

class BOT:
    def ai(self, driver):
        try:
        
            soal = driver.find_element(By.XPATH, '//*[@id="nomerurut"]').text
            A = "A. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[3]/table/tbody/tr/td[2]').text
            B = "B. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[4]/table/tbody/tr/td[2]').text
            C = "C. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[5]/table/tbody/tr/td[2]').text
            D = "D. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[6]/table/tbody/tr/td[2]').text
            E = "E. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[7]/table/tbody/tr/td[2]').text
            full = soal + '\n'+ A+ '\n'+B+ '\n'+C+ '\n'+D+ '\n'+E+"\n"+"jawab dengan benar dan akurat, pilih A, B, C, D atau E tanpa kesimpulan atau penjelasan atau alasan hanya jawab A,B,C,D atau E jawab dengan satu baris dengan benar dan akurat"
            print(full)
            geminiai(full)
        except:
            print("Yahahah gagal")
