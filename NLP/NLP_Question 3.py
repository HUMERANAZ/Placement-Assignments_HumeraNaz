import pandas as pd
from gensim import models, corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from nltk.corpus import stopwords

# Load the CSV file
data = pd.read_csv('instagram_reach.csv')

# Preprocess the text data
stop_words = stopwords.words('english')
data['Text'] = data['Text'].apply(lambda x: ' '.join(simple_preprocess(x, deacc=True) if x else ''))

# Tokenize the text data
tokenized_data = [text.split() for text in data['Text']]

# Create a dictionary from the tokenized data
dictionary = corpora.Dictionary(tokenized_data)

# Create a corpus from the tokenized data
corpus = [dictionary.doc2bow(text) for text in tokenized_data]

# Perform keyword extraction using TF-IDF
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
keywords = []
for doc in corpus_tfidf:
    sorted_doc = sorted(doc, key=lambda x: x[1], reverse=True)
    for term_id, weight in sorted_doc[:5]:  # Extract top 5 keywords from each document
        keywords.append(dictionary[term_id])

# Perform topic modeling using Latent Dirichlet Allocation (LDA)
num_topics = 5
lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary)
topics = lda_model.print_topics(num_words=5)  # Get top 5 words for each topic

# Print the keywords and topics
print("Keywords:")
print(keywords)
print("Topics:")
for topic in topics:
    print(topic)
