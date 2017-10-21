import webbrowser

class Movie():
    def __init__(self, movie_title, story_line, movie_poster_url, movie_trailer_url):
        self.movie_title = movie_title
        self.story_line = story_line
        self.movie_poster_url = movie_poster_url
        self.movie_trailer_url = movie_trailer_url

    def show_trailer(self):
        webbrowser.open(self.movie_trailer_url)
