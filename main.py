"""
Command-line demo of the Movie Universe Graph Explorer.
Useful for quickly testing the logic without launching Streamlit.

Run with: python main.py
"""

from data import MOVIES
from graph import MovieGraph
from recommender import MovieRecommender


def print_path(graph, actor_a, actor_b):
    path, movies_used = graph.bfs_shortest_path(actor_a, actor_b)
    print(f"\n--- Path from '{actor_a}' to '{actor_b}' (BFS) ---")
    if path is None:
        print("No connection found.")
        return
    if len(path) == 1:
        print("Same actor.")
        return
    print(f"Degrees of separation: {len(path) - 1}")
    for i in range(len(path) - 1):
        print(f"  {path[i]}  --[{movies_used[i]}]-->  {path[i + 1]}")


def print_recommendations(recommender, title, top_n=5):
    print(f"\n--- Movies similar to '{title}' ---")
    results = recommender.recommend(title, top_n=top_n)
    if not results:
        print("Movie not found.")
        return
    for t, score in results:
        print(f"  {t}  (similarity: {score})")


if __name__ == "__main__":
    graph = MovieGraph(MOVIES)
    recommender = MovieRecommender(MOVIES)

    print("=== Movie Universe Graph Explorer (CLI demo) ===")
    print(f"Total movies: {len(MOVIES)}")
    print(f"Total actors: {len(graph.actors())}")

    # Example 1: two actors who never worked together directly
    print_path(graph, "Elliot Page", "Robert Downey Jr.")

    # Example 2: two actors in totally different movie circles
    print_path(graph, "Keira Knightley", "Bruce Willis")

    # Example 3: recommend similar movies
    print_recommendations(recommender, "Inception")
    print_recommendations(recommender, "The Dark Knight")
