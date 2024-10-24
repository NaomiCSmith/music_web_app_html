from lib.album import *

# album class constructs with:
#             id, title, release_year, and genre

def test_class_album_constructs():
    album = Album(1, "English Rain", 2013, 3)
    assert album.id == 1
    assert album.title == "English Rain"
    assert album.release_year == 2013
    assert album.artist_id == 3

# when I add two entries of the same album, they are equal

def test_equality():
    album_1 = Album(1, 'Doolittle', 1989, 1)
    album_2 = Album(1, 'Doolittle', 1989, 1)
    assert album_1 == album_2


