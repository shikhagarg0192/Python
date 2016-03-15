#tokenizers
#corpora - body of text, e.g : speeches, medical journals
#lexicon - words and their meanings

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello there, how are you doing today? The weather is great and python is awesome too"
print(sent_tokenize(example_text))
print(word_tokenize(example_text))
for i in word_tokenize(example_text):
    print i

#stop words : not needed, a, an, the, be

from nltk.corpus import stopwords

ex_sent = "This is an example of showing off stop word filteration."
stop_words = set(stopwords.words("english"))
print(stop_words)

words = word_tokenize(ex_sent)
#filter_sent = []
#for w in words:
#    if w not in stop_words:
#        filter_sent.append(w)
#           or
filter_sent = [w for w in words if w not in stop_words]

print filter_sent

#stemming : Data preprocessing step
#riding : affix ride so, it removes affixes
#porter algo

from nltk.stem import PorterStemmer

ps = PorterStemmer()
ex_words = ["python", "pythoner", "pythoning", "pythonly"]

for w in ex_words:
    print ps.stem(w)

new_t = "it is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"

words = word_tokenize(new_t)

for w in words:
    print ps.stem(w)


#speech tagging
#tags each word in a sentence with the part of speech for that word. labels words
#as noun, adjective etc.

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_t = state_union.raw("2005-GWBush.txt")
sample_t = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer =  PunktSentenceTokenizer(train_t)

tokenized = custom_sent_tokenizer.tokenize(sample_t)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #named entities
            namedEnt = nltk.ne_chunk(tagged, binary=False)
           # namedEnt.draw()

            #print tagged
    except Exception as e:
        print str(e)

#process_content()

#chunking : grouping various words together by their speech tags
#def process_content_chunking():
 #   try:
  #      for i in tokenized:
   #         words = nltk.word_tokenize(i)
    #        tagged = nltk.pos_tag(words)
          # chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP.>*<NN>*}
          #                             }<VB.?|IN|DT>+{""" #one or more adverb
          # chunkParser = nltk.RegexpParser(chunkGram)
          # chunked = chunkParser.parse(tagged)
          # chunked.draw()
          # print chunked
            
#            print tagged
    #except Exception as e:
     #   print str(e)

#process_content_chunking()

#chinking : to be removed from chunk. }chink{

#named entity recognition

#Lemmatizers

from nltk.stem import WordNetLemmatizer
lemmat = WordNetLemmatizer()
print lemmat.lemmatize("cats")
print lemmat.lemmatize("cacti")
print lemmat.lemmatize("pirat")
print lemmat.lemmatize("yogas")
print lemmat.lemmatize("limits")
print lemmat.lemmatize("catetr")

print lemmat.lemmatize("better", pos="n") #a for adjective
#v for verb

#NLTK corpora
#body of texts
#corpora are grouped by some sort of defining characteristic


from nltk.corpus import gutenberg

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)
print tok[5:15]






#to know nltk location
print(nltk.__file__)



