from pynput.keyboard import Key, Listener
from pyfiglet import Figlet



def main():
    def on_press(key):
        if 'char' in dir(key):     #check if char method exists,
            if key.char == '/':    #check if it is 'q' key
                f = Figlet(font='slant')
                print(f.renderText('BSI x GEMINI'))

    def on_release(key):
        if key == Key.home:
            return False  # Stop listener

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        
main()