#required liberaries
import pandas as pd
import numpy as np
import  re # regular expression
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings("ignore")

#data gathering 
df=pd.read_csv("SMSSpamCollection", sep='\t', names = ['lable','mesg'])
df.head()

#EDA(Exploratory Data Analysis)
df.info()

df.isna().sum()

df['lable'].value_counts()

corpus = []
lm = WordNetLemmatizer()
for i in range(len(df)):
    review = re.sub(r'[^a-zA-Z0-9]', ' ', df['mesg'][i])
    review = review.lower()
    review = review.split()
    review = [data for data in review if data not in stopwords.words('english')]
    review = [lm.lemmatize(data) for data in review]
    review = "".join(review)
    corpus.append(review)
    
df['mesg'][0]
len(df['mesg'])
len(corpus)

df['mesg']=corpus
df.head()