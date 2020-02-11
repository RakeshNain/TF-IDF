"""
Class "Cleaning" can perform the basic pre-processing on each input text. This class have one instance variable that is
a string which holds the text of the book. This string will change depending on whether clean() or read_text() has been
called.
Majorly in this task we are cleaning a book by removing undesirable characters from it.
"""


class Preprocessor:

    def __init__(self):
        self.book_content = ""

    # This method removes undesirable characters from text present in book_content and stores it back in book content
    def clean(self):

        # If no text has been read into this variable then it will return int 1 else it will do cleaning and return None
        if self.book_content == "":
            return 1

        else:
            text_list = []

            # filling data into list(text_list), character by character present in book_content string
            for text in self.book_content:
                text_list.append(text.lower())

            # finding length of string
            text_list_len = len(text_list)

            # running a for loop to remove undesirable characters present in list and replacing some characters
            for i in range(text_list_len):

                # checking that character is ASCII character or not and if it is not a ASCII character than replacing it
                # with empty string and if it is a ASCII character then checking further
                if ord(text_list[i]) < 128:

                    # checking that character is a alphabet or number. If it is not a alphabet or number then checking
                    # further
                    if not text_list[i].isalnum():

                        # checking that character is a white space or not. If it is not a white space then checking
                        # further
                        if not text_list[i].isspace():

                            # checking that character is "-" or "_". If it is one of them then replacing it with a white
                            # space else replacing character with empty string
                            if text_list[i] == "-" or text_list[i] == "_":
                                text_list[i] = " "
                            else:
                                text_list[i] = ""
                else:
                    text_list[i] = ""

            # assigning book_content a new cleaned string from a list(text_list)
            self.book_content = ''.join(text_list)

    # method to present content of book_content
    def __str__(self):
        return self.book_content

    # this method accepts a string argument that is a name of a file in current directory and then reading the content
    # of the file into book_content
    def read_text(self, text_name):
        book = open(text_name, "r", encoding="utf8")
        self.book_content = book.read()
        book.close()
