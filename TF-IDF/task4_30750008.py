"""
This function is finding most suitable document for a given term(word)
"""
import pandas as pd


def choice(term, documents):

    # finding IDF of given term(word)
    idf = documents.get_IDF(term)

    # creating a new DataFrame of the term which contain TF-IDF instead of frequencies
    tf_idf_df = documents.data[term]*idf

    # finding the maximum value is the new Data Frame
    max_v = tf_idf_df.max()

    # finding the row name(book name) corresponding to the highest value
    book_choice = tf_idf_df[tf_idf_df == max_v].index[0]

    return book_choice
