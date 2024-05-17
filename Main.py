import selenium
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from pynput.keyboard import Key, Listener
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from package.botBsi import BOT


edge_options = Options()
edge_options.add_experimental_option("debuggerAddress","127.0.0.1:3241")
edge_options.use_chromium = True
s = Service('msedgedriver.exe')
driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()), options = edge_options)
driver.get('https://elearning.bsi.ac.id/')

def main():
    
    print("Use '/' to render text and get the answer")
    def on_press(key):
        if 'char' in dir(key):
            if key.char == '/':
                BOT().ai(driver=driver)

    def on_release(key):
        if key == Key.home:
            return False  # Stop listener

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
main()
