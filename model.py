from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dummy training data
texts = ["This is a bad comment", "You are awesome", "Terrible language here"]
labels = [1, 0, 1]  # 1 = Profane, 0 = Clean

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

# Prediction Function
def is_profane(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0] == 1
