import numpy as np
import pandas as pd
df=None
similarity=None

import warnings
warnings.filterwarnings("ignore")

def recommend(movie):
    l=[]
    try:
        indx=df[df['title']==movie.lower()].index[0]
        movie_list=sorted(list(enumerate(similarity[indx])), reverse=True, key=lambda x: x[1])[0:6]
        for i,_ in movie_list:
            l.append(df['title'].iloc[i])
        return l
    except IndexError:
        return ['Movie Not Found !!!']

def load_saved_movies():
    print("loading names start....")
    global df
    global similarity
    similarity = np.load('similarity.npy')
    df = pd.read_csv('movie.csv')
    print('------Loading data done ... 100 %------')