import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer=PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    pass

'''a="How are you feeling today?"
print(a)
a=tokenize(a)
print(a)'''

'''words=["Organize","organizing","organizer"]
print(words)
a=[stem(w) for w in words]
print(a)'''