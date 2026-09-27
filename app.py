"""
Movie Universe Graph Explorer -- Streamlit App

Run with:  streamlit run app.py
"""

import streamlit as st
from data import MOVIES
from graph import MovieGraph
from recommender import MovieRecommender

st.set_page_config(page_title="Movie Universe Graph Explorer", page_icon="🎬", layout="centered")

st.title("🎬 Movie Universe Graph Explorer")
st.caption(
    "Find how any two actors are connected through shared movies "
    "(custom BFS graph search), and discover similar movies "
    "(TF-IDF + cosine similarity)."
)


@st.cache_resource
def load_data():
    graph = MovieGraph(MOVIES)
    recommender = MovieRecommender(MOVIES)
    return graph, recommender


graph, recommender = load_data()
actor_list = graph.actors()
movie_titles = [m["title"] for m in MOVIES]

tab1, tab2 = st.tabs(["🔗 Actor Path Finder", "🎥 Movie Recommender"])

with tab1:
    st.subheader("Find the connection between two actors")
    col1, col2 = st.columns(2)
    with col1:
        actor_a = st.selectbox("Actor A", actor_list, index=0)
    with col2:
        actor_b = st.selectbox("Actor B", actor_list, index=min(5, len(actor_list) - 1))

    if st.button("Find Path (BFS)"):
        path, movies_used = graph.bfs_shortest_path(actor_a, actor_b)
        if path is None:
            st.error("No connection found between these two actors in this dataset.")
        elif len(path) == 1:
            st.info("That's the same actor!")
        else:
            degrees = len(path) - 1
            st.success(f"Degrees of separation: {degrees}")
            for i in range(len(path) - 1):
                st.write(f"**{path[i]}** → *{movies_used[i]}* → **{path[i + 1]}**")

with tab2:
    st.subheader("Get similar movies")
    selected_movie = st.selectbox("Pick a movie", movie_titles)
    top_n = st.slider("Number of recommendations", 3, 10, 5)

    if st.button("Recommend"):
        results = recommender.recommend(selected_movie, top_n=top_n)
        if not results:
            st.error("Movie not found.")
        else:
            st.write(f"Movies similar to **{selected_movie}**:")
            for title, score in results:
                st.write(f"- **{title}**  (similarity: {score})")

st.divider()
st.caption(
    "Built with a custom BFS graph traversal over an actor co-star network, "
    "and a TF-IDF + cosine similarity content-based recommender. "
    "Dataset: hand-curated sample of well-known movies."
)
