"""
Class "WordCount" can analyse the number of occurrences for each word from a given cleaned text. This class have a
instance variable called word_counts which is a Python Dictionary
"""


class WordAnalyser:

    def __init__(self):
        self.word_counts = {}
        self.word_list = []
        self.word_count_list = []

    # This method performs a count on a given book text at word level. It accept the cleaned book text as the argument,
    # and count the occurrence for each of the words and stores it into word_counts dictionary
    def analyse_words(self, c_book):

        # creating a list of words
        b_word_list = c_book.split()

        # removing redundant words
        word_set = set(b_word_list)

        # creating new list with removed redundant words
        self.word_list = list(word_set)

        n = len(self.word_list)
        self.word_count_list = [0] * n

        # counting total number of occurrence of words, one by one
        for word in b_word_list:
            self.word_count_list[self.word_list.index(word)] += 1

        # converting lists into dictionary
        zipped_counts = zip(self.word_list, self.word_count_list)
        self.word_counts = dict(list(zipped_counts))

    # this method returns the frequency of the words found in word_counts dictionary
    def get_word_frequency(self):

        n = len(self.word_list)

        # finding total number of words in the book
        total_count = 0
        for i in range(n):
            total_count = total_count + int(self.word_count_list[i])

        # finding frequency of words and storing it in list, one by one
        word_freq_list = []
        for i in range(n):
            word_freq_list.append(self.word_count_list[i]/total_count)

        # creating dictionary of word's frequency
        zipped_f = zip(self.word_list, word_freq_list)
        freq_count = dict(list(zipped_f))

        return freq_count

    # this method present the number of occurrence for each word in a readable format
    def __str__(self):

        n = len(self.word_list)
        r_output = ""

        # creating a string to present word counts in a readable format
        for i in range(n):
            r_output = r_output + str(self.word_list[i]) + ":" + str(self.word_count_list[i]) + "\n"

        return r_output
