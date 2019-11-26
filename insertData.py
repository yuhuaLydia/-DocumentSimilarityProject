import re
from firstHandle import *
import pymysql

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))


def readData(fileName, docID, db):
    results = dict()
    try:
        with open(fileName, "r") as f:
            for line in f:
                if line.rstrip():  # remove all blank line under the text
                    newLine = re.sub("[\s+\.\!\/_,$%^*(+\"\'\]+|\[+——！，。？、~@#￥%……&*()]+", " ", line)
                    newLine = newLine.rstrip().split()
                    for eachWord in newLine:
                        if eachWord not in results:
                            if isStop(eachWord):
                                value = [1, "STOP"]
                                results[eachWord] = value  # if the word is stopword, dict = {word:[1,"STOP"]}
                            else:
                                value = [1, "NULL"]
                                results[eachWord] = value

                        else:
                            results[eachWord][0] += 1
        insert(results, docID, db)

    finally:
        f.close()


def insert(insertList, docID, db):
    cursor = db.cursor()
    default = "NULL"
    for eachWord in insertList:
        try:
            sql = "INSERT INTO wordsCalculator(document_id,word,stoptype,word2vec,no_of_occurences," \
                  "stemmed_word) VALUES (%s, %s, %s, %s, %s, %s) "
            value = (docID, eachWord, insertList[eachWord][1], 0.0, insertList[eachWord][0], default)
            cursor.execute(sql, value)
            db.commit()
        except:
            db.rollback()
