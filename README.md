## 🚀 Live Demo
Try it here: https://movie-graph-explorer-6ufrejc8vsbzyexmquwqwv.streamlit.app/
# 🎬 Movie Universe Graph Explorer

A project combining **Data Structures & Algorithms** (graphs, BFS, Dijkstra) with **Machine Learning** (TF-IDF + cosine similarity) to explore how actors and movies are connected — like the "Six Degrees of Kevin Bacon" game, plus a content-based movie recommender.

## What it does

1. **Actor Path Finder** — Enter two actors, and the app finds the shortest chain of shared movies connecting them, using a **custom-built BFS algorithm** (not a library shortcut).
2. **Movie Recommender** — Enter a movie, and get similar movies using **TF-IDF vectorization + cosine similarity** on genre and plot data.

## Why this project stands out

- Implements **BFS and Dijkstra from scratch** on a graph built from real movie/actor co-star relationships — a strong DSA showcase, not just an ML model call.
- Combines graph theory with NLP-based similarity (TF-IDF) in one cohesive app.
- Fully self-contained: works out of the box with an embedded dataset, no external API keys or downloads required.

## Tech Stack

- Python
- Custom graph + BFS/Dijkstra implementation (`graph.py`)
- Scikit-learn (TF-IDF, cosine similarity)
- Streamlit (web UI)

## Project Structure

```
movie-graph-explorer/
├── data.py          # embedded movie dataset (title, genre, overview, cast)
├── graph.py          # MovieGraph class: builds graph, custom BFS + Dijkstra
├── recommender.py    # TF-IDF + cosine similarity recommender
├── app.py             # Streamlit web app
├── main.py            # CLI demo (no Streamlit needed)
├── requirements.txt
└── README.md
```

## How to Run

### Option 1: Web app (recommended for demo)
```bash
pip install -r requirements.txt
streamlit run app.py
```
This opens a browser tab where you can pick two actors and see their connection, or pick a movie to get recommendations.

### Option 2: Command-line demo (fastest, no browser)
```bash
pip install scikit-learn
python main.py
```
This prints example actor paths and recommendations directly to the terminal.

## How the algorithms work

**BFS (Breadth-First Search)**
The graph has actors as nodes and an edge between two actors if they appeared in the same movie. BFS explores the graph level by level from the starting actor, guaranteeing the path found has the *fewest* movie-hops — the true "degrees of separation."

**Dijkstra (bonus, in `graph.py`)**
A weighted variant is also implemented: edges through higher-rated movies are cheaper, so the algorithm can find a path that favors well-reviewed movies instead of just the shortest hop count.

**TF-IDF + Cosine Similarity**
Each movie's genre and plot overview are converted into TF-IDF vectors (numeric representations that weigh distinctive words more heavily). Cosine similarity then measures how "close" two movies are in that vector space, powering the recommendations.

## Example Output
```
--- Path from 'Elliot Page' to 'Robert Downey Jr.' (BFS) ---
Degrees of separation: 4
  Elliot Page  --[Inception]-->  Leonardo DiCaprio
  Leonardo DiCaprio  --[Once Upon a Time in Hollywood]-->  Brad Pitt
  Brad Pitt  --[Se7en]-->  Gwyneth Paltrow
  Gwyneth Paltrow  --[Iron Man]-->  Robert Downey Jr.

--- Movies similar to 'The Dark Knight' ---
  Batman Begins  (similarity: 0.403)
  Kill Bill  (similarity: 0.243)
  Taxi Driver  (similarity: 0.159)
```

## Possible Extensions
- Swap the embedded dataset for the full TMDB 5000 dataset (Kaggle) for thousands of real movies.
- Add an interactive graph visualization using `pyvis` or `networkx` + `matplotlib`.
- Weight edges by box office or rating for more Dijkstra path variety.

## Author
Built as a portfolio project demonstrating applied DSA (graph algorithms) + ML (NLP similarity).
