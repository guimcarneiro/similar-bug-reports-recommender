# Dataset

In the link provided below, it is possible to access a dump of the MongoDB database used for the experiments conducted in the present study. Furthermore, each entity belonging to the database is also presented, aiming to facilitate the replication of the experiments, if deemed necessary.

[Link to dump](https://drive.google.com/drive/folders/1aAbZG5oEazgpst42e3T9IdExRLL54-ET?usp=sharing)

## Objective

O objetivo do presente dataset foi armazenar Bug Reports e suas informações necessárias para calcular recomendações baseadas em similaridade textual. Para isso, utilizamos duas entidades principais: o _bug_, referente ao Bug Report, e o _arc_, referente ao Arco de Similaridade, que armazena informações sobre a similaridade entre um par de Bug Reports.

The purpose of the present dataset was to store Bug Reports and their necessary information for calculating recommendations based on textual similarity. To achieve this, we employed two main entities: the _bug_, pertaining to the Bug Report, and the _arc_, pertaining to the similarity arc, which stores information about the similarity between a pair of Bug Reports.

Finally, after the execution of the tests, we saved the results in a third entity called _result_, from which it was possible to generate plots, for instance.

## Entities

### **Bug Report ("bug")**

![image](https://user-images.githubusercontent.com/32914505/216782047-0a64e7b4-f0fb-400d-86fb-e38ffb5875ea.png)

The majority of fields remain consistent with the Bugzilla API ([link](https://bmo.readthedocs.io/en/latest/using/understanding.html)), with the exception of the following fields:

- **"when_changed_to_resolved"**: Information was retrieved through the change history of each Bug Report, also available in the Bugzilla API, and it pertains to when a Bug Report was changed to the _RESOLVED_ status. From this information, it was possible to determine which Bug Reports were open for each query, enabling the search for valid candidates according to the oracle.

- **"when_final_change_assigned_to"**: Although not utilized, it refers to when the last assignee was set for the Bug Report.

- **"embeddings_vector"**: It refers to the binary representation of the word embeddings calculated for the respective Bug Report. To make use of it, one can utilize the "pickle" library by employing the "pickle.load" function.

- **"tfidf_vector"**: It refers to the binary representation of the TF-IDF calculated for the respective Bug Report. To make use of it, one can utilize the "pickle" library by employing the "pickle.load" function.


### **Similarity Arc ("arc")**

![image](https://user-images.githubusercontent.com/32914505/216782431-d41c67c3-d28d-4908-b48b-1a9e01c4be9c.png)

- **"from"**: The Bug Report that is being used as the basis for calculating the similarity.
- **"to"**: Regarding which Bug Report the similarity is being calculated in relation to. The "from-to" field stores information about the similarity between two Bug Reports.
- **"categoric_similarity"**: As explained in the article, the combination of the "product" and "component" fields generates a similarity value that can be either 1, 0.5, or 0.
- **"cos_similarity_tfidf"**: As explained in the article, this field refers to the cosine similarity between the TF-IDF vectors generated from the description field of the Bug Reports in the "from" and "to" fields.
- **"cos_similarity_word_embeddings"**: As explained in the article, this field refers to the cosine similarity between the word embeddings generated from the description field of the Bug Reports in the "from" and "to" fields.

### **Results ("result")**

![image](https://user-images.githubusercontent.com/32914505/216782608-f1294fbf-6ace-412a-a24f-81327d3374a8.png)

- **"version"**: It refers to the technique used to calculate the similarity score to obtain such results. In the article, they are presented as HT (_categoric_tfidf_we_), TT (_categoric_tfidf_), and WET (_categoric_we_).
- **"feedback"**: Feedback metric.
- **"precision"**: Precision metric.
- **"likelihood"**: Likelihood metric.
- **"query"**: It refers to which Bug Report served as the input for the obtained result.
- **"recommendations"**: It refers to the ordered list of recommendations obtained from inserting the Bug Report from the _query_ field as input. It contains the fields **"bg_number"** (Bug Report ID), **"score"** (similarity score), and **"relevant"** (whether that Bug Report was deemed relevant or not, considering the proposed oracle).
