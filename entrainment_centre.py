import media
import fresh_tomatoes

# Creating movies to describe the instances of the Class Movie
the_shawshank = media.Movie(
    "The Shawshank Redemption",
    """the film tells the story of Andy Dufresne a banker who is 
    sentenced to life in Shawshank State for the murder of his
    wife and her lover""",
    "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=NmzuHjWmXOc")


avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/"
    "id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

The_Last_Samurai = media.Movie(
    "The Last Samurai",
    """Tom Cruise portrays a formerly retired officer
    of the United States 7th Cavalry Regiment whose personal
    and emotional conflicts bring him into contact with 
    samurai warriors in the wake of the Meiji Restoration in 
    19th Century Japan.""",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",  # noqa
    "https://www.youtube.com/watch?v=RdS6FgmO4j8")

ms_dhoni = media.Movie(
    "Ms Dhoni",
    """Untold story of India's most successful
    captain of cricket team""",
    "https://upload.wikimedia.org/wikipedia/en/3/33/M.S._Dhoni_-_The_Untold_Story_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=6L6XqWoS8tw")

vanilla_sky = media.Movie(
    "Vanilla Sky",
    "About a mightnight in Paris",
    "https://upload.wikimedia.org/wikipedia/en/9/9b/Vanilla_sky_post.jpg",  # noqa
    "https://www.youtube.com/watch?v=k09OX40NLUw&t=27s")

yah_jawani_hai_dewani = media.Movie(
    "Yah Jawani Hai Diwani",
    "Story of four friend",
    "https://upload.wikimedia.org/wikipedia/en/1/15/Yeh_jawani_hai_deewani.jpg",  # noqa
    "https://www.youtube.com/watch?v=Rbp2XUSeUNE")

"""
Movies array, contains the list of movies as input, which
is passed to the function "open_movies_page". This function
translates this list into a web page when we run the
entertainment_center.py" file.
"""

movies = [ms_dhoni,
          avatar,
          The_Last_Samurai,
          the_shawshank,
          vanilla_sky,
          yah_jawani_hai_dewani]

fresh_tomatoes.open_movies_page(movies)
