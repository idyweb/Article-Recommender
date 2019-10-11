# -*- coding: utf-8 -*-
"""keyword.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BFpqReIgy9_dSTNbnHVAx0-SM2KMuyvH
"""

pip install newspaper3k

from newspaper import Article 
import nltk
nltk.download('punkt')

#A new article from anywhere 
URL = "https://lucid.blog/mercyinyang/post/flutterwave-africas-largest-online-payment-gateway-be0"

#To set language to English
ARTICLE = Article(URL, language="en") # en for English 

#To download the article 
ARTICLE.download() 

#To parse the article 
ARTICLE.parse() 

#To perform natural language processing ie..nlp 
ARTICLE.nlp() 

#To extract title 
print("Article's Title:") 
print(ARTICLE.title) 
print("n") 

#To extract text 
print("Article's Text:") 
print(ARTICLE.text) 
print("n") 

#To extract summary 
print("Article's Summary:") 
print(ARTICLE.summary) 
print("n")



#To extract keywords 
''' keyword function to return article keywords '''
def keyword():
  print("keyword in article")
  print(ARTICLE.keywords)

keyword()

