## DBSCAN
É um algoritmo de clusterização não supervisionado baseado em densidade, bom para identificar outliers. Considera pontos mais isolados como ruído

Usa 2 parêmetros principais, eps(epsilon) = raio de vizinhança, min_samples = Número mínimo de vizinhos dentro do raio

### Vantagens
- Não precisa especificar número de clusters previamente
- Lida bem com ruídos

### Desvantagens
- A escolha do raio e o mínimo de vizinhos influencia muito no resultado
- Pode encontrat dificuldades com clusters de densidades muito diferentes