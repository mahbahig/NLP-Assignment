import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.exceptions import NotFittedError


class SpamClassifier:
    def __init__(self):
        # store artifacts inside the package directory so training scripts
        # can save them where the package will reliably find them.
        base_dir = os.path.dirname(__file__)
        model_path = os.path.join(base_dir, "spam_model.pkl")
        vec_path = os.path.join(base_dir, "vectorizer.pkl")

        if os.path.exists(model_path) and os.path.exists(vec_path):
            try:
                self.model = joblib.load(model_path)
                self.vectorizer = joblib.load(vec_path)
            except Exception:
                self.vectorizer = CountVectorizer()
                self.model = MultinomialNB()
        else:
            self.vectorizer = CountVectorizer()
            self.model = MultinomialNB()

    def predict(self, text):
        try:
            x = self.vectorizer.transform([text])
            pred = self.model.predict(x)[0]
            return "spam" if int(pred) == 1 else "not_spam"
        except (NotFittedError, AttributeError, ValueError, Exception):
            return "not_spam"
