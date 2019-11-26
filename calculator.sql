Drop database if exists Calculator;
create database Calculator DEFAULT CHARACTER SET utf8;
use Calculator;
CREATE TABLE wordsCalculator(
	document_id int(10) NOT NULL,
    word varChar(50) NOT NULL,
    stoptype varChar(50),
    word2vec float(50),
    no_of_occurences int(50),
    stemmed_word varChar(50),
    primary key(document_id,word)
);

