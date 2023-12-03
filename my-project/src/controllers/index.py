from ..getyoutube import get_youtube_data

class YoutubeController:
    def __init__(self):
        self.data = None

    def fetch_data(self):
        self.data = get_youtube_data()

    def get_data(self):
        if not self.data:
            self.fetch_data()
        return self.data