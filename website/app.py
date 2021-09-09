from flask import Flask, request, jsonify, render_template
import numpy as np
import json
import pandas as pd

app = Flask("MovieRecommender")

def clean_platforms(platform_list):
    for platform in platform_list:
        if platform == 'netflix':
            platform_list.remove(platform)
            platform_list.append('Netflix')
        elif platform == 'hulu':
            platform_list.remove(platform)
            platform_list.append('Hulu')
        elif platform == 'prime_video':
            platform_list.remove(platform)
            platform_list.append('Prime Video')
        elif platform == 'disney_plus':
            platform_list.remove(platform)
            platform_list.append('Disney+')
    return platform_list

def rec_data(rec_title):
    file = open('metadata.json')
    data = json.load(file)
    all_data = data['data']

    for rec in all_data:
        if rec['name'] == rec_title:
            rec_desc = rec['desc']
            rec_platform = rec['platforms']
            rec_platform = clean_platforms(rec_platform)
    return (rec_title,rec_desc,rec_platform)

@app.route('/')

def main_func():
    # Loading in Data
    file = open('metadata.json')
    data = json.load(file)
    all_data = data['data']

    # PART 1: Filling Out Genre/Select Movies Page

    examples_for_genre = {}
    while len(examples_for_genre) < 6:
        index = np.random.choice(len(all_data), replace=False)
        if all_data[index]['genre'] == 'Drama' or all_data[index]['sub_genre'] == 'Drama':
            examples_for_genre['Drama'] = all_data[index]['name']
        elif all_data[index]['genre'] == 'Comedy' or all_data[index]['sub_genre'] == 'Comedy':
            examples_for_genre['Comedy'] = all_data[index]['name']
        elif all_data[index]['genre'] == 'Action' or all_data[index]['sub_genre'] == 'Action':
            examples_for_genre['Action']=all_data[index]['name']
        elif all_data[index]['genre'] == 'Horror' or all_data[index]['sub_genre'] == 'Horror':
            examples_for_genre['Horror']=all_data[index]['name']
        elif all_data[index]['genre'] == 'Animation' or all_data[index]['sub_genre'] == 'Animation':
            examples_for_genre['Animation']=all_data[index]['name']
        elif all_data[index]['genre'] == 'Adventure' or all_data[index]['sub_genre'] == 'Adventure':
            examples_for_genre['Adventure']=all_data[index]['name']

    genres = {}

    for movie in all_data:
        if movie['name'] == examples_for_genre['Drama']:
            genres['drama'] = (movie['name'],movie['desc'])
        elif movie['name'] == examples_for_genre['Comedy']:
            genres['comedy'] = (movie['name'],movie['desc'])
        elif movie['name'] == examples_for_genre['Action']:
            genres['action'] = (movie['name'],movie['desc'])
        elif movie['name'] == examples_for_genre['Horror']:
            genres['horror'] = (movie['name'],movie['desc'])
        elif movie['name'] == examples_for_genre['Animation']:
            genres['animation'] = (movie['name'],movie['desc'])
        elif movie['name'] == examples_for_genre['Adventure']:
            genres['adventure'] = (movie['name'],movie['desc'])
    # END PART 1

    # PART 2: Filling Out Recommendations Tab
    recs = {}
    for movie in all_data:
        if movie['name'] == examples_for_genre['Drama']:
            rec_title = movie['recs'][0]
            recs['drama'] = rec_data(rec_title)
        elif movie['name'] == examples_for_genre['Comedy']:
            rec_title = movie['recs'][0]
            recs['comedy'] = rec_data(rec_title)
        elif movie['name'] == examples_for_genre['Action']:
            rec_title = movie['recs'][0]
            recs['action'] = rec_data(rec_title)
        elif movie['name'] == examples_for_genre['Horror']:
            rec_title = movie['recs'][0]
            recs['horror'] = rec_data(rec_title)
        elif movie['name'] == examples_for_genre['Animation']:
            rec_title = movie['recs'][0]
            recs['animation'] = rec_data(rec_title)
        elif movie['name'] == examples_for_genre['Adventure']:
            rec_title = movie['recs'][0]
            recs['adventure'] = rec_data(rec_title)

    return render_template("index.html",genres=genres,recs=recs)


if __name__ == "__main__":
    app.run(debug=True)
