# Machine-learning


### Lista de Exercícios 12
* Faça a clusterização do dataset [deste link](https://raw.githubusercontent.com/datascienceinc/learn-data-science/master/Introduction-to-K-means-Clustering/Data/data_1024.csv) usando o algoritmo k-means++.  
* O dataset possui os seguintes dados de motoristas: a distância média dirigida por dia e a média percentual do tempo que um motorista estava 5mph acima do limite de velocidade.  
* Portanto, agrupe os motoristas pela similaridade das features acima usando o algoritmo k-means++.  
* Use o método do cotovelo (Elbow Method) e a análise de silhueta (Silhouette Analysis) para identificar o melhor valor de k.
* Mostre ambos graficamente.
* Na análise de silhueta, para o melhor valor encontrado para k, mostre: k-1, k e k+1.  
* Para o mesmo valor de k obtido acima, execute o k-means original com inicialização totalmente randômica.  
* Compare os resultados de k-means e k-means++ (1) graficamente, (2) tempo de execução e (3) número mínimo de iterações necessárias para chegar ao melhor resultado.

### Lista de Exercícios 13
* Use o dataset da Lista 12 para:
  + Fazer clusterização hierárquica (HC) usando os seguintes métodos e mostrando os dendrogramas para:
    + Single
    + Complete
    + Average
* Escolher uma clusterização hierárquica do item 1 e, a partir dela, escolher uma linha de corte e mostrar os clusters no gráfico.
  * Fazer clusterização DBSCAN com diferentes valores de eps e minPoints.
* Escolher um resultado do item 3 e, a partir dele, mostrar os clusters no gráfico.
* Questões conceituais:
  + Quais as diferenças entre feature selection e feature extraction? 
  + Dê exemplos de técnicas usadas para feature selection.
  + Dê exemplos de técnicas usadas para feature extraction. 
* Use o iris dataset e a partir dele:
  + Reduza a dimensionalidade para 2 dimensões usando PCA, e  mostre os pontos em um gráfico, onde cada classe é visualizada com uma cor diferente. 
  + Reduza a dimensionalidade para 2 dimensões usando LDA, e  mostre os pontos em um gráfico, onde cada classe é visualizada com uma cor diferente. 
