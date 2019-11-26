from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))

def isStop(word):
    if word not in stopwords:
        return 0
    else:
        return 1
