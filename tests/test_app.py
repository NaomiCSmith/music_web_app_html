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

"""
GET /albums
When: I submit a get request to albums in html
Then: I receive a list of all albums in the repository
"""
def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getalbums")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Title: Doolittle\nReleased: 1989",
        "Title: Surfer Rosa\nReleased: 1988",
        "Title: Waterloo\nReleased: 1974",
    ])

"""
GET /singlealbum
When: I submit a get request for a specific album in html
Then: I receive the details of that album
"""
def test_get_single_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getalbum/3")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Waterloo")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Release year: 1974")


"""
When: I visit the albums page
Then: I can click on a link to see more details about the album
"""

def test_show_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getalbums")
    page.click("text=Title: Waterloo")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Waterloo")


"""
GET /artists
When: I submit a get request to artists in html
Then: I receive a list of all artists in the repository
"""
def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getartists")
    div_tags = page.locator("div")
    expect(div_tags).to_have_text([
        "Name: Pixies",
        "Name: ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone"
    ])


"""
When: I visit the artists page
Then: I can click on a link to see more details about the artist
"""

def test_show_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getartists")
    page.click("text=Name: Taylor Swift")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Taylor Swift")

"""
When: I submit an album on /getalbums
Then: it is added to the repository
"""

def test_submit_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getalbums")
    page.click('text="Add a New Album:"')
    page.fill('input[name=title]', "English Rain")
    page.fill('input[name=release_year]', "2013")
    page.click('input[type=submit]')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "Title: Doolittle",
        "Title: Surfer Rosa",
        "Title: Waterloo",
        "Title: English Rain",
    ])


"""
When: I submit an artist on /getartists
Then: it is added to the repository
"""

def test_submit_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_web_app.sql")
    page.goto(f"http://{test_web_address}/getartists")
    page.click('text="Add a New Artist:"')
    page.fill('input[name=name]', "Gabrielle Aplin")
    page.fill('input[name=genre]', "Indie Pop")
    page.click('input[type=submit]')

    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "Name: Pixies",
        "Name: ABBA",
        "Name: Taylor Swift",
        "Name: Nina Simone",
        "Name: Gabrielle Aplin"
    ])