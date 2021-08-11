from gensim.models.fasttext import FastText
from gensim.test.utils import get_tmpfile
import nltk
from nltk.stem import WordNetLemmatizer
import re
import numpy as np
from sklearn.decomposition import PCA
import pickle
import pandas as pd
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
stemmer = WordNetLemmatizer()    

def pre_processing_text(doc):
    doc = re.sub(r'\W', ' ', str(doc))
    doc = re.sub(r'\s+[a-zA-Z]\s+', ' ', str(doc))
    doc = re.sub(r'\^[a-zA-Z]\s+', ' ', str(doc))
    doc = re.sub(r'\s+', ' ', str(doc), flags=re.I)
    doc = re.sub(r'^b\s+', '', str(doc))
    doc = doc.lower()
    tokens = doc.split()
    token = [stemmer.lemmatize(word=word) for word in tokens]
    token = [word for word in token if word not in en_stop]
    token = [word for word in token if len(word)>3]

    preprocess_text = ' '.join(tokens)
    return preprocess_text

ai = []
with open('datasets/train.txt', 'r',encoding="utf-8") as f: 
    for ln in f.readlines():
        ai.append(ln[23:])
final_corpus = [pre_processing_text(sent) for sent in ai if sent.strip()!='']

word_dict = pd.DataFrame(columns=['num_words','word_indices'])
wrd_id = []
for every in final_corpus:
    for eve in range(len(every)):
        wrd_id.append(eve)
    word_dict = word_dict.append({'word_indices':wrd_id,'num_words':len(wrd_id)},ignore_index=True)

with open('datasets/word_indices.pickle', 'wb') as handle:
    pickle.dump(word_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

punct_tok = nltk.WordPunctTokenizer()
tok_corpus = [punct_tok.tokenize(sent) for sent in final_corpus]
embedd_size = 60
window_size = 40
min_wrd = 5
down_sampling=1e-2
model = FastText(vector_size=embedd_size,window=window_size,min_count=min_wrd,sg=1)
model.build_vocab(tok_corpus)
total_words = model.corpus_total_words 
model.train(tok_corpus,total_words=total_words, epochs=100)
model.save('datasets/fastT.model')

fname = get_tmpfile("D:\\lakehead-sem-1\\nlp-5014\\nlp_project\\datasets\\fastT.model")
model = FastText.load(fname)

a_file = open('datasets/fastText.vec', 'w')
for i in final_corpus:
    for j in i.split():
        np.savetxt(a_file,model.wv[j])
f.close()
model.save("datasets/fastText.bin")