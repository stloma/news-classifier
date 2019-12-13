import connexion
import joblib

app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

clf = joblib.load('model/news_classifier.joblib')
count_vectorizer = joblib.load('model/count_vectorizer.joblib')
classifications = joblib.load('model/classifications.joblib')


def health():

    try:
        predict('text text')
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}


def predict(article):

    word_counts = count_vectorizer.transform([article])
    prediction = clf.predict_log_proba(word_counts)

    ordered_classifications = dict(zip(classifications, prediction[0]))
    ordered_classifications = {k: v for k, v in sorted(
        ordered_classifications.items(), key=lambda x: x[1], reverse=True)}

    classes = list(ordered_classifications.keys())
    scores = list(ordered_classifications.values())

    return [classes, scores]


app.add_api("news_classification_api.yaml")

if __name__ == "__main__":
    app.run()
