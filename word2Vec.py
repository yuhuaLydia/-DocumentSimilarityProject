import numpy as np
import gensim
from scipy import spatial
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec

def avg_feature_vector(sentence, model, num_features, index2word_set):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec


path = get_tmpfile("word2vec.model")

#model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)
model = gensim.models.KeyedVectors.load("word2vec.model")
#model.save("word2vec.model")
index2word_set = set(model.wv.index2word)

with open('./txtfiles/testfile1.txt', 'r') as file:
    s1 = file.read().replace('\n', '')

with open('./txtfiles/testfile2.txt', 'r') as file:
    s2 = file.read().replace('\n', '')

s1_afv = avg_feature_vector(s1, model=model, num_features=300, index2word_set=index2word_set)
s2_afv = avg_feature_vector(s2, model=model, num_features=300, index2word_set=index2word_set)

#print(s1_afv)
#print(s2_afv)

sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
print(sim)
