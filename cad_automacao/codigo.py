# Bibliotecas = pacotes de código
# pip install pyautogui

import pyautogui
import time

from mouseinfo import MouseInfoWindow

# pyautogui.click #clica
# pyautogui.write #escreve
# pyautogui.press #aperta uma tecla Mouse   1   25.95   6.5
# pyautogui.hotkey #aperta um atalho (hotkey)

pyautogui.PAUSE = 1   # pausa de 1 segundo entre os comandos
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "pythonimpressionador@gmail.com"

# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.click(x=921, y=183)

pyautogui.write(link)
pyautogui.press("enter")
# fazer uma pausa maior para o site carregar
time.sleep(3)

# Passo 2: Fazer login no site da empresa
# Clicar no campo de login
pyautogui.click(x=774, y=368)
pyautogui.write(email)
pyautogui.press("tab")  # passar para o próximo campo
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")  # pressionar o botão de login
time.sleep(3)  # esperar o site carregar

# Passo 3: Abrir a base de dados (importar o arquivo Excel)
# pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("produtos(1).csv")
print(tabela)  # exibir a tabela no terminal

for linha in tabela.index:

    # Passo 4: Cadastra 1 produtochrome
    pyautogui.click(x=827, y=259)  # clicar no campo código
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)  # escrever o código do produto
    pyautogui.press("tab")  # passar para o próximo campo

    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")  # passar para o próximo campo

    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")  # passar para o próximo campo

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")  # passar para o próximo campo

    # preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")  # passar para o próximo campo

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")  # passar para o próximo campo

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")  # passar para o botão enviar

    pyautogui.press("enter")  # pressionar o botão enviar

# volta pro início da tela
pyautogui.scroll(-10000000)
pyautogui.scroll(10000000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos para cada linha da base de dados