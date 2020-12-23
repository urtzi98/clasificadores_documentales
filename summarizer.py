#!/usr/bin/python
# -*- coding: utf-8 -*-
from parser import Parser


class Summarizer:
    def __init__(self):
        self.parser = Parser()

    def summarize(self, text):
        (keywords, wordCount) = self.parser.getKeywords(text)

        topKeywords = self.getTopKeywords(keywords[:60], wordCount)
        return topKeywords

    def getTopKeywords(self, keywords, wordCount):
        # Add getting top keywords in the database here
        for keyword in keywords:
            articleScore = 1.0 * keyword['count'] / wordCount
            keyword['totalScore'] = articleScore * 1.5

        return keywords