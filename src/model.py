from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

vectorizer = TfidfVectorizer()
model = LogisticRegression(class_weight='balanced')

def train_model(X, y):
    X_vec = vectorizer.fit_transform(X)
    model.fit(X_vec, y)
    return model, vectorizer

def predict(text, model, vectorizer, preprocess_func):
    cleaned = preprocess_func(text)
    vec = vectorizer.transform([cleaned])
    return model.predict(vec)[0]