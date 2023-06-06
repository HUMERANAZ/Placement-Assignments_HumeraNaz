import pandas as pd
import youtube_comment_scraper as ycs
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim import corpora, models

# Set up NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Define YouTube video URL
video_url = "https://www.youtube.com/channel/UCNU_lfiiWBdtULKOw6X0Dig"

# Scrape comments from the YouTube video
comments = ycs.scrape(video_url)

# Preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
preprocessed_comments = []

for comment in comments:
    # Remove special characters and digits
    comment = re.sub(r'\W', ' ', comment)
    comment = re.sub(r'\d+', ' ', comment)
    
    # Tokenization
    tokens = word_tokenize(comment.lower())
    
    # Remove stopwords and perform lemmatization
    processed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    
    preprocessed_comments.append(processed_tokens)

# Create dictionary and corpus
dictionary = corpora.Dictionary(preprocessed_comments)
corpus = [dictionary.doc2bow(comment) for comment in preprocessed_comments]

# Perform LDA topic modeling
lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)

# Get topics and their keywords
topics = lda_model.show_topics(num_topics=5, num_words=5)

# Store topics and keywords in a DataFrame
topics_df = pd.DataFrame([(topic[0], topic[1]) for topic in topics], columns=["Topic", "Keywords"])

# Display the most demanding topic
most_demanding_topic = topics_df.iloc[0]["Topic"]
print("The most demanding topic is:", most_demanding_topic)

# Save the comments and their corresponding topics to a CSV file
comments_df = pd.DataFrame({"Comment": comments})
comments_df["Topic"] = [lda_model[dictionary.doc2bow(comment)][0][0] for comment in preprocessed_comments]
comments_df.to_csv("comments_topics.csv", index=False)
