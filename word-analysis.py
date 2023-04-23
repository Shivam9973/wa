import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk import sent_tokenize,word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
text = "the weather is nice. My name is shubham. How are you. where do you stay."
#tokenizng sentence using sent_tokenize
print("sentence tokenizing",sent_tokenize(text))
print("-------------------------------------------------------")
#tokenizng words using word_tokenize
print("words tokenizing :",word_tokenize(text))
wr=word_tokenize(text)
#calculating the frequency of the words
fdist = FreqDist(wr)
print("Frequency:",fdist)
print(fdist.most_common(3))
#plotting graph of frequency of words
fdist.plot(19,cumulative=False)
plt.show()
#calling stop words function
stop_words = set(stopwords.words("english"))

print(stop_words)
#filtering the stop words
filtered_sent=[]
for w in wr:
    if w not in stop_words:
        filtered_sent.append(w)
        print("tokenized word :",wr)
print("filterd word: ", filtered_sent)