import trailer_library
import media

the_jungle_book = media.Movie("The Jungle Book",
                              "After a threat from the tiger Shere Khan forces"
                              " him to flee the jungle, a man-cub named Mowgli"
                              " embarks on a journey of self discovery with"
                              " help of panther, Bagheera, and free spirited"
                              " bear, Baloo.",
                              "https://upload.wikimedia.org/wikipedia/en/a/a4/"
                              "The_Jungle_Book_%282016%29.jpg",
                              "https://www.youtube.com/watch?v=C4qgAaxB_pc",
                              "15 April 2016", "Jon Favreau", "Drama",
                              "English", 106, "PG")

superman_vs_batman = media.Movie("Batman v Superman",
                                 "Fearing that the actions of Superman are"
                                 " left unchecked, Batman takes on the Man of"
                                 " Steel, while the world wrestles with what"
                                 " kind of a hero it really needs.",
                                 "https://upload.wikimedia.org/wikipedia/en/"
                                 "2/20/Batman_v_Superman_poster.jpg",
                                 "https://www.youtube.com/watch?v=0WWzgGyAH6Y",
                                 "March 19, 2016", "Zack Snyder", "Sci-Fi",
                                 "English", 151, "PG-13")

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency recruits some of the"
                            " most dangerous incarcerated super-villains to"
                            " form a defensive task force. Their first mission"
                            ": save the world from the apocalypse.",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/"
                            "Suicide_Squad_%28film%29_Poster.png",
                            "https://www.youtube.com/watch?v=CmRih_VtVAs",
                            "5 August 2016", "David Ayer", "Sci-Fi",
                            "English", 123, "PG-15")

the_martian = media.Movie("The Martian",
                          "An astronaut becomes stranded on Mars after his"
                          " team assume him dead, and must rely on his"
                          " ingenuity to find a way to signal to Earth that"
                          " he is alive.",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/"
                          "The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8",
                          "30 September 2015", "Ridley Scott", "Drama",
                          "English", 141, "PG")

despicable_me = media.Movie("Despicable Me",
                            "When a criminal mastermind uses a trio of orphan"
                            " girls as pawns for a grand scheme, he finds"
                            " their love is profoundly changing him for the"
                            " better.",
                            "https://upload.wikimedia.org/wikipedia/en/d/db/"
                            "Despicable_Me_Poster.jpg",
                            "https://www.youtube.com/watch?v=sUkZFetWYY0",
                            "15 October 2010", "Chris Renaud", "Animation",
                            "English", 95, "U")

spectre = media.Movie("Spectre",
                      "A cryptic message from Bond's past sends him on a trail"
                      " to uncover a sinister organization. While M battles"
                      " political forces to keep the secret service alive,"
                      " Bond peels back the layers of deceit to reveal the"
                      " terrible truth behind SPECTRE.",
                      "https://images-na.ssl-images-amazon.com/images/M/"
                      "MV5BMjM2Nzg4MzkwOF5BMl5BanBnXkFtZTgwNzA0OTE3NjE"
                      "@._V1_QL50_.jpg",
                      "https://www.youtube.com/watch?v=z4UDNzXD3qA",
                      "26 October 2015", "Sam Mendes", "Thriller",
                      "English", 148, "12A")


# Create the list of all the Movie class instance
movies = [the_jungle_book, superman_vs_batman, suicide_squad, the_martian]
movies.append(despicable_me)
movies.append(spectre)

# Generate and display the output page in browser
trailer_library.open_movies_page(movies)
