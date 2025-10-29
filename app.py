import streamlit as st
import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors

with open("movies.pkl", "rb") as f:
    movies_list = pickle.load(f)

with open("similarity.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

with open("nn.pkl", "rb") as f:
    nn= pickle.load(f)

movie_titles=movies_list['title'].values
new_movies=movies_list

def recommend(title, k=3):
  if title not in new_movies['title'].values:
    print(f"{title} not present in database.")
  idx=int(new_movies[new_movies['title']==title].index[0])
  vector=tfidf_matrix[idx].reshape(1,-1)
  distance, indices=nn.kneighbors(vector, n_neighbors=k+1)
  distance=distance.flatten()
  indices=indices.flatten()
  results=[]
  for dist, i in zip(distance[1:], indices[1:]):
    results.append({
        'title':new_movies.iloc[i]['title'],
        'movie_id':new_movies.iloc[i]['movie_id'],
        'score_cosine_similarity': 1-dist
    })
  return results



st.title("Movie Recommendation System")

selected_movie=st.selectbox("Enter any type of movie you recently liked.", movie_titles)
if st.button('Recommend'):
    L=recommend(selected_movie, k=5)
    for r in L:
        st.write(r['title'])
if st.button('Clear Search'):
    st.rerun()
