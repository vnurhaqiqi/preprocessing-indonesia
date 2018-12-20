import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

corpus = "Sistem Informasi (SI) adalah kombinasi dari teknologi informasi dan aktivitas orang yang menggunakan teknologi itu untuk mendukung operasi dan manajemen. " \
         "Dalam arti yang sangat luas, istilah sistem informasi yang sering digunakan merujuk kepada interaksi antara orang, proses algoritmik, data, dan teknologi. " \
         "Dalam pengertian ini, istilah ini digunakan untuk merujuk tidak hanya pada penggunaan organisasi teknologi informasi dan komunikasi (TIK), tetapi juga untuk cara di mana orang berinteraksi dengan teknologi ini dalam mendukung proses bisnis."

# proses tokenizing kalimat dan mengkonversi kalimat menjadi huruf kecil
sentences = sent_tokenize(corpus.lower())

# proses menghilangkan karakter spesial
spe = []
for i in sentences:
    spe.append(re.sub(r'-(?:(?<!\b[0-9]{4}-)|(?![0-9]{2}(?:[0-9]{2})?\b))', ' ', i))
removetable = str.maketrans('', '', '@#%()[]{}.,!?><:;*&^+=_`~$"|/')
clean_sent = [s.translate(removetable) for s in spe]

# proses filtering (menghilangkan stopword) bahasa indonesia
stopwords_id = set(stopwords.words('indonesian'))
sent_stopwords = []
for sent in clean_sent:
    sent_stopwords.append(' '.join(w for w in nltk.word_tokenize(sent) if w.lower() not in stopwords_id))

# proses stemming bahasa indonesia
factory = StemmerFactory()
stemmer = factory.create_stemmer()

stemming = []
for sent in sent_stopwords:
    stemming.append(stemmer.stem(sent))

print(stemming)