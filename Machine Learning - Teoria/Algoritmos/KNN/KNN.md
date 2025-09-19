## KNN (K-Nearest Neighbors)

Aprendizado Supervisionado, Usado para Classificação e Regressão

### Funcionamento
Basicamente o KNN pega o novo ponto inserido que vc quer classificar, faz uma análise dos seus vizinhos mais próximos, e a classe mais comum entre os K vizinhos é atribuída a esse ponto.

Um K muito pequeno pode ser sensível a ruídos, outlaiers, e um K grande é mais estável porém pode suavizar demais a classificação.

K é a quantidade de vizinhos que será analisada

Os vizinhos mais próximos são calculados com distância euclideana.

### Características
- Facil de Entender
- É bastante efetivo para um grande conjunto de dados
- Não aprende nada (Lazy learner)
- Não é bom para muitas dimensões

