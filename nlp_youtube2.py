from nltk.corpus import wordnet
#synonym set
syns = wordnet.synsets("program")
#synset
print syns[0]
#just the word
print syns[0].lemmas()[0].name()
#definition
print syns[0].definition()
#examples
print "\n"
print syns[0].examples()

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        print("l : ",l)
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print set(synonyms)
print "\n"
print set(antonyms)

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")


w1 = wordnet.synset("motor.n.01")
w2 = wordnet.synset("car.n.01")


print(w1.wup_similarity(w2)) #percentage of similarity between w1 and w2
