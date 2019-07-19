import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story 4", 
                        "The fourth installment in the Toy Story series, which is the story a boy and his toys that come to life", 
                        "https://upload.wikimedia.org/wikipedia/en/4/4c/Toy_Story_4_poster.jpg",
                        "https://www.youtube.com/watch?v=wmiIUN-7qhE")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=6ziBFh3V1aM")
#print(avatar.storyline)
#avatar.show_trailer()

afewgoodmen = media.Movie("A Few Good Men",
                          "A legal drama about the blinding adherence to code and honor by US marines",
                          "https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
                          "https://www.youtube.com/watch?v=ePo91pMcu94")

#afewgoodmen.show_trailer()

schoolofrock = media.Movie("School of Rock",
                          "Using rock music to learn",
                          "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                          "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnightinparis = media.Movie("Midnight in Paris",
                              "Going back in time to meet authors",
                              "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                              "https://www.youtube.com/watch?v=FAfR8omt-CY")

hungergames = media.Movie("Hunger Games",
                          "A really real reality show",
                          "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=4S9a5V9ODuY")

shawshank = media.Movie("Shawshank Redemption",
                        "Escaping maximum security prison like a boss",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

darknightrises = media.Movie("Dark Night Rises",
                             "Best (Batman) movie ever",
                             "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                             "https://www.youtube.com/watch?v=g8evyE9TuYk")

movies = [toy_story, avatar, afewgoodmen, schoolofrock, ratatouille, midnightinparis, hungergames, shawshank, darknightrises]
fresh_tomatoes.open_movies_page(movies)

