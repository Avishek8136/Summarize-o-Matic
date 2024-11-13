import streamlit as st
import nltk
import re
import heapq
import os
from nltk.corpus import stopwords
from nltk import data

# Custom NLTK data directory (useful for cloud deployments)
nltk_data_dir = './nltk_data'
os.makedirs(nltk_data_dir, exist_ok=True)
data.path.append(nltk_data_dir)

# Download NLTK data files if they aren't already present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_dir)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=nltk_data_dir)

def summarize_text(article_text, num_sentences):
    # Clean and format the input text
    article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
    article_text = re.sub(r'\s+', ' ', article_text)
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    # Tokenize the article into sentences
    sentence_list = nltk.sent_tokenize(article_text)

    # Get stopwords
    stop_words = set(stopwords.words('english'))

    # Calculate word frequencies
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word.lower() not in stop_words:
            word_frequencies[word.lower()] = word_frequencies.get(word.lower(), 0) + 1

    # Find maximum frequency
    maximum_frequency = max(word_frequencies.values())

    # Normalize frequencies
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequency

    # Calculate sentence scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Get the top N sentences for the summary
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary

# Streamlit UI
st.title("Text Summarizer")
st.write("Enter the text below to get a summary:")

# Text area for input
article_text = st.text_area("Enter Text", height=300)

# Number of sentences input
num_sentences = st.number_input("Number of sentences for the summary:", min_value=1, max_value=20, value=7, step=1)

# Summarize button
if st.button("Summarize"):
    if article_text:
        summary = summarize_text(article_text, num_sentences)
        st.subheader("Summary")
        st.write(summary)
    else:
        st.error("Please enter some text to summarize.")
