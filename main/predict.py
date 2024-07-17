import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
def linear_regression(question):
    question=question.lower()
    model = joblib.load(r"F:\spam-mail-prediction\mailprediction\main\logistic_regression_model.pkl")
    feature_extraction = joblib.load(r"F:\spam-mail-prediction\mailprediction\main\tfidf_vectorizer.pkl")
    texts = [question]
    x_test = feature_extraction.transform(texts)
    ans = model.predict(x_test)
    print(ans)
    if ans[0]==0:
        return "Ham Mail"
    return "Spam Mail"