from lib.album_repository import AlbumRepository
from lib.album import Album

# when we call all, we get all the albums in the database

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
]
    
# when we call find with an id, we get one specific album back

def test_find_an_album(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    result = repository.find(3)
    assert result == Album(3, 'Waterloo', 1974, 2)


