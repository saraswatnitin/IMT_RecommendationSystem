from flask import Flask, request, jsonify
import utils


import warnings
warnings.filterwarnings("ignore")

app=Flask(__name__,template_folder='./client')

@app.route('/')
def admin():
    return "This is a Flask based app  for Content Based Recommendation System"

@app.route('/recommend_movie',methods=['GET','POST'])
def recommend():
    movie=request.form['movie']
    response_back_list = utils.recommend(movie)
    response = jsonify({
        'recomendations': response_back_list
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response



if __name__ =="__main__":
    utils.load_saved_movies()
    print("starting python flask")
    app.run()