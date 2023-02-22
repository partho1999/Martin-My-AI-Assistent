import numpy as np # pip install numpy
import nltk #pip install nltk
from nltk.stem.porter import PorterStemmer
#nltk.download('punkt')

stemmer = PorterStemmer()


def tokenize(sentence):
   return nltk.word_tokenize(sentence)


def stem(word):
   return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentance,words):
   sentence_word = [stem(word) for word in tokenized_sentance]
   bag = np.zeros(len(words),dtype=np.float32)

   for idx, w in enumerate(words):
      if w in sentence_word:
         bag[idx] = 1
        
   return bag

#tokenize("hello jarvis")