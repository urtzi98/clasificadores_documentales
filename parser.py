# !/usr/bin/python
# -*- coding: utf-8 -*-
import nltk
import nltk.data
import os


class Parser:
    def __init__(self):
        self.ideal = 20.0

    def getKeywords(self, text):
        text = self.removePunctations(text)
        words = self.splitWords(text)
        # Eliminamos stopwords del castellano
        words = [word for word in words if word not in nltk.corpus.stopwords.words('spanish')]
        # Ahora solo cogemos las que no se repiten
        unique_words = list(set(words))
        key_words = [{'word': word, 'count': words.count(word)} for word in unique_words]
        key_words = keywords = sorted(key_words, key=lambda x: -x['count'])

        return (keywords, len(words))

    def splitWords(self, sentence):
        return nltk.word_tokenize(sentence.lower())

    def removePunctations(self, text):
        return ''.join(t for t in text if t.isalnum() or t == ' ')

    def removeStopWords(self, words):
        return [word for word in words if word not in nltk.corpus.stopwords.words('spanish')]
