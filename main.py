import time
import pyautogui
from time import sleep
import os
from pathlib import Path

####### Coordenadas do PC Desktop ##########
#### Btn login = 770,543
#### Campo Produto = 750,419
#### Campo Quantidade = 730,488
#### Campo Preço = 729,554
#### Btn Registrar = 728,593
############################################

# Obtém o diretório atual do script
current_dir = Path(__file__).parent

# Constrói o caminho absoluto para o ícone com base no diretório do script
file_path = current_dir / "produtos.txt"

if not os.path.isfile(file_path):
    print(f"Arquivo '{file_path}' não encontrado.")
    
else:
    print(f"Arquivo '{file_path}' encontrado prosseguindo...")
    time.sleep(6)

    # 3 - Clicar em Entrar
    #pyautogui.click(290,375, duration=1)
    pyautogui.click(770,543, duration=1) #Botão Login Notebook

    with open(file_path, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            produto = linha.split(',')[0]
            quantidade = linha.split(',')[1]
            preco = linha.split(',')[2]

            # 4 - Clicar e digitar o produto
            pyautogui.click(750,419, duration=0.3)
            pyautogui.write(produto)

            # 5 - Clicar e digitar a quantidade
            pyautogui.click(730,488, duration=0.3)
            pyautogui.write(quantidade)

            # 6 - Clicar e digitar o preco
            pyautogui.click(729,554, duration=0.3)
            pyautogui.write(preco)

            # 4 - Clicar em registrar
            pyautogui.click(728,593, duration=0.3)
