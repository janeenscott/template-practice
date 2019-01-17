import csv

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)




@app.route("/")
def index():

    all_songs = [
        {'title': "Postcards",
         'lyrics': "Now you're sending me postcards from home, pictures of the places that I know.",
         'composer': "Janeen Scott"},
        {'title': "Been Here Before",
         'lyrics': "Your skin looks foreign, but I imagine it would feel like an old map.",
         'composer': "Janeen Scott"},
        {'title': "Barcelona",
         'lyrics': "So we laughed at the guidebooks, and rewrote the pages",
         'composer': "Janeen Scott"},
        {'title': "Settle My Heart",
         'lyrics': "How can my weary heart love a world on fire?",
         'composer': "Janeen Scott"}
        ]

    return render_template('index.html', song_list=all_songs)
                                        # song_list=all_songs is defining the variable,
                                        # song_list for use in my index.html file. song_list
                                        # is now a list of dictionaries, containing all the
                                        # information that is listed above in all_songs.
    # return render_template is saying "look in index.html and use the information stored in
    # song_lists to fill in the requests in the html.


@app.route("/postcards/")
def postcards():

    all_songs = [
        {'title': "Postcards",
         'lyrics': "Now you're sending me postcards from home, pictures of the places that I know.",
         'composer': "Janeen Scott"},
        {'title': "Been Here Before",
         'lyrics': "Your skin looks foreign, but I imagine it would feel like an old map.",
         'composer': "Janeen Scott"},
        {'title': "Barcelona",
         'lyrics': "So we laughed at the guidebooks, and rewrote the pages",
         'composer': "Janeen Scott"},
        {'title': "Settle My Heart",
         'lyrics': "How can my weary heart love a world on fire?",
         'composer': "Janeen Scott"}
    ]
    return render_template('postcards.html', song_list=all_songs)

@app.route("/been-here-before/")
def been_here_before():
    pass

@app.route("/barcelona/")
def barcelona():
    pass

@app.route("/settle-my-heart/")
def settle_my_heart():
    pass



