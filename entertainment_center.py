"""Stores details of movies and displays them on a website."""
import marvel
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    cm = media.Movie("Captain Marvel",
                          "MCU's most powerful superhero",
                          "https://stat.ameba.jp/user_images/20190108/19/jumbooomori/68/06/j/o0821120014335603368.jpg?caw=800",
                          "https://www.youtube.com/watch?v=0LHxvxdRnYc",
                          "March 8, 2019")

    ae = media.Movie("Avengers: EndGame",
                          "The Avengers take a final stand against Thanos",
                          "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg",
                          "https://www.youtube.com/watch?v=TcMBFSGVi1c",
                          "April 26, 2019")

    sm = media.Movie("Spider-Man: FFH",
                           "Following the events of Avengers: Endgame,",
                           "https://terrigen-cdn-dev.marvel.com/content/prod/1x/sffh_venice-high-res.jpg",
                           "https://www.youtube.com/watch?v=Nt9L1jCKGnE",
                           "July 5, 2019")

    aw = media.Movie("Ant-Man and the Wasp",
                     "Scott Lang is grappling with the consequences of his choices as both a superhero and a father",
                     "https://upload.wikimedia.org/wikipedia/en/2/2c/Ant-Man_and_the_Wasp_poster.jpg",
                     "https://www.youtube.com/watch?v=UUkn-enk2RU",
                     "July 6, 2018")

    aiw = media.Movie("Avengers: Infinity War",
                         "The Avengers must stop Thanos and his army from getting their hands on all the infinity stones",
                         "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                         "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                         "April 27, 2018")

    bp = media.Movie("Black Panther",
                           "After the death of his father, T'Challa returns home to Wakanda to take his place as king",
                           "https://i.pinimg.com/564x/a8/8e/fe/a88efe3ef511363615da28dbc0fb13dc.jpg",
                           "https://www.youtube.com/watch?v=xjDjIWPwcPU",
                           "February 16, 2018")

    tr = media.Movie("Thor: Ragnarok",
                          "Thor must escape the other side of the universe to save Asgard from Hela",
                          "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                          "https://www.youtube.com/watch?v=ue80QwXMRHg",
                          "November 3, 2017")

    shc = media.Movie("Spider-Man: Homecoming",
                      "Peter Parker tries to stop Adrian 'The Vulture' Toomes from selling weapons",
                      "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                      "https://www.youtube.com/watch?v=DiTECkLZ8HM",
                      "July 7, 2017")

    gg2 = media.Movie("Guardians of the Galaxy Vol. 2",
                     "Star-Lord and his team of galactic defenders meet Ego, a man claiming to be his father",
                     "https://upload.wikimedia.org/wikipedia/en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg",
                     "https://www.youtube.com/watch?v=wUn05hdkhjM",
                     "May 5, 2017")

    ds = media.Movie("Doctor Strange",
                      "Dr. Stephen Strange's life changes after a car accident robs him of the use of his hands",
                      "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                      "https://www.youtube.com/watch?v=HSzx-zryEgM",
                      "November 4, 2016")

    cacv = media.Movie("Captain America: CW",
                      "Factions of superheroes divide themselves in to Team Captain America and Team Stark",
                      "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                      "https://www.youtube.com/watch?v=dKrVegVI0Us",
                      "May 6, 2016")

    am = media.Movie("Ant-Man",
                     "Criminal Scott gains the ability to shrink in scale with the help of a futuristic suit",
                     "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
                     "https://www.youtube.com/watch?v=pWdKf3MneyI",
                     "July 17, 2015")

    aou = media.Movie("Avengers: Age of Ultron",
                       "Tony Stark builds an artificial intelligence system named Ultron with the help of Bruce Banner",
                       "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg",
                       "https://www.youtube.com/watch?v=tmeOjFno6Do",
                       "May 1, 2015")

    gg = media.Movie("Guardians of the Galaxy",
                     "Peter escapes from the planet Morag with a valuable orb that Ronan the Accuser wants",
                     "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",
                     "https://www.youtube.com/watch?v=2LIQ2-PZBC8",
                     "August 1, 2014")

    caws = media.Movie("Captain America: TWS",
                       "Steve Rogers, along with Black Widow and Falcon, must uncover the secrets hidden within S.H.I.E.L.D",
                       "https://www.movienewsletters.net/photos/181326R1.jpg",
                       "https://www.youtube.com/watch?v=7SlILk2WMTI",
                       "April 4, 2014")

    tdw = media.Movie("Thor: The Dark World",
                     "Malekith returns to take a weapon from Asgard in order to force the Nine Realms into darkness",
                     "https://upload.wikimedia.org/wikipedia/en/7/7f/Thor_The_Dark_World_poster.jpg",
                     "https://www.youtube.com/watch?v=npvJ9FTgZbM",
                     "November 8, 2013")

    im3 = media.Movie("Iron Man 3",
                      "Tony Stark encounters a formidable foe called the Mandarin",
                      "https://upload.wikimedia.org/wikipedia/en/1/19/Iron_Man_3_poster.jpg",
                      "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc",
                      "May 3, 2013")

    ma = media.Movie("Marvel's The Avengers",
                      "When Loki gains access to the unlimited power of Tesseract, Nick Fury initiates a superhero recruitment effort to defeat the unprecedented threat to Earth",
                      "https://upload.wikimedia.org/wikipedia/en/8/8a/The_Avengers_%282012_film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                      "May 4, 2012")

    ca = media.Movie("Captain America: TFA",
                      "After Steve Rogers decides to volunteer in an experiment, his weak body is fully enhanced",
                      "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
                      "https://www.youtube.com/watch?v=JerVrbLldXw",
                      "July 27, 2011")

    th = media.Movie("Thor",
                     "Thor is exiled by his father, Odin to the Earth to live among mortals",
                     "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
                     "https://www.youtube.com/watch?v=JOddp-nlNvQ",
                     "May 6, 2011")

    im2 = media.Movie("Iron Man 2",
                     "Tony Stark is under pressure from various organizations to share his technology with the world",
                     "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                     "https://www.youtube.com/watch?v=BoohRoVA9WQ",
                     "May 7, 2010")

    tih = media.Movie("The Incredible Hulk",
                     "Dr Bruce Banner subjects himself to high levels of gamma radiation which transforms him into a huge green creature, the Hulk",
                     "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
                     "https://www.youtube.com/watch?v=xbqNb2PFKKA",
                     "June 13, 2008")

    im = media.Movie("Iron Man",
                      "When an industrialist is captured, he constructs a high-tech armoured suit to escape. Later he decides to use his suit to save the world",
                      "https://upload.wikimedia.org/wikipedia/en/0/00/Iron_Man_poster.jpg",
                      "https://www.youtube.com/watch?v=8hYlB38asDY",
                      "May 2, 2008")

    # Store the Movie objects in a list.
    movies = [sm, ae, cm, aw, aiw, bp, tr, shc, gg2, ds, cacv, am, aou, gg, caws, tdw, im3, ma, ca, th, im2, tih, im]

    # Open the movie website in the user's browser, featuring the movies above.
    marvel.open_movies_page(movies)

if __name__ == '__main__':
    main()