from conn import *


if __name__ == "__main__":
    db = connSQL()
    cursor = db.cursor()
    cursor.execute("select * from wordsCalculator")
    results = cursor.fetchall()
    for row in results:
        document_id=row[0]
        word=row[1]
        stoptype=row[2]
        word2vec=row[3]
        no_of_occurences=row[4]
        stemmed_word=row[5]
        print ("document_id=%s,word=%s,stoptype=%s,word2vec=%s,no_of_occurences=%s, stemmed_word =%s" % \
               (document_id, word, stoptype,word2vec,no_of_occurences, stemmed_word))