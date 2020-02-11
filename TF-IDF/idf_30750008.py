"""
Class IDFAnalyser is mainly for calculation of Inverse Document Frequency(IDF) of a word other than this it is also
create a DataFrame who's rows represents the frequency of single cleaned text. Each column corresponds to a word
"""
import math
import pandas as pd


class IDFAnalyser:

    def __init__(self):
        self.data = pd.DataFrame()
        self.key_list = []
        self.value = []

    # this method loads the frequency of a cleaned text into data frame with a title that corresponds to the text the
    # frequency was generated from
    def load_frequency(self, book_frequency, book_title):
        temp_data = pd.DataFrame(book_frequency, index=[book_title])
        self.data = pd.concat([temp_data, self.data], sort=False)

    # this method finds the IDF for the term(word) provided and the documents loaded into data
    def get_IDF(self, term):

        # finding the total number of documents(books) in the data frame
        d = len(self.data)

        # finding the total number of documents(books) contains the term(word)
        n = self.data[term].count()

        # calculating IDF
        idf = 1 + math.log(d / (1 + n))

        return idf
