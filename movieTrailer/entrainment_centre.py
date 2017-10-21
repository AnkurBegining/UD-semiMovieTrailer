from movieTrailer import media

toy_story = media.Movie("Toy Story",
                        "In a world where toys are living things"
                        " who pretend to be lifeless when humans are present, "
                        "a group of toys, owned by six-year-old Andy Davis, "
                        "are caught off-guard when Andy's birthday party is "
                        "moved up a week,"
                        " as Andy, his mother and infant sister Molly are "
                        "preparing to move the following week.",
                        "https: // en.wikipedia.org / wiki / Toy_Story  #/media/File:Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.story_line)

toy_story.show_trailer()
