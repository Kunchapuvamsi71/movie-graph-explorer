"""
Graph construction and custom path-finding algorithms.

We build an undirected graph where:
- Nodes  = actors
- Edges  = "co-starred together", labeled with the movie title
- Edge weight (for Dijkstra) = 10 - movie_score, so higher-rated
  connections are "cheaper" to traverse.

Both BFS and Dijkstra are implemented from scratch (no networkx
shortest-path calls) to demonstrate the underlying algorithms --
this is the core DSA showcase of the project.
"""

from collections import defaultdict, deque
import heapq


class MovieGraph:
    def __init__(self, movies):
        """
        movies: list of dicts with keys 'title', 'genre', 'overview', 'cast'
        """
        self.movies = movies
        self.adj = defaultdict(list)   # actor -> list of (neighbor, movie_title)
        self.actor_movies = defaultdict(set)
        self._build_graph()

    def _build_graph(self):
        for movie in self.movies:
            cast = movie["cast"]
            title = movie["title"]
            for actor in cast:
                self.actor_movies[actor].add(title)
            # connect every pair of co-stars in this movie
            for i in range(len(cast)):
                for j in range(i + 1, len(cast)):
                    a, b = cast[i], cast[j]
                    self.adj[a].append((b, title))
                    self.adj[b].append((a, title))

    def actors(self):
        return sorted(self.adj.keys())

    def bfs_shortest_path(self, start, end):
        """
        Custom BFS implementation.
        Returns (path, movies_connecting_each_step) or (None, None) if
        no path exists. This finds the path with the FEWEST hops,
        i.e. the smallest "degrees of separation".
        """
        if start not in self.adj or end not in self.adj:
            return None, None
        if start == end:
            return [start], []

        visited = {start}
        queue = deque([start])
        parent = {}       # child -> (parent, movie_used)

        while queue:
            current = queue.popleft()
            if current == end:
                break
            for neighbor, movie in self.adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = (current, movie)
                    queue.append(neighbor)

        if end not in visited:
            return None, None

        # reconstruct path
        path = [end]
        movies_used = []
        node = end
        while node != start:
            prev, movie = parent[node]
            path.append(prev)
            movies_used.append(movie)
            node = prev

        path.reverse()
        movies_used.reverse()
        return path, movies_used

    def dijkstra_path(self, start, end, movie_scores=None):
        """
        Custom Dijkstra implementation. If movie_scores (dict title -> 0-10
        rating) is provided, edges through higher-rated movies are
        treated as "cheaper", so the path favors well-reviewed movies
        over the raw shortest hop count.
        """
        if start not in self.adj or end not in self.adj:
            return None, None

        movie_scores = movie_scores or {}
        dist = {start: 0}
        parent = {}
        visited = set()
        pq = [(0, start)]

        while pq:
            d, current = heapq.heappop(pq)
            if current in visited:
                continue
            visited.add(current)
            if current == end:
                break

            for neighbor, movie in self.adj[current]:
                score = movie_scores.get(movie, 7)   # default mid rating
                weight = max(0.5, 10 - score)         # better movie = cheaper edge
                nd = d + weight
                if neighbor not in dist or nd < dist[neighbor]:
                    dist[neighbor] = nd
                    parent[neighbor] = (current, movie)
                    heapq.heappush(pq, (nd, neighbor))

        if end not in dist:
            return None, None

        path = [end]
        movies_used = []
        node = end
        while node != start:
            prev, movie = parent[node]
            path.append(prev)
            movies_used.append(movie)
            node = prev

        path.reverse()
        movies_used.reverse()
        return path, movies_used
