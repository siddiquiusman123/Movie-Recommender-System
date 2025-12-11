import joblib
import streamlit as st
import requests
import pandas as pd
import gdown
import os

file_id = "18sIsXqGyDINfrIdk-wX5QeCI1YwRoKc9"
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Download only if the file doesn't exist
if not os.path.exists("similarity.pkl"):
    with st.spinner("Downloading similarity model..."):
        gdown.download(url, "similarity.pkl", quiet=False)
        st.success("Model downloaded successfully!")

st.header('Movie Recommender System')
movies_list = joblib.load("movies_dict.pkl")
movies = pd.DataFrame(movies_list)

try:
    similarity = joblib.load("similarity.pkl")
except FileNotFoundError:
    st.error("Failed to load similarity model. Please check the download.")
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c5186a5eecc1cd93c187a87726e66f52&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    num_cols = len(recommended_movie_names)
    cols = st.columns(num_cols)

    for i, col in enumerate(cols):
        col.image(recommended_movie_posters[i], use_container_width=True)
        col.caption(recommended_movie_names[i])
