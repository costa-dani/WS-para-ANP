import time
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Caminho para o diretório com o executável do ChromeDriver
caminho_chromedriver = r"C:\Users\danic\OneDrive\Área de Trabalho\wsANP\chromedriver-win64"

# Adiciona o caminho do executável do ChromeDriver ao PATH
os.environ["PATH"] += os.pathsep + r'C:\Users\danic\OneDrive\Área de Trabalho\wsANP\chromedriver-win64'

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# pPro Chrome ficar aberto
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
url = 'https://dados.gov.br/dados/conjuntos-dados/movimentacao-de-derivados-de-petroleo-e-biocombustiveis'
driver.get(url)

# Esperar o botão 'Recursos' ficar 'clicável'
botao_recursos = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-light btn-block m-1 dataset-btn botao-collapse-Recursos collapsed')]")))
botao_recursos.click()

# Esperar pra ter certeza de que tudo vai carregar
time.sleep(5)

# Achar e clicar no botão 'Acessar o recurso' 
botao_acessar_recurso = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[text()=' Acessar o recurso '])[6]")))

botao_acessar_recurso.click()

# Tempo pra baixar o arquivo
time.sleep(15)

# Especificar o diretorio do download
diretorio_download = os.path.expanduser("~") + "\\Downloads\\"

# Achar o arquivo ZIP
zip_file_path = None
for filename in os.listdir(diretorio_download):
    if filename.endswith('.zip'):
        zip_file_path = os.path.join(diretorio_download, filename)
        break

# Checar se o ZIP foi achado
if zip_file_path:
    # Especificar onde colocar os arquivos descompactados
    diretorio_final = os.path.expanduser("~") + "\\Downloads\\Dados_ANP\\"

    # Criar o diretório de extração, caso ele não exista
    os.makedirs(diretorio_final, exist_ok=True)

    # Extrair o arquivo ZIP
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(diretorio_final)

    print(f"Arquivo ZIP extraído para: {diretorio_final}")

else:
    print("Arquivo ZIP não foi achado no diretório do download.")