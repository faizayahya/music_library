class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_tracks(self, track):
        if track == " ":
            raise Exception("Track cannot be empty")
        self.tracks.append(track)

    def list_tracks(self):
        return self.tracks

