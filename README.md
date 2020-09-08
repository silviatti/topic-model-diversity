# A collection of Topic Diversity measures for topic modeling.
Here I collected and implemented most of the known topic diversity measures used for measuring how different topics are.
The more diverse the resulting topics are, the higher will be the coverage of the various aspects of the analyzed corpus. It is therefore important to also obtain topics that are different from each other (rather than just considering how much coherent the topics are).

## List of the currently implemented metrics:
* Proportion of unique words (PUW) [[Dieng et al., 2020](#puw)]
* average Pairwise Jaccard Distance (JD) [[Tran et al., 2013](#jd)]
* Inverted Rank-Biased Overlap (IRBO) [[Bianchi et al., 2020a]](#irbo)
* Word Embedding-based Centroid Distance (WE-CD) [[Bianchi et al., 2020b]](#cd)
* Word Embedding-based Pairwise Distance (WE-PD)
* Word Embedding-based Inverted Rank-Biased Overlap (WE-IRBO)

### How to use:
The necessary input for all the metrics is a list of topics, i.e. a list of list of strings. For example: 
```python
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
```
You can also specify the parameter `topk` which represents the number of words considered for each list. Note that `topk` must be less or equal than the length of the a topic list.  

#### Proportion of Unique Words:
```python 
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
proportion_unique_words(topics, topk=3)

Out[1]: 1.0
```

#### Pairwise Jaccard Diversity:
```python 
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
pairwise_jaccard_diversity(topics, topk=3)

Out[1]: 1.0
```
#### Word Embedding-based Centroid Distance
This metric requires a word embedding space as input to compute distances (parameter `word_embedding_model`). 
```python
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
pairwise_word_embedding_distance(topics, wv, topk=3)

Out[1]: 0.6379696850836505
```
### Word Embedding-based Pairwise Distance
This metric requires a word embedding space as input to compute distances (parameter `word_embedding_model`). 
```python
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
centroid_distance(topics, wv, topk=3)

Out[1]: 0.8380562411966147
```
#### Inverted Rank-Biased Overlap
```python
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
print("irbo p=0.5:",irbo(topics, weight=0.5, topk=3))

Out[1]: 1.0
```
#### Word Embedding-based Rank-Biased Overlap
This metric requires a word embedding space as input to compute distances (parameter `word_embedding_model`). 
```python
topics = [['cat', 'animal', 'dog'], ['building', 'bank', 'house'], ['nature', 'wilderness', 'lake']]
word_embedding_irbo(topics,wv, weight=0.9, topk=3)

Out[1]: 0.8225350005800525
```

## References:
<h5 id="puw">Adji Bousso Dieng, Francisco J. R. Ruiz, and David M.Blei. 2020. Topic modeling in embedding spaces.Trans. Assoc. Comput. Linguistics, 8:439–453. </h5>
<h5 id="jd">Nam Khanh Tran, Sergej Zerr, Kerstin Bischoff, Claudia Niederée, Ralf Krestel: Topic Cropping: Leveraging Latent Topics for the Analysis of Small Corpora. TPDL 2013: 297-308</h5>
<h5 id="irbo"> Federico Bianchi, Silvia Terragni, Dirk Hovy: Pre-training is a Hot Topic: Contextualized Document Embeddings Improve Topic Coherence. Preprint (2020a) </h5>
<h5 id="cd"> 	Federico Bianchi, Silvia Terragni, Dirk Hovy, Debora Nozza, Elisabetta Fersini: Cross-lingual Contextualized Topic Models with Zero-shot Learning. Preprint (2020b)
</h5>
