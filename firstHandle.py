from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stopwords = set(stopwords.words('english'))

def isStop(word):
    if word not in stopwords:
        return 0
    else:
        return 1
def stemmWords(word):
    ps = PorterStemmer()
    return ps.stem(word)



