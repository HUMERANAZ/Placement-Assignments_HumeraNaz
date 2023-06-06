import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
import heapq

def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words
    words = [word_tokenize(sentence.lower()) for sentence in sentences]

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    words = [[word for word in sentence if word not in stop_words] for sentence in words]

    # Perform stemming
    ps = PorterStemmer()
    words = [[ps.stem(word) for word in sentence] for sentence in words]

    return words

def calculate_sentence_scores(words):
    # Calculate word frequency distribution
    word_frequency = FreqDist()

    for sentence in words:
        for word in sentence:
            word_frequency[word] += 1

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for i, sentence in enumerate(words):
        score = 0
        for word in sentence:
            score += word_frequency[word]
        sentence_scores[i] = score

    return sentence_scores

def generate_summary(text, num_sentences):
    # Preprocess the text
    words = preprocess_text(text)

    # Calculate sentence scores
    sentence_scores = calculate_sentence_scores(words)

    # Select top sentences with highest scores
    selected_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Generate the summary
    summary = ' '.join([sentences[i] for i in selected_sentences])
    return summary

# Read the text from the file
with open('My_text.txt', 'r') as file:
    text = file.read()

# Generate the summary
summary = generate_summary(text, num_sentences=3)
print(summary)
