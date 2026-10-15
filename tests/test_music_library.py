import pytest
from lib.music_library import MusicLibrary


def test_error_empty_track():
    library = MusicLibrary()
    with pytest.raises(Exception) as err:
        library.add_tracks(" ")
    assert str(err.value) == "Track cannot be empty"


def test_starts_empty_list():
    library = MusicLibrary()
    assert library.list_tracks() == []

def test_add_track():
    library = MusicLibrary()
    library.add_tracks("Halo")
    assert library.list_tracks() == ["Halo"]


def test_multiple_tracks():
    library = MusicLibrary()
    library.add_tracks("Halo")
    library.add_tracks("Say my name")
    library.add_tracks("Thriller")
    assert library.list_tracks() == ["Halo", "Say my name", "Thriller"]