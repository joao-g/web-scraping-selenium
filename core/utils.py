from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()
    options.add_argument("--headless")  # Executar em modo headless (sem interface gráfica)
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(executable_path="/path/to/chromedriver")  # Atualize com o caminho do chromedriver
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver
