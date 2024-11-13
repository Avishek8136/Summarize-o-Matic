# Summarize-o-Matic: Text Summarizer 📄🤖

📌 **Introduction**
------------------
Text summarizers have become essential tools in today’s data-heavy world. They help users quickly extract main ideas from lengthy texts, making it easier to grasp crucial information without reading through the entire content. This capability is invaluable for professionals, researchers, and students who often need to process large volumes of data rapidly. Text summarizers also streamline decision-making, boost productivity, and save time by offering quick insights. In business, they enhance workflow by summarizing reports, emails, and documents, helping reduce information overload and making relevant information more accessible. 📚💼🔍

## 🛑 **Problem Statement** 

In an age of information overload, users often face the challenge of processing massive amounts of text quickly and efficiently. Manually sifting through lengthy documents to find key insights is time-consuming and impractical for professionals, students, and researchers. The goal is to develop an automated text summarizer that condenses large texts into concise summaries, capturing essential points without losing context, thus enabling users to make informed decisions faster and improve productivity.

## 🔧 **Libraries Required**
------------------

- **NLTK** 📚: A comprehensive toolkit for natural language processing in Python, providing interfaces for over 50 corpus and lexical resources, plus tools for text processing like classification, tokenization, and stemming.
- **RE** 🔍: Regular expressions used for pattern matching and string manipulation, enabling complex search, replace, and text extraction tasks.
- **Tkinter** 🖥️: A standard Python package for building graphical user interfaces, featuring a variety of widgets like buttons, labels, and text fields.
- **Heapq** ⏳: A library for efficient heap queue (priority queue) operations, often used for handling tree-based data structures.
- **Pyttsx3** 🗣️: An offline text-to-speech conversion library that enables text-to-speech functionalities with adjustable parameters like rate, volume, and voice.

## 🛠️ **Installing the Required Libraries**
------------------

Run the following command to install the required libraries:

```bash
pip install -r requirements.txt
```

## 🚀 **Text Summarization Steps**
------------------

#### **1. Preprocessing** ✂️
------------------
The preprocessing stage involves cleaning the text by removing references and replacing multiple spaces with a single space. The text remains otherwise unchanged to retain its weighted word frequencies for summarization.

#### **2. Converting Text into Sentences** 📝
------------------
Tokenize the `article_text` into sentences, utilizing punctuation to identify sentence boundaries. The `formatted_article_text` does not contain punctuation, so tokenizing is only possible using `article_text`.

#### **3. Finding the Weighted Frequency of Words** 📊
------------------
Use the `formatted_article_text` to calculate the frequency of each word, excluding stop words. Then calculate the weighted frequency by dividing each word’s count by the highest frequency in the text.

##### **Example: Weighted Frequency of Occurrence**

| Word     | Frequency | Weighted Frequency |
|----------|-----------|-------------------|
| keep     | 5         | 1.00              |
| striving | 1         | 0.20              |

#### **4. Calculating Sentence Scores** 📝
------------------
Score each sentence by summing the weighted frequencies of its words. Only sentences with fewer than 35 words are considered to improve summary clarity.

##### **Example: Sum of Weighted Frequencies**

| Sentence     | Sum of Weighted Frequencies | 
|--------------|-----------------------------|
| Keep striving| 1 + 0.20 = 1.20             | 

#### **5. Generating the Summary** 📝
------------------
Using the `sentence_scores` dictionary, retrieve the top N sentences with the highest scores to create the summary. The script typically selects the top seven sentences.

## 🛑 **Problem Statement**
------------------
Design a summarization tool that provides users with condensed insights from lengthy text documents while maintaining the context and key information, helping users quickly understand large amounts of data in limited time.

## 🌐 **Deployment Link**
------------------
Explore the application live here: [Summarize-o-Matic](https://summarize-o-matic.streamlit.app/)

## 🔗 **Important Links**
------------------
- [NLTK Documentation](https://www.nltk.org/)
- [NLTK on PyPI](https://pypi.org/project/nltk/)
- [Tkinter GUI Docs](https://docs.python.org/3/library/tkinter.html)
- [Pyttsx3 on PyPI](https://pypi.org/project/pyttsx3/)

<p align="center">© [2024 Data Hack Fest](https://events.mlh.io/events/11279) | [Avishek Rauniyar](https://www.github.com/Avishek8136) | All rights reserved. 📅</p># Summarize-o-Matic: Text Summarizer 📄🤖
