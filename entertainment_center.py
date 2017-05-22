import fresh_tomatoes
import movie

toy_story = movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = movie.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Post.jpg",
                        "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = movie.Movie("School of Rock",
                        "Using rock music to heart",
                        "http://upload.wikimedia.org/wikipedia/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = movie.Movie("Ratatouille",
                        "A rat is a chef in Paris",
                        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = movie.Movie("Midnight in Paris",
                        "Going back in time to meet authors",
                        "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=atLg2wQQxvU")


hunger_games = movie.Movie("Hunger Games",
                        "A really real reality show",
                        "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=9bA63a7H0bo")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)
print(movie.Movie.__doc__)
print(movie.Movie.__name__)
print(movie.Movie.__module__)
print(movie.Movie.__dict__)
print(movie.Movie.__bases__)


