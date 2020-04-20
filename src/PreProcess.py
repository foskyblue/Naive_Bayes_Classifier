import re


class PreProcess:

    def __init__(self):
        pass

    def clean_sentence(self, string):
        cleaned_str = re.sub('[^a-z\s]+', '', string, flags=re.IGNORECASE)
        cleaned_str = re.sub('(\s+)', ' ', cleaned_str)  # multiple spaces are replaced by single space
        cleaned_str = cleaned_str.lower()  # converting the cleaned string to lower case
        return cleaned_str

    def pre_process(self, corpus):
        cleaned_cor = [self.clean_sentence(sentence) for sentence in corpus]
        return cleaned_cor
