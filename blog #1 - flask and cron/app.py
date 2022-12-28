from flask import Flask

import click
from click import echo

import psycopg2
import os
import requests
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='hashnode_movie_db',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn


@app.cli.command('get-movie-recommendations')
def get_movie_recommendations():
    
    # get Db connection
    conn = get_db_connection()
    
    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    # Clear the table completely
    cur.execute('DELETE FROM movie_schema.movierecommendation;')
    conn.commit()

    # Invoke TMDB API to fetch popular movies
    API_KEY = os.environ['TMDB_API_KEY']
    api = "https://api.themoviedb.org/3/movie/popular?api_key=" \
        + API_KEY + "&language=en-US&page=1"
    response = requests.get(f"{api}")

    # If success, then iterate through the reponse
    # fetch few fields, and insert them into the
    # database table
    if response.status_code == 200:
        response_json = response.json()
        for (k, v) in response_json.items():
            if k == 'results':
                for x in v:
                    id = 0
                    vote_average = 0.0
                    vote_count = 0
                    original_title = overview = ["" for i in range(2)]
                    for (y,z) in x.items():
                        if y == "id":
                            id = z
                        if y == "original_title":
                            original_title = str(z)
                        if y == "overview":
                            overview = str(z)
                        if y == "vote_average":
                            vote_average = z
                        if y == "vote_count":
                            vote_count = z
                        popular_movie = (id, original_title, overview, \
                            vote_average, vote_count)
                        cur.execute('INSERT INTO movie_schema.movierecommendation(id, \
                            original_title, overview, vote_average, vote_count) \
                                VALUES (%s, %s, %s, %s, %s)', popular_movie)
                        del popular_movie
                    
    else:
        return f"There was an error with code {response.status_code} while \
             fetching the movie details from TMDB"
    
    # For test purpose, fetch records from the table
    cur.execute('SELECT * FROM movie_schema.movierecommendation;')
    movies = cur.fetchall()
    cur.close()
    conn.close()
    # Print the output to screen
    click.echo(movies)
