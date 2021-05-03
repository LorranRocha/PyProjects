import pyautogui
import time
import requests
from bs4 import BeautifulSoup

def bot_spam(url, tag): #A função pega uma url, e uma tag HTML
    time.sleep(10)

    req = requests.get(url)
    parse = BeautifulSoup(req.text, 'html.parser')
    html = parse.find_all(tag)
    print(html)

    for mensagem in html:
        pyautogui.typewrite(mensagem.get_text())
        pyautogui.press("enter")

bot_spam('http://www.seulinkaqui.com.br', 'tag html, por exemplo: p')    #Coleta o link do site e o tipo de Tag que será utilizada
