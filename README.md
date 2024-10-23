##  Content Based Movie Recommender System

The Content-Based Movie Recommender System is designed to provide personalized movie recommendations by analyzing the content of movies and matching them to user preferences. Using the TMDB Movie Metadata dataset, the system considers features such as genre, keywords, cast, and crew to generate a list of movies similar to those a user has enjoyed in the past. The model processes and vectorizes these features to compute similarity scores, ensuring that the recommendations align closely with the user’s tastes. The system is built in Streamlit, offering an interactive interface where users can select a movie and receive ten similar movie recommendations, each displayed with its corresponding poster. This project is ideal for users who want tailored movie suggestions based on their viewing history and preferences.

### Dataset

The recommender system uses the TMDB Movie Metadata dataset from Kaggle

[Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The Dataset includes:

* movie_id: Unique identifier for each movie.
* title: Title of the movie.
* vote_average: Average rating of the movie.
* vote_count: Number of ratings.
* release_date: Release date of the movie.
* runtime: Duration of the movie in minutes.
* tags: Keywords or tags related to the movie.
