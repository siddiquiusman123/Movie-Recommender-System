import joblib
import streamlit as st
import requests
import pandas as pd
import os

st.header("Movie Recommender System")

# Load data
similarity = joblib.load("similarity.pkl")
movies_list = joblib.load("movies_dict.pkl")
movies = pd.DataFrame(movies_list)

movie_list = movies["title"].values
selected_movie = st.selectbox("Search for a movie", movie_list)

# Secure API Key (avoid hardcoding)
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    if not TMDB_API_KEY:
        return None
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    
    try:
        data = requests.get(url, timeout=5).json()
        poster_path = data.get("poster_path")
        if not poster_path:
            return None
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception:
        return None


def recommend(movie):
    if movie not in movies["title"].values:
        return [], []

    index = movies[movies["title"] == movie].index[0]

    # Faster top-5 extraction
    similarity_scores = similarity[index]
    top_indices = similarity_scores.argsort()[::-1][1:6]

    names = []
    posters = []

    for idx in top_indices:
        movie_id = movies.iloc[idx].id
        names.append(movies.iloc[idx].title)
        posters.append(fetch_poster(movie_id))

    return names, posters


if st.button("Show Recommendation"):
    names, posters = recommend(selected_movie)

    if not names:
        st.error("No recommendations found.")
    else:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            if i < len(names):
                col.image(posters[i] or "https://via.placeholder.com/500", use_container_width=True)
                col.caption(names[i])
