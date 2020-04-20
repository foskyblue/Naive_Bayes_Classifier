import numpy as np


class NaiveBayes:

    def __init__(self):
        pass

    def fit(self, X, y, smoothing):
        print('------------------------------------Training Started------------------------------------')
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        self.score_ci = np.zeros(self._classes)
        self.word_conditional_prob = {}  # np.zeros(n_classes)

        # initialize prior
        self._priors = np.zeros(len(self._classes), dtype=np.float64)

        # for each word, compute their frequencies and probabilities for each class (class ham
        # and class spam)
        for c in self._classes:
            self.word_conditional_prob[c] = np.zeros(n_features)
            X_c = X[c == y]  # get all rows where the label is same as class c
            self._priors[c] = X_c.shape[0] / float(n_samples)  # probability of each class
            self.word_conditional_prob[c] = (np.sum(X_c, axis=0) + smoothing) / np.sum(X_c)  # conditional probability for each word in the vocabulary
        print('------------------------------------Training Completed------------------------------------')

    def predict(self, X):
        print('------------------------------------Prediction Started------------------------------------')
        predicted_classes = [self.predict_(x) for x in X]
        print('------------------------------------Prediction Completed------------------------------------')
        return predicted_classes

    def predict_(self, x):
        posteriors = []
        for c in self._classes:
            prior = np.log(self._priors[c])
            word_conditional_prob = self.word_conditional_prob[c]
            class_conditional_probs = self.conditional_prob(x, word_conditional_prob)
            posteriors.append(prior + class_conditional_probs)
        return self._classes[np.argmax(posteriors)]  # return class with maximum posterior (0/1)

    def conditional_prob(self, x, word_conditional_prob):
        product = np.multiply(x, word_conditional_prob)
        return np.sum(np.log(product[product > 0]))  # return the sum of log of numbers greater than 0
