# Capstone Project: Movie Recommender System (My Movies)
by Nati Marcus

## Problem Statement
All major TV and movie streaming platforms today have their own recommendations built into their software. However, each streaming service is only able to recommend whichever movies are currently on its respective platform.  To solve this problem, I will build a recommender system model for movies on Netflix, Hulu, Amazon Prime Video, and Disney+ to predict which movies to recommend to a user in one location. I will use movie description, actors, genre, and director data to compare movies. The model will be evaluated based on the cosine similarity scores between titles in the dataset. 

## Data Overview
The original dataset was downloaded from <a href="https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney" target="_blank">Kaggle.</a> Features in this dataset included movie title, year made, age rating, director(s), genres, language(s), country, movie length in minutes, whether it was on Netflix, Hulu, Amazon Prime Video, or Disney+, IMDB rating, and Rotten Tomatoes scores. However, I intended on enhancing the data by scraping relevant content from IMDB, such as Rotten Tomatoes audience scores, movie description, and actor data. 

## Data Collection
Initially, I had sought to utilize rotten tomatoes scores in the modeling process. Accordingly, I scrapped audience scores from Rotten Tomatoes for most of the movies in the Kaggle dataset. Additionally, as I pivoted to focus more on text-based features, I decided to scrape movie descriptions and cast data from IMDB for around half of the movies in the Kaggle dataset. I had also intended on scraping streaming links for each of the movies from Google, however time constraints did not allow for this.

## Data Dictionary
|Feature|Type|Dataset|Description|
|----|----|----|----|
|**desc**|*object*|Final Dataset with Webscraped Data|IMDB movie description for each movie.|
|**lead_actor**|*object*|Final Dataset with Webscraped Data|The top actor on the IMDB cast & crew page for each movie.|
|**directors_ordinal**|*integer*|Final Dataset with Webscraped Data|Rank for each director based on how often they appear in the dataset.|
|**top_genre**|*object*|Final Dataset with Webscraped Data|The first genre listed in the genres column of the original dataset from Kaggle.|
  
## Analysis Overview
For the modeling process, I created a sparse matrix based on CountVectorized data from movie description, lead actor, and top genre, and then concatenated director rank data to the matrix. Using this matrix, I calculated the cosine similarities for each of the movies in the dataset. Scores improved significantly from the original model based solely on movie description. For one movie title, the cosine similarity scores went from maxing out at 0.3 to around 0.94.

## App Development
To showcase the modeling process, I developed an application called My Movies using Flask and a template from free-css.com. The site contains a page with a random sample of six movies from six different genres for movie preferences on which to make predictions. The subsequent page contains the top recommendation for each of these six movies as well as its description and where to stream this movie.

## Conclusions
With fairly high cosine similarity scores, the model I constructed serves as a solid system for movie recommendations for movies on Netflix, Hulu, Amazon Prime Video, and Disney+.
