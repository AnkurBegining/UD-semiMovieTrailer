import webbrowser


class Movie():
    """
    Here class object would store movie related information
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        :param movie_title:
        :param movie_storyline:
        :param poster_image:
        :param trailer_youtube:
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        this function is initializing instance to open the youtube video
        :return: Here this webbrowser would be used to open trailer
        """
        webbrowser.open(self.trailer_youtube_url)