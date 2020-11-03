import numpy as np
from rbo import rbo
from scipy.spatial import distance
from itertools import combinations
from word_embeddings_rbo import word_embeddings_rbo


def proportion_unique_words(topics, topk=10):
    """
    compute the proportion of unique words

    Parameters
    ----------
    topics: a list of lists of words
    topk: top k words on which the topic diversity will be computed
    """
    if topk > len(topics[0]):
        raise Exception('Words in topics are less than '+str(topk))
    else:
        unique_words = set()
        for topic in topics:
            unique_words = unique_words.union(set(topic[:topk]))
        puw = len(unique_words) / (topk * len(topics))
        return puw


def irbo(topics, weight=0.9, topk=10):
    """
    compute the inverted rank-biased overlap

    Parameters
    ----------
    topics: a list of lists of words
    weight: p (float), default 1.0: Weight of each
        agreement at depth d:p**(d-1). When set
        to 1.0, there is no weight, the rbo returns
        to average overlap.
    topk: top k words on which the topic diversity
          will be computed

    Returns
    -------
    irbo : score of the rank biased overlap over the topics
    """
    if topk > len(topics[0]):
        raise Exception('Words in topics are less than topk')
    else:
        collect = []
        for list1, list2 in combinations(topics, 2):
            word2index = get_word2index(list1, list2)
            indexed_list1 = [word2index[word] for word in list1]
            indexed_list2 = [word2index[word] for word in list2]
            rbo_val = rbo(indexed_list1[:topk], indexed_list2[:topk], p=weight)[2]
            collect.append(rbo_val)
        return 1 - np.mean(collect)


def word_embedding_irbo(topics, word_embedding_model, weight=0.9, topk=10):
    '''
    compute the word embedding-based inverted rank-biased overlap

    Parameters
    ----------
    topics: a list of lists of words
    weight: p (float), default 1.0: Weight of each agreement at depth d:
    p**(d-1). When set to 1.0, there is no weight, the rbo returns to average overlap.
    
    Returns
    -------
    weirbo: word embedding-based inverted rank_biased_overlap over the topics
    '''
    if topk > len(topics[0]):
        raise Exception('Words in topics are less than topk')
    else:
        collect = []
        for list1, list2 in combinations(topics, 2):
            word2index = get_word2index(list1, list2)
            index2word = {v: k for k, v in word2index.items()}
            indexed_list1 = [word2index[word] for word in list1]
            indexed_list2 = [word2index[word] for word in list2]
            rbo_val = word_embeddings_rbo(indexed_list1[:topk], indexed_list2[:topk], p=weight,
                                          index2word=index2word, word2vec=word_embedding_model)[2]
            collect.append(rbo_val)
        return 1 - np.mean(collect)


def pairwise_jaccard_diversity(topics, topk=10):
    '''
    compute the average pairwise jaccard distance between the topics 
  
    Parameters
    ----------
    topics: a list of lists of words
    topk: top k words on which the topic diversity
          will be computed
    
    Returns
    -------
    pjd: average pairwise jaccard distance
    '''
    dist = 0
    count = 0
    for list1, list2 in combinations(topics, 2):
        js = 1 - len(set(list1).intersection(set(list2)))/len(set(list1).union(set(list2)))
        dist = dist + js
        count = count + 1
    return dist/count


def pairwise_word_embedding_distance(topics, word_embedding_model, topk=10):
    """
    :param topk: how many most likely words to consider in the evaluation
    :return: topic coherence computed on the word embeddings similarities
    """
    if topk > len(topics[0]):
        raise Exception('Words in topics are less than topk')
    else:
        count = 0
        sum_dist = 0
        for list1, list2 in combinations(topics, 2):
            count = count+1
            word_counts = 0
            dist = 0
            for word1 in list1[:topk]:
                for word2 in list2[:topk]:
                    dist = dist + distance.cosine(word_embedding_model.wv[word1], word_embedding_model.wv[word2])
                    word_counts = word_counts + 1

            dist = dist/word_counts
            sum_dist = sum_dist + dist
        return sum_dist/count


def centroid_distance(topics, word_embedding_model, topk=10):
    """
    :param topk: how many most likely words to consider in the evaluation
    :return: topic coherence computed on the word embeddings similarities
    """
    if topk > len(topics[0]):
        raise Exception('Words in topics are less than topk')
    else:
        count = 0
        for list1, list2 in combinations(topics, 2):
            count = count + 1
            centroid1 = np.zeros(word_embedding_model.vector_size)
            centroid2 = np.zeros(word_embedding_model.vector_size)
            for word1 in list1[:topk]:
                centroid1 = centroid1 + word_embedding_model[word1]
            for word2 in list2[:topk]:
                centroid2 = centroid2 + word_embedding_model[word2]
            centroid1 = centroid1 / len(list1[:topk])
            centroid2 = centroid2 / len(list2[:topk])
        return distance.cosine(centroid1, centroid2)


def get_word2index(list1, list2):
    words = set(list1)
    words = words.union(set(list2))
    word2index = {w: i for i, w in enumerate(words)}
    return word2index
