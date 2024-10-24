from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

# Tests for your routes go here

"""
POST /albums
When: I add an album to albums
Then: The new album is added and nothing is returned
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post("/albums", data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

"""
GET /artists
When: I submit a get request to artists
Then: I receive a list of all artists' names in the repository
"""
def test_get_all_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == 'Pixies, ABBA, Taylor Swift, Nina Simone'

"""
POST /artists
When: I add an artist to artists
Then: I receive a list of artists' names with my new artist added on the end
"""
def test_post_artist_and_return_all_artists(web_client):
    response = web_client.post("/artists", data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    second_response = web_client.get("/artists")
    assert second_response.status_code == 200
    assert second_response.data.decode("utf-8") == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing'