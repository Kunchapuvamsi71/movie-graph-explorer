"""
Content-based movie recommender.

Builds a TF-IDF matrix over each movie's genre + overview text,
then uses cosine similarity to find the most similar movies to
a given title.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    def __init__(self, movies):
        self.movies = movies
        self.titles = [m["title"] for m in movies]
        # combine genre + overview so both style and plot influence similarity
        self.corpus = [f"{m['genre']} {m['genre']} {m['overview']}" for m in movies]

        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def recommend(self, title, top_n=5):
        if title not in self.titles:
            return []
        idx = self.titles.index(title)
        scores = list(enumerate(self.similarity_matrix[idx]))
        # exclude the movie itself, sort by similarity descending
        scores = [s for s in scores if s[0] != idx]
        scores.sort(key=lambda x: x[1], reverse=True)
        top = scores[:top_n]
        return [(self.titles[i], round(float(score), 3)) for i, score in top]
