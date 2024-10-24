from lib.artist import Artist

"""
Artist constructs with an id, name and genre
"""
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Test Genre"

"""
We can format artists to strings nicely
"""
def test_artists_format_nicely():
    artist = Artist(1, "Test Artist", "Test Genre")
    assert str(artist) == "Artist(1, Test Artist, Test Genre)"
    
"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Artist", "Test Genre")
    artist2 = Artist(1, "Test Artist", "Test Genre")
    assert artist1 == artist2
 