# AUTOMATIZAÇÃO DE TAREFAS NO PC COM O PYAUTOGUI

#Passo 1 ---> ENTRAR NO SISTEMA

import pyautogui # verificar documentação do pyautogui para saber os comandos
import time

from trio import CapacityLimiterStatistics

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 2 # pausa entre os comandos 

# abrir o navegador (chrome)
pyautogui.press("win") # pressionar tecla do Windowns
pyautogui.write("chrome") # escrever chrome
pyautogui.press("enter") # apertar enter
# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4.5) # PARA GARANTIR QUE CARREGOU O SITE

#Passo 2 ---> FAZER LOGIN
# selecionar o campo de email
pyautogui.click(x=-1021, y=-154)  # FEITO COM AJUDA DO ARQUIVO AUXILIAR
# escrever o seu email
pyautogui.write("maria.flu@hotmail.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=-810, y=4) # CLICAR NO BOTÃO
time.sleep(4.5) # tempo por garantia

# Passo 3 ---> Importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv") # Nome da variavel sempre em minusculo, sem caracteres especiais etc
print (tabela)

# Passo 4 ---> Cadastrar um produto
#para cada linha da minha tabela:
for linha in tabela.index: # looping da index (linhas da tabela)
    # clicar no campo de código
    pyautogui.click(x=-982, y=-272) 
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
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
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
