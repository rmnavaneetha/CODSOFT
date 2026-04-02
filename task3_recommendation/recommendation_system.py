# recommendation_system.py

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (movies with genres)
movies = [
    {"title": "Inception", "genre": "sci-fi thriller action"},
    {"title": "Titanic", "genre": "romance drama"},
    {"title": "Avengers", "genre": "action superhero sci-fi"},
    {"title": "The Notebook", "genre": "romance drama"},
    {"title": "Interstellar", "genre": "sci-fi drama space"},
    {"title": "John Wick", "genre": "action thriller"},
    {"title": "Frozen", "genre": "animation family fantasy"},
    {"title": "Toy Story", "genre": "animation family comedy"}
]

# Convert genres into text list
genres = [movie["genre"] for movie in movies]

# Convert text to vectors
cv = CountVectorizer()
count_matrix = cv.fit_transform(genres)

# Compute similarity
similarity = cosine_similarity(count_matrix)


# Function to recommend movies
def recommend(movie_name):
    movie_indices = {movie["title"]: idx for idx, movie in enumerate(movies)}

    if movie_name not in movie_indices:
        print("Movie not found in database!")
        return

    idx = movie_indices[movie_name]
    scores = list(enumerate(similarity[idx]))

    # Sort based on similarity score
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended movies for '{movie_name}':\n")

    # Skip first one (itself)
    for i in scores[1:6]:
        print(movies[i[0]]["title"])


# User input
if __name__ == "__main__":
    print("Available Movies:")
    for movie in movies:
        print("-", movie["title"])

    user_input = input("\nEnter a movie name: ")
    recommend(user_input)