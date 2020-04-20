from time import time

import numpy as np
import re

class CountVectorizer:

    def fit(self, corpus):
        self.vocabulary = {}
        print('fit started...')
        for sentence in corpus:
            for word in sentence.split(" "):
                if word not in self.vocabulary.keys():
                    self.vocabulary[word] = 1
                else:
                    self.vocabulary[word] += 1
        self.vocabulary_count = len(self.vocabulary)  # this approach was used to avoid re-computing the valuse

        self.sorted_vocabulary_keys = list(sorted(self.vocabulary))
        print('fit completed...')

    def test(self):
        v = {}
        params = self.get_feature_params()
        for word in params:
            v[word] = params.index(word)
        return v

    def get_feature_params(self):
        return self.sorted_vocabulary_keys

    def get_vocabulary_keys(self):
        return self.vocabulary.keys()

    def vocabulary_(self):
        return self.vocabulary

    def get_vocabulary_count(self):
        return self.vocabulary_count

    # def fit_transform(self, samples):
    #     print('fit_transform started...')
    #     word_track = {}  # helps reduce time complexity
    #     sparse_matrix = np.zeros((len(samples), self.get_vocabulary_count()))
    #
    #     for index in range(len(samples)):
    #         for word in samples[index].split(' '):
    #             if word in word_track.keys():
    #                 sparse_matrix[index, word_track[word]] += 1
    #             else:
    #                 if word in self.get_vocabulary_keys():
    #                     sparse_matrix[index, self.get_feature_params().index(word)] += 1
    #                     word_track[word] = self.get_feature_params().index(word)
    #     print('fit_transform completed...')
    #     return sparse_matrix

    def fit_transform2(self, corpus):
        st = time()
        print('fit_transform started...')
        word_track = {}
        params = self.test()
        sparse_matrix = np.zeros((len(corpus), len(params)))
        for idx in range(len(corpus)):
            for word in corpus[idx].split():
                if word in word_track.keys():
                    sparse_matrix[idx, params[word]] += 1
                elif word in params:
                    sparse_matrix[idx, params[word]] += 1
                    word_track[word] = idx
        et = time()
        print(et - st)
        print('fit_transform completed...')
        return sparse_matrix

    def fit_transform(self, samples):
        st = time()
        print('fit_transform started...')
        word_track = {}  # helps reduce time complexity
        params = self.get_feature_params()
        sparse_matrix = np.zeros((len(samples), len(params)))

        l = len(samples)
        for idx in range(l):
            for word in samples[idx].split():
                if word in word_track.keys():
                    sparse_matrix[idx, word_track[word]] += 1
                else:
                    if word in params:
                        sparse_matrix[idx, params.index(word)] += 1
                        word_track[word] = params.index(word)
        et = time()
        print(et - st)
        print('fit_transform completed...')
        return sparse_matrix
