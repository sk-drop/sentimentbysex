# WHAT ARE WE DOING HERE?
# - topic modelling and sentiment analysis
# 1 imports and preparation
# 2 create pipeline
# 3 process data


# 1 imports
import numpy as np
import pandas as pd

import spacy
from spacy.lang.en import English
from spacytextblob.spacytextblob import SpacyTextBlob
from spacy.lang.en.stop_words import STOP_WORDS

# load dataset
df = pd.read_csv("./data/new2021v2.csv")

# adding new columns for subjectivity, sentiment and topics
df["subjectivity"] = pd.Series()
df["sentiment"] = pd.Series()
df["cleanText"] = pd.Series()

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()

#  "nlp" Object is used to create documents with linguistic annotations.
for index, row in df.iterrows():
    doc = nlp(row["text"])
    print(row["text"])

# Create list of word tokens
    token_list = []
    for token in doc:
        token_list.append(token.text)

# Create list of word tokens after removing stopwords
    filtered_sentence =[] 

    for word in token_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False:
            filtered_sentence.append(word) 

    print(filtered_sentence)
    df.loc[index,"cleanText"] = " ".join(filtered_sentence)


# does not work with other pipes --> handle stopwords removal beforehand
nlp.add_pipe('spacytextblob')

# 3 process data
# getting polarity and subjectivity of text

for index, row in df.iterrows():
    doc = nlp(row["cleanText"])
    df.loc[index,"subjectivity"] = doc._.subjectivity
    df.loc[index,"sentiment"] = doc._.polarity
    print(index,doc._.subjectivity, doc._.polarity)

# saving df
df.to_csv("./data/new2021v3.csv")

'''
# adding stopwords removal to pipe
nlp.add_pipe('remove_stopwords', last=True)

# getting topics present in text

doc_list = []
# Iterates through each article in the corpus and adds it to processed list
for doc in data:
    pr = nlp(doc)
    doc_list.append(pr)

# Creates, which is a mapping of word IDs to words.
words = corpora.Dictionary(doc_list)

# Turns each document into a bag of words.
corpus = [words.doc2bow(doc) for doc in doc_list]

lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=words,
                                           num_topics=10, 
                                           random_state=2,
                                           update_every=1,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)


topics = lda_model.get_topic_terms(1)
for key, value in topics:
    word = words[key]
    print(word)
'''
