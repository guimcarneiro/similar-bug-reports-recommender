# Dataset

No link abaixo é possível acessar um _dump_ do banco de dados MongoDB utilizado para os experimentos executados no presente estudo. A seguir, também é apresentada cada entidade pertencente ao mesmo, com o objetivo de facilitar a replicação dos experimentos, caso venha a ser necessário.

[Link para acesso ao dump](https://drive.google.com/drive/folders/1aAbZG5oEazgpst42e3T9IdExRLL54-ET?usp=sharing)

## Objetivo

O objetivo do presente dataset foi armazenar Bug Reports e suas informações necessárias para calcular recomendações baseadas em similaridade textual. Para isso, utilizamos duas entidades principais: o _bug_, referente ao Bug Report, e o _arc_, referente ao Arco de Similaridade, que armazena informações sobre a similaridade entre um par de Bug Reports.

Por fim, após a execução dos testes, salvamos os resultados em uma terceira entidade, chamada de _result_, de onde foi possível plotar gráficos, por exemplo.

## Entidades

### **Bug Report ("bug")**

![image](https://user-images.githubusercontent.com/32914505/216782047-0a64e7b4-f0fb-400d-86fb-e38ffb5875ea.png)

A maioria dos campos se mantém igual à API do Bugzilla ([link](https://bmo.readthedocs.io/en/latest/using/understanding.html)), excetuando-se pelos campos abaixo:

- **"when_changed_to_resolved"**: Informação foi recuperada por meio do histórico de alterações de cada BR, também disponível na API do Bugzilla, e se refere à quando um Bug Report foi alterado para status _RESOLVED_. A partir dele foi possível saber quais Bug Reports estavam abertos para cada _query_, e assim poder buscar por candidatos válidos, de acordo com o oráculo.

- **"when_final_change_assigned_to"**: Não foi utilizado, mas se refere à quando o último responsável foi definido para o Bug Report.

- **"embeddings_vector"**: Se refere ao binário dos word embeddings calculados para o respectivo Bug Report. Para poder utilizá-lo, pode-se utilizar a biblioteca "pickle", através do "pickle.load".

- "tfidf_vector": Se refere ao binário do vetor gerado pelo TF-IDF calculado para o respectivo Bug Report. Para poder utilizá-lo, pode-se utilizar a biblioteca "pickle", através do "pickle.load".


### **Arco de Similaridade ("arc")**

![image](https://user-images.githubusercontent.com/32914505/216782431-d41c67c3-d28d-4908-b48b-1a9e01c4be9c.png)

- **"from"**: A partir de qual Bug Report se está calculando a similaridade.
- **"to"**: Em relação à qual Bug Report se está calculando a similaridade. Par from-to guarda informações de similaridade entre 2 BRs.
- **"categoric_similarity"**: Como explicado no TCC, o cruzamento dos campos "product" e "component" geram um valor de similaridade, podendo ser 1, 0.5 ou 0.
- **"cos_similarity_tfidf"**: Como explicado no TCC, esse campo se refere à similaridade de cosseno entre os vetores TF-IDF gerados pelo campo de descrição dos BRs dos campos "from" e "to".
- **"cos_similarity_word_embeddings"**: Como explicado no TCC, esse campo se refere à similaridade de cosseno entre os word embeddings gerados pelo campo de descrição dos BRs dos campos "from" e "to".

### **Resultado ("result")**

![image](https://user-images.githubusercontent.com/32914505/216782608-f1294fbf-6ace-412a-a24f-81327d3374a8.png)

- **"version"**: Se refere à qual técnica de cálculo de score de similaridade foi utilizada para obter tal resultado. No TCC, elas são apresentadas como TP (_categoric_tfidf_we_), T1 (_categoric_tfidf_) e T2 (_categoric_we_).
- **"feedback"**: Métrica de feedback.
- **"precision"**: Métrica de precisão.
- **"likelihood"**: Métrica de likelihood.
- **"query"**: Se refere à qual BR que serviu de entrada para o resultado obtido.
- **"recommendations"**: Se refere à lista ordenada de recomendações obtidas a partir da inserção do BR do campo _query_ como entrada. Ele contem os campos **"bg_number"** (ID do BR), **"score"** (score de similaridade), **"relevant"** (se aquele BR foi ou não relevante, considerando o oráculo proposto no TCC).
