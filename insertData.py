import re
from firstHandle import *
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))


def readData(fileName, docID, db):
    results = dict()
    try:
        with open(fileName, "r") as f:
            for line in f:
                if line.rstrip():  # remove all blank line under the text
                    newLine = re.sub("[\s+\.\!\/_,$%^*(+\"\'\]+|\[+——！，。？、~@#￥%……&*()]+", " ", line)
                    newLine = newLine.rstrip().split()
                    results = readEachWords(newLine, results)
        insert(results, docID, db)

    finally:
        f.close()


def readEachWords(newLine, results):
    for eachWord in newLine:
        if eachWord not in results:
            if isStop(eachWord):
                if stemmWords(eachWord) != eachWord:
                    value = [1, "STOP", "STEMMED"]
                    results[eachWord] = value  # if the word is stopword and stemmed word, dict = {word:[1,"STOP","STEMMED"]}
                else:
                    value = [1, "STOP", "NULL"]
                    results[eachWord] = value

            else:
                if stemmWords(eachWord) != eachWord:
                    value = [1, "NULL", "STEMMED"]
                    results[eachWord] = value
                else:
                    value = [1, "NULL", "NULL"]
                    results[eachWord] = value
        else:
            results[eachWord][0] += 1

    return results


def insert(insertList, docID, db):
    cursor = db.cursor()
    for eachWord in insertList:
        try:
            sql = "INSERT INTO wordsCalculator(document_id,word,stoptype,word2vec,no_of_occurences," \
                  "stemmed_word) VALUES (%s, %s, %s, %s, %s, %s) "
            value = (docID, eachWord, insertList[eachWord][1], 0.0, insertList[eachWord][0], insertList[eachWord][2])
            cursor.execute(sql, value)
            db.commit()
        except:
            db.rollback()
