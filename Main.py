from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\Kobaldo\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://the-internet.herokuapp.com/login")

    def enviarDados(usuario, senha):
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        senha_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/button/i'))
        )
        email_login.clear
        senha_login.clear
        email_login.send_keys(usuario)
        senha_login.send_keys(senha)
        btn_login.click()
        driver.implicitly_wait(5)  
        alert = driver.find_element(By.ID, "flash").text
        return alert
    
    alert = enviarDados('Rodrigo','SuperSecretPassword!')
    if 'Your username is invalid' in alert :
        print("Teste de usuário inválido bem sucedido")
    else:
        print("Usuário incorreto não reconhecido, teste falhou")
    
    alert = enviarDados('tomsmith','senhaQualquer')
    if 'Your password is invalid' in alert:
        print("Teste de senha inválida bem sucedido")
    else:
        print("Senha incorreta não reconhecida, teste falhou")

    alert = enviarDados("tomsmith","SuperSecretPassword!")
    if 'You logged into a secure area' in alert:
        print("Teste de login bem sucedido")
    else:
        print("Falaha ao efetuar login, teste falhou")

    print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()