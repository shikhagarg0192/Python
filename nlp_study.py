import nltk
text = "to be or not to be"
print set(text)
print len(text)
print (len(set(text))*100//len(text))
print (text.count("to")*100//len(text))
