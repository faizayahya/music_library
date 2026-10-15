class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_tracks(self, track):
        if not isinstance(track, str):
            raise Exception("Track must be string")
        if track == " ":
            raise Exception("Track cannot be empty")
        self.tracks.append(track)

    def list_tracks(self):
        return self.tracks