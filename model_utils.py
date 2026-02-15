import pickle
import os
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def build_similarity():
    print("⚙️ Generating similarity matrix...")

    # movies = pickle.load(open("movies.pkl", "rb"))
    with open("movies.pkl", "rb") as f:
        movies = pickle.load(f)

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()

    similarity = cosine_similarity(vectors)

    # pickle.dump(similarity, open("similarity.pkl", "wb"))
    with open("similarity.pkl", "wb") as f:
        pickle.dump(similarity, f)

    print("✅ similarity.pkl generated")
    return similarity
