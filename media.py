import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
#    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #This function opens a web browsing tab to a specified url. The intent is
    #to play a trailer related to the movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
