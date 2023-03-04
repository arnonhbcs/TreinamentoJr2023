# Bibliotecas necessarias para automatizar o CookieClicker

from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
import time

# Caminho do webdriver e link do site
# PATH = "C:/ChromeWebdriver/chromedriver.exe"
URL = "https://orteil.dashnet.org/cookieclicker/"

# inicializando o site
with  webdriver.Chrome() as driver: 
    time.sleep(2)
    driver.get(URL)
    time.sleep(2)

    # Selecionando o portuguesBR como idioma do jogo
    try:
        idioma = driver.find_element(By.ID, "langSelect-PT-BR")
        idioma.click()
    finally:
        print('Idioma Selecionado')
    # Mapeando o elemento HTML do cookie.
    bigCookie = driver.find_element(By.ID, "bigCookie")

    # Loop do jogo
    while True:
        # Iterando cliques
        for i in range(20):
            bigCookie.click()
        
        # Condicional para a compra de itens
        try:
            items = driver.find_elements(By.CLASS_NAME, "enabled") # Armazenando os itens disponiveis em uma lista
            time.sleep(0.5) # Tempo para 'farmar' cookies antes de efetuar mais uma compra
            items[-1].click() # Escolhendo o mais caro
        except:
            pass
        if keyboard.is_pressed("q"): # Para encerrar o jogo
            break

print('Game Over')
time.sleep(2)
