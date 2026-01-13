# pip install pyautogui

import pyautogui
import time

# pyautogui.click -> clica
# pyautogui.write -> escreve um texto
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
pyautogui.press("win")
pyautogui.write("Opera GX")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(3)

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=846, y=367)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab")
pyautogui.write("sua senha muito muito muito dificilima")

pyautogui.press("tab")
pyautogui.press("enter")
# fazer uma pausa maior pro site carregar
time.sleep(4)

# Passo 3: Abrir a base de dados
# pip install pandas openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
# Passo 4: Cadastrar 1 produto
    pyautogui.click(x=724, y=245)
    codigo = tabela.loc[linha, "codigo"]
    #codigo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos



