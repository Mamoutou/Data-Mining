from nltk import sent_tokenize , word_tokenize
from nltk.corpus import stopwords

f = open('lyrics.txt','r',encoding="utf-8")

stop_words = set(stopwords.words("english"))
# print(stop_words)



for line in f:
    line = line.lower()
    words = word_tokenize(line)
    filtered_words = [w for w in words if w not in stop_words]
    # print(filtered_words)

# print(word_tokenize(f.read()))