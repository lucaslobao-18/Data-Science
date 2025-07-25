import re

#search = re.search('Antonio','Rua Antonio Basilio')
#print(search)

#findall = re.findall('div','<div class=container> <div class=container>')
#print(findall)

#split = re.split('c','Descomplica')
#print(split)

#sub = re.sub  substitui um trecho que dê match por aquilo que vc quer

#Crio a minha regex e salvo no 'p'
p = re.compile(r'[0-9]+')
print(p.findall('12 campos de futebol, 10 bolas, 25 chuteiras'))