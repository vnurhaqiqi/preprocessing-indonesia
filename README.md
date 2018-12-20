# preprocessing-indonesia

Contoh preprocessing menggunakan bahasa Indonesia pada bahasa pemrograman Python.

## Tokenizing
Untuk proses tokenizing menggunakan nltk sebagai library yang digunakan, untuk penjelasan lebih lanjut mengenai nltk dapat dilihat [disini](http://www.nltk.org/)

### Contoh penerapan tokenizing dengan menggunakan nltk :

`from nltk.tokenize import sent_tokenize, word_tokenize`

`corpus = "Jurnal ilmiah adalah sebuah publikasi yang diterbitkan secara berkala oleh suatu organisasi profesi atau institusi akademik yang memuat artikel-artikel yang merupakan produk pemikiran ilmiah secara empiris (artikel hasil penelitian) maupun secara logis (artikel hasil pemikiran) dalam bidang ilmu tertentu."`

`sentences = sent_tokenize(corpus) # tokenizing per kalimat`

`words = word_tokenize(corpus) # tokenizing per kata`

## Filtering
Pada proses filtering masih menggunakan library yang sama yaitu nltk.

### Contoh penerapan filtering menggunakan nltk :
`from nltk.tokenize import sent_tokenize, word_tokenize`

`from nltk.corpus import stopwords`

`stopwords_id = set(stopwords.words('indonesian'))`

`corpus = "Jurnal ilmiah adalah sebuah publikasi yang diterbitkan secara berkala oleh suatu organisasi profesi atau institusi akademik yang memuat artikel-artikel yang merupakan produk pemikiran ilmiah secara empiris (artikel hasil penelitian) maupun secara logis (artikel hasil pemikiran) dalam bidang ilmu tertentu."`

`sents_rm_stopwords = []
for sent in corpus:
    sents_rm_stopwords.append(' '.join(w for w in nltk.word_tokenize(sent) if w.lower() not in stopwords_en))`

## Stemming
Pada proses stemming bahasa Indonesia menggunakan library khusus yang diciptakan untuk menangani kasus stemming bahasa Indonesia yaitu Sastrawi. Untuk mengetahui lebih jelas apa itu Sastrawi dapat dilihat [disini](https://github.com/sastrawi/sastrawi).

### Contoh penerapan stemming menggunakan Sastrawi
`from Sastrawi.Stemmer.StemmerFactory import StemmerFactory`

`factory = StemmerFactory()`

`stemmer = factory.create_stemmer()`

`corpus = "Tokenisasi sebenarnya bukan merupakan normalisasi yang dilakukan, melainkan hanya pembantu dalam proses preprocessing. Fungsi token dikasus ini adalah untuk memisah kata perkata pada text untuk diolah lebih jauh seperti melakukan spelling check dan lainnya."`

`stemming = stemmer.stem(stopwords)`
