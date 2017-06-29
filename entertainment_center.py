import media
import fresh_tomatoes

#Create all of the Movie objects and put them in a list.
dotd     = media.Movie("Dawn of the Dead",
                       "Survivors of a zombie apocalypse take refuge in a mall",
                       "https://upload.wikimedia.org/wikipedia/en/1/16/Dawn_of_the_Dead_2004_movie.jpg",
                       "https://www.youtube.com/watch?v=8LUzJAsa-gg")

rpa      = media.Movie("Rise of the Planet of the Apes",
                       "Medical experiments lead to intelligent apes.",
                       "https://upload.wikimedia.org/wikipedia/en/8/81/Rise_of_the_Planet_of_the_Apes_Poster.jpg",
                       "https://www.youtube.com/watch?v=EbCoDf44oCE")

gotg     = media.Movie("Guardians of the Galaxy",
                       "A band of miscreants teams up to take on a galactic villain.",
                       "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                       "https://www.youtube.com/watch?v=2LIQ2-PZBC8")

kickass  = media.Movie("Kick-Ass",
                       "A bored high school student decides to become a superhero.",
                       "https://upload.wikimedia.org/wikipedia/en/3/30/Kick-Ass_film_poster.jpg",
                       "https://www.youtube.com/watch?v=rFpWpkxsVI8")

speed    = media.Movie("Speed Racer",
                       "A young stunt racer named Speed changes the sport forever.",
                       "https://upload.wikimedia.org/wikipedia/en/8/82/Speed_racer_ver5_xlg.jpg",
                       "https://www.youtube.com/watch?v=8V8sLlqJB2w")

prestige = media.Movie("The Prestige",
                       "A pair of magicians enter into a rivalry that threatens to turn deadly.",
                       "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                       "https://www.youtube.com/watch?v=o4gHCmTQDVI")

movies = [dotd, gotg, speed, prestige, kickass, rpa]

#use the movies list to produce and open a webpage.
fresh_tomatoes.open_movies_page(movies)
