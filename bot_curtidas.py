from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoEsperada
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #para usar as teclas do teclado
from time import sleep

def iniciar_driver():
    chorome_options = Options()
    arguments = ["--lang=pt-BR","--incognito","--window-size-1300,1000"]
    for argument in arguments:
        chorome_options.add_argument(argument)

    chorome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()),options=chorome_options)
    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
        NoSuchElementException,       
        ElementNotVisibleException,
        ElementNotSelectableException])

    return driver, wait


driver, wait = iniciar_driver()
driver.get("https://www.instagram.com/")
sleep(2)
campo_email = driver.find_element(By.XPATH,"//input[@aria-label='Telefone, nome de usuário ou email']")
driver.execute_script("arguments[0].click()",campo_email)
campo_email.send_keys("")

sleep(1)

campo_senha = driver.find_element(By.XPATH, "//input [@aria-label='Senha']")
driver.execute_script("arguments[0].click()",campo_senha)
campo_senha.send_keys("")

sleep(1)

botao_entrar = driver.find_element(By.XPATH,"//div[text()='Entrar']")
driver.execute_script("arguments[0].click()",botao_entrar)
sleep(5)

explorar = driver.find_element(By.XPATH,"//span[text()='Explorar']")
driver.execute_script("arguments[0].click()",explorar)
sleep(2)
postagem = driver.find_elements(By.XPATH,"//div[@class='_aagu']")
driver.execute_script("arguments[0].click()",postagem[0])
sleep(2)

perfil = driver.find_element(By.XPATH,"//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']")
sleep(2)
perfil.click()

sleep(6)

seguir = driver.find_element(By.XPATH,"//div[@class='_ap3a _aaco _aacw _aad6 _aade']")
seguir.click()

sleep(2)

postagem_perfil = driver.find_elements(By.XPATH,"//div[@class='_aagu']")
postagem_perfil[0].click()

sleep(2)


curtida = driver.find_element(By.XPATH,"//span[@class='_aamw']")
curtida.click()

sleep(2)

proximo = driver.find_elements(By.XPATH,"//button[@class='_abl-']")
driver.execute_script("arguments[0].click()",proximo[0])
sleep(1)
curtida = driver.find_element(By.XPATH,"//span[@class='_aamw']")
curtida.click()

sleep(2)
for proximo in range(2):
    proximo2 = driver.find_elements(By.XPATH,"//button[@class='_abl-']")
    driver.execute_script("arguments[0].click()",proximo2[1])
    sleep(1)
    curtida = driver.find_element(By.XPATH,"//span[@class='_aamw']")
    curtida.click()
    sleep(2)


input("")