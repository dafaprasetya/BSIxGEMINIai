import time
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from gemini import Gemini
import pynput
from pynput.keyboard import Key, Listener
from geminih import geminiai

def readtxt(txt):
    try:
        with open(txt,'r') as file:
            isi_file = file.read()
        return isi_file
    except FileNotFoundError:
        print(f"file'{txt}' tidak ditemukan.")
        return None
    except Exception as e:
        print("terjadi kesalahan: {e}")
        return None
def end():
    print("program terhenti")
    driver.quit()
def triger():
    try:
        
        soal = driver.find_element(By.XPATH, '//*[@id="nomerurut"]').text
        A = "A. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[3]/table/tbody/tr/td[2]').text
        B = "B. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[4]/table/tbody/tr/td[2]').text
        C = "C. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[5]/table/tbody/tr/td[2]').text
        D = "D. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[6]/table/tbody/tr/td[2]').text
        E = "E. "+driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div[7]/table/tbody/tr/td[2]').text
        full = soal + '\n'+ A+ '\n'+B+ '\n'+C+ '\n'+D+ '\n'+E+"\n"+"pilih A, B, C, D atau E tanpa kesimpulan atau penjelasan atau alasan hanya jawab A,B,C,D atau E"
        print(full)
        geminiai(full)
    except:
        print("Yahahah gagal")
        
def main():
    def on_press(key):
        if key == Key.ctrl_l:
            triger()

    def on_release(key):
        if key == Key.esc:
            return False  # Stop listener

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


edge_options = Options()
edge_options.add_experimental_option("debuggerAddress","127.0.0.1:3241")
edge_options.use_chromium = True
driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
driver.get(readtxt('url.txt'))
main()

