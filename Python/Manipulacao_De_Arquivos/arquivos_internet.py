#Lendo arquivo da internet
import requests
ler = requests.get("https://dados.al.gov.br/catalogo/dataset/d8a3b0a3-1f18-48b0-a4d4-18871502d635/resource/2f35f0ca-5be0-4584-9ed9-3f9435595be0/download/informacoessobreoformatodosarquivos-novo.txt")
print(ler.content)

# with open("arquivo2.txt", "wb") as arquivo:
#     arquivo.write(ler.content)