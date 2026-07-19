import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

medicine_df = pd.read_csv("data/medicines.csv")

medicine_df["Features"] = (
    medicine_df["Disease"] + " " +
    medicine_df["Category"]
)

vectorizer = CountVectorizer()

feature_matrix = vectorizer.fit_transform(medicine_df["Features"])

similarity = cosine_similarity(feature_matrix)


def recommend_medicine(medicine_name):
    medicine_name = medicine_name.lower()

    index = None

    for i, med in enumerate(medicine_df["Medicine"]):
        if med.lower() == medicine_name:
            index = i
            break

    if index is None:
        return []

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i in scores[1:4]:
        recommendations.append(medicine_df.iloc[i[0]]["Medicine"])

    return recommendations