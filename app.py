import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from lib.artist_repository import *
from lib.artist import *
from flask import Flask, request, render_template

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# Request:
# POST /albums
# With body parameters: title=Voyage, release_year=2022, artist_id=2
# Expected response (200 OK)

@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    repository.create(album)
    return "", 200



# Request:
# GET /artists
#  with body parameter: none
# Expected response (200 OK) - Pixies, ABBA, Taylor Swift, Nina Simone

@app.route('/artists', methods=['GET'])
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return (", ".join(artist.name for artist in repository.all()))

# Request:
# POST /artists
# With body parameters: name=Wild nothing, genre=Indie
# Expected response (200 OK)
# Then subsequent request:
# GET /artists
# Expected response (200 OK) - Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

@app.route('/artists', methods=['POST', 'GET'])
def post_artist_and_return_all_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = Artist(None, request.form['name'], request.form['genre'])
    artist_repository.create(artist)
    return (", ".join(artist.name for artist in artist_repository.all()))



# Request:
# /GET albums with html

@app.route('/getalbums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)









# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


