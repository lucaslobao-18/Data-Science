#!pip install selenium
 
#!pip install webdriver-manager
 
#!pip install pandas
 
#!pip install openpyxl
 
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
 
 
service = Service()
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
 
navegador = webdriver.Chrome(service = service, options=options)
 
 
lista_dou = []
 
for a in (1,2,3):
  navegador.get(f'https://www.in.gov.br/leiturajornal?&secao=do{a}&org=Minist%C3%A9rio%20dos%20Transportes')
 
  for i in (1,2,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5):
    try:
      navegador.find_element('xpath',f'//*[@id="hierarchy_content"]/div/span[{i}]').click()
    except:
        pass
 
    for c in range (1,11):
        try:
          linkweb = navegador.find_element(By.XPATH,f'/html/body/div[1]/div[1]/main/div[2]/div/div[2]/div/div/div/div[4]/section/div/div[2]/div/div[4]/div[2]/ul/li[{c}]/div/h5/a').get_attribute('href')
          titulo = navegador.find_element(By.XPATH,f'//*[@id="hierarchy_content"]/ul/li[{c}]/div/h5/a').text
          resumo = navegador.find_element(By.XPATH,f'//*[@id="hierarchy_content"]/ul/li[{c}]/div/p').text
          departamento = navegador.find_element(By.XPATH,f'//*[@id="hierarchy_content"]/ul/li[{c}]/div/ol/li[3]').text
          secao = navegador.find_element(By.XPATH,f'//*[@id="hierarchy_content"]/ul/li[{c}]/div/ol/li[1]').text
          detalhamento = navegador.find_element(By.XPATH,f'//*[@id="hierarchy_content"]/ul/li[{c}]/div/ol').text
          lista_dou.append([titulo,resumo,departamento,secao,detalhamento,linkweb])
          lista_dou.drop_duplicates()
        except:
            pass
 
 
 
 
 
dou = pd.DataFrame(lista_dou, columns=['Título','Resumo','Departamento','Seção','Detalhamento','Link'])
dou_limpo = dou.drop_duplicates()
dou_limpo.to_excel('DOU_MT.xlsx', index=False)