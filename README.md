# -DocumentSimilarityProject

#Mysql 连接步骤：https://www.runoob.com/python3/python3-mysql.html

#StopWords 处理：    https://tobiaslee.top/2017/11/17/Sentence-preprocessing-skills/
                    https://www.geeksforgeeks.org/removing-stop-words-nltk-python/



# 11.26 Completed Stemmword Part
1. enter the Mysql and check the conn.py 是否连接成功
2. 把calculator.sql copy到mysql中运行
3. 直接run main.py  //应该能用

现在可以看到数据库中stemmword和stoptype 已经有了变化

# 12.6 Update - Word2Vec.py Added
First, install all the following dependent modules using pip3:
numpy
gensim
scipy
spatial

In command line, run

$ python3 word2Vec.py

The similarity of testfile1 and testfile2 should be printed.

You can change testfile1/testfile2 under './txtfiles' to see different results. 