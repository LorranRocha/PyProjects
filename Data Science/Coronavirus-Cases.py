#   Created By: Lorran Rocha
#   Using python: 3.6.9

import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

#   Função para receber informações sobre Coronavirus
res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()

#   Função para Notificação
def notfyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        timeout = 5)

print('Pressione CTRL + C para encerrar o programa')

while True:
    notfyMe('Número total de casos',cases)
    time.sleep(10)        

