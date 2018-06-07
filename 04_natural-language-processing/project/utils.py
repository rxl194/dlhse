import nltk
import pickle
import re
import numpy as np

nltk.download('stopwords')
from nltk.corpus import stopwords

# Paths for all resources for the bot.
RESOURCE_PATH = {
    'INTENT_RECOGNIZER': 'intent_recognizer.pkl',
    'TAG_CLASSIFIER': 'tag_classifier.pkl',
    'TFIDF_VECTORIZER': 'tfidf_vectorizer.pkl',
    'THREAD_EMBEDDINGS_FOLDER': 'thread_embeddings_by_tags',
    'WORD_EMBEDDINGS': 'data/GoogleNews-vectors-negative300.bin',
}

def text_prepare_list(text):
    """Performs tokenization and simple preprocessing."""
    
    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    intent = ' '.join([x for x in text.split() if x and x not in stopwords_set])
    text = [x.strip() for x in text.split() if x and x not in stopwords_set]
#    print (text)

    return intent.strip(), text

def text_prepare(text):
    """Performs tokenization and simple preprocessing."""
    
    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()

import gensim
from gensim.models import KeyedVectors

def load_embeddings(embeddings_path):
    """Loads pre-trained word embeddings from tsv file.

    Args:
      embeddings_path - path to the embeddings file.

    Returns:
      embeddings - dict mapping words to vectors;
      embeddings_dim - dimension of the vectors.
    """
    
    # Hint: you have already implemented a similar routine in the 3rd assignment.
    # Note that here you also need to know the dimension of the loaded embeddings.
    # When you load the embeddings, use numpy.float32 type as dtype

    ########################
    #### YOUR CODE HERE ####
    ########################
    #        pass 
#    embeddings = {}
#    for line in open(embeddings_path):
#        data = line.strip().split('\t')
#        embeddings[data[0]] = np.array(data[1:], dtype=np.float32)
#    embeddings_len = len(list(embeddings.values())[0])
    embeddings = KeyedVectors.load_word2vec_format(embeddings_path, binary=True) 
    len(embeddings.index2word) 
    return embeddings, embeddings.vector_size    



def question_to_vec(question, embeddings, dim):
    """Transforms a string to an embedding by averaging word embeddings."""
    
    # Hint: you have already implemented exactly this function in the 3rd assignment.

    ########################
    #### YOUR CODE HERE ####
    ########################
#    qvec = np.zeros(dim)
#    question_words = question.split(' ')
##    count = 0
#    for word in question_words:
#        if word in embeddings:
##            qvec += embeddings[word]
#            count += 1
#    return qvec
    words_embedding = [embeddings[word] for word in question.split() if word in embeddings]
    if not words_embedding:
        return np.zeros(dim)
    words_embedding = np.array(words_embedding)
    return words_embedding.mean(axis=0)


def unpickle_file(filename):
    """Returns the result of unpickling the file content."""
    with open(filename, 'rb') as f:
        return pickle.load(f)
