import re


class PreProcess:

    def __init__(self):
        pass

    def clean_sentence(self, string):
        """
        clean_sentence method takes all letters to small letters, remove multiple spaces and remove all special characters from doc.
        :param string:
        :return:
        """
        cleaned_str = re.sub('[^a-z\s]+', '', string, flags=re.IGNORECASE)
        cleaned_str = re.sub('(\s+)', ' ', cleaned_str)  # multiple spaces are replaced by single space
        cleaned_str = cleaned_str.lower()  # converting the cleaned string to lower case
        return cleaned_str

    def pre_process(self, corpus):
        """
        pre-process methos is used to clean the documents with the help of a util method clean_sentence()
        :param corpus: The document to be cleaned
        :return: returns cleaned document with every later converted to small letters, multiple spaces deleted and special characters are dropped.
        """
        cleaned_cor = [self.clean_sentence(sentence) for sentence in corpus]
        return cleaned_cor
