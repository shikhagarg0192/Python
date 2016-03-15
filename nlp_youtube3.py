import nltk
import random
from nltk.corpus import movie_reviews

#list of tuples of words which will be used as  features to train the data
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print(documents[1])

#gather all the words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
# it is a list
#convert to freq distribution of all words

all_words = nltk.FreqDist(all_words)
#print all_words.most_common(15)
#print all_words["stupid"]

word_features = list(all_words.keys())[:3000]

def find_features(documents):
    words = set(documents)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

print find_features(movie_reviews.words('neg/cv000_29416.txt'))

#featuresets = []
