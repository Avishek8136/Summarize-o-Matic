# Summarize-o-Matic: Text Summarizer

📌Introduction
------------------
Text summarizers are essential tools in today's information-rich society, where massive volumes of data are generated every minute. They aid in rapidly extracting vital information from long texts, allowing users to absorb the main ideas without having to read the entire text. This is especially valuable for professionals, researchers, and students who need to review big amounts of information fast. Text summarizers also help in decision-making by providing brief insights, increasing productivity, and saving time. In the business world, they provide quick comprehension of reports, emails, and publications, hence increasing workflow efficiency. Finally, text summarizers address the issue of information overload by making relevant information accessible and manageable.📚💼🔍

## Libraries Required
------------------

NLTK:-The NLTK library is a general Python toolkit for natural language processing (NLP) activities that includes easy-to-use interfaces to over 50 corpus and lexical resources, as well as a suite of text processing tools for classification, tokenization, stemming, tagging, parsing, and more.📚

RE:- Regular expressions (RE) are character sequences that generate search patterns. They are generally used for string matching and manipulation. They are strong text processing tools that let users to do complex search and replace operations, extract specific data from huge volumes of text, and validate input formats. 🔍

Tkinter:- Tkinter is a typical Python package for developing graphical user interfaces (GUIs). It allows you to quickly and easily create desktop programs by providing a number of widgets such as buttons, labels, text fields, and menus. 🖥️

Heapq:- Implementations of the heap queue algorithm are available via the Python package heapq. It makes it possible to insert and remove items from heap data structures—a type of customized tree-based data structure that complies with the heap property—efficiently. According to the heap property, a binary heap can only have a parent node that is either larger (max heap) or smaller (min heap) than its offspring. ⏳

Pyttsx3:- The 'pyttsx3' Python module is a text-to-speech conversion library that works offline and supports a variety of TTS engines. It allows you to convert text to spoken words and adjust speech parameters such as rate, volume, and voice.

## Installating the required libraries
------------------

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Text Summarization Steps
------------------

#### Preprocessing
------------------

The initial preprocessing step is to remove all references from the article. The square brackets are eliminated, the ensuing many spaces are replaced with a single space, and the input is further cleaned. 

We will not remove any other numbers, punctuation marks, or special characters from this text because we will utilize it to generate summaries, and weighted word frequencies will be replaced in this article.✂️

We now have two objects: article_text (original article) and formatted_article_text (formatted article). 📝

#### Converting Text into Sentences
------------------

We will now utilize the article_text object to tokenize the article into a sentence because it contains full stops. The formatted_article_text lacks punctuation and so cannot be translated into sentences with the full stop as a parameter.📝

#### Find the Weighted Frequency of Occurrence.
------------------

We utilize the formatted_article_text variable to determine the frequency with which each word appears. We utilized this variable to calculate frequency of occurrence because it lacks punctuation, numerals, and other special characters. Now we loop through all of the phrases and their matching words to see if they are stop words. If not, we check to see if the terms exist in the word_frequency dictionary (also known as word_frequencies).

To calculate the weighted frequency, we divided the number of occurrences of each word by the frequency of the most frequent word.📊

#### Example:- Weight Frequency of Occurence

| Word     | Frequency | Weighed Frequency |
|----------|-----------|-------------------|
| keep     | 5         | 1.00              |
| striving | 1         | 0.20              |

#### Calculating Sentence Scores
------------------

Calculate the scores for each sentence by adding the weighted frequencies of the words in that sentence. We calculated the score solely for statements containing fewer than 35 words.

#### Example:-Sum of Weighted frequencies

| Sentence     | Sum of Weighted Frequencies | 
|----------|-----------|
| Keep striving     | 1 + 0.20 = 1.20       | 

#### Genearating the summary
------------------

Now we have the sentence_scores dictionary, which contains sentences and their related scores. To summarize the article, we can select the top N sentences with the highest score. The following script retrieves the top seven sentences and prints them to the screen.📝

## Important Links:- 

[NLTK](https://www.nltk.org/)
[NLTK in python](https://pypi.org/project/nltk/)
[Tkinter GUI](https://docs.python.org/3/library/tkinter.html)
[Pyttsx3](https://pypi.org/project/pyttsx3/)

<p align="center">© <a href="https://events.mlh.io/events/11279">2024 Data Hack Fest</a> | <a href="https://www.github.com/Avishek8136"> Avishek Rauniyar </a> | All rights reserved. </p>