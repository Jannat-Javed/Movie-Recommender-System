import pandas as pd
import pickle
import streamlit as st
import requests

# Function to fetch the movie poster from an API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to fetch detailed information about a movie
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    response = requests.get(url).json()
    return {
        "title": response.get("title", "N/A"),
        "release_date": response.get("release_date", "N/A"),
        "runtime": response.get("runtime", "N/A"),
        "vote_average": f"{response.get('vote_average', 0):.1f}",
        "overview": response.get("overview", "N/A"),
        "genres": ", ".join([genre['name'] for genre in response.get("genres", [])]),
        "poster": fetch_poster(movie_id)
    }

# Function to recommend movies similar to the selected one
def recommend(movie_title):
    if movie_title in movies['title'].values:
        index = movies[movies['title'] == movie_title].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = []
        for i in distances[1:11]:  # Get top 10 recommendations
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(fetch_movie_details(movie_id))
        return recommended_movies
    

# UI Setup
st.header('🎬 Movie Recommender System')

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Select a movie from the dropdown
selected_movie = st.selectbox("Select a movie to get recommendations", movies['title'].values)

# Show details of the selected movie
selected_movie_id = movies[movies['title'] == selected_movie].iloc[0].movie_id
selected_movie_data = fetch_movie_details(selected_movie_id)
st.subheader(f"Selected Movie: {selected_movie_data['title']}")
st.image(selected_movie_data['poster'], width=150)  # Display reduced size image
st.markdown(f"**Release Date:** {selected_movie_data['release_date']}")
st.markdown(f"**Rating:** {selected_movie_data['vote_average']}")
st.markdown(f"**Runtime:** {selected_movie_data['runtime']} min")
st.markdown(f"**Genres:** {selected_movie_data['genres']}")
st.markdown(f"**Overview:** {selected_movie_data['overview']}")

# Show recommendations when the button is pressed
if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie)
    if recommended_movies:
        st.subheader(f"Recommendations for {selected_movie}:")
        cols = st.columns(5)  # Create 5 columns for layout
        for i, movie in enumerate(recommended_movies):
            with cols[i % 5]:
                st.image(movie['poster'], use_column_width=True)
                st.markdown(f"**{movie['title']}**")
                st.markdown(f"Release Date: {movie['release_date']}")
                st.markdown(f"Rating: {movie['vote_average']}")
                st.markdown(f"Runtime: {movie['runtime']} min")
   
