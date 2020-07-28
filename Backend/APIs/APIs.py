from collections import Counter
from imdb import IMDb as MovieAPI
import spotipy.util as util
import spotipy

###############################################################

def GetUserToken(Username, RedirectLink):
    Scope = "user-top-read"
    ClientID = 'f33ea24085634624b58c3622dedf563c'
    ClientSecret = 'af327494a245416baeb06580cf584350'
    RedirectURL = 'https://dexter0-0.github.io/'

    File = open("RedirectLink.txt", "w+")
    File.write(RedirectLink)
    File.close()

    Spotify = spotipy.Spotify(auth=util.prompt_for_user_token(Username, Scope, ClientID, ClientSecret, RedirectURL))
    return Spotify


def GetMusicCompatibility(SpotifyUserOne, SpotifyUserTwo):
    MusicScore = 0
    GenresOne = ""
    GenresTwo = ""
    TopArtistsOne = SpotifyUserOne.current_user_top_artists()
    TopArtistsTwo = SpotifyUserTwo.current_user_top_artists()

    for i in range(len(TopArtistsOne)):
        for j in range(len(TopArtistsOne["items"][i]["genres"])):
            GenresOne = GenresOne + TopArtistsOne["items"][i]["genres"][j] + ","

    for i in range(len(TopArtistsTwo)):
        for j in range(len(TopArtistsTwo["items"][i]["genres"])):
            GenresTwo = GenresTwo + TopArtistsTwo["items"][i]["genres"][j] + ","

    GenresOne = GenresOne.split(",")
    GenresTwo = GenresTwo.split(",")

    for i in range(len(GenresOne)):
        for j in range(len(GenresTwo)):
            if GenresOne[i] == GenresTwo[j]:
                MusicScore = MusicScore + 1

    MusicScore = MusicScore / max(len(GenresOne), len(GenresTwo))
    return MusicScore

###############################################################

def GetMovieCompatibility(MoviesUserOne, MoviesUserTwo):
    MovieScore = 0
    GenresOne = ""
    GenresTwo = ""

    for i in range(len(MoviesUserOne)):
        MovieID = MovieAPI().search_movie(MoviesUserOne[i])[0].movieID
        GenresMovie = MovieAPI().get_movie(MovieID)["genres"]
        for j in range(len(GenresMovie)):
            GenresOne = GenresOne + GenresMovie[j] + ","

    for i in range(len(MoviesUserTwo)):
        MovieID = MovieAPI().search_movie(MoviesUserTwo[i])[0].movieID
        GenresMovie = MovieAPI().get_movie(MovieID)["genres"]
        for j in range(len(GenresMovie)):
            GenresTwo = GenresTwo + GenresMovie[j] + ","

    GenresOne = GenresOne.split(",")
    GenresTwo = GenresTwo.split(",")

    for i in range(len(GenresOne)):
        for j in range(len(GenresTwo)):
            if GenresOne[i] == GenresTwo[j]:
                MovieScore = MovieScore + 1

    MovieScore = MovieScore / max(len(GenresOne), len(GenresTwo))
    return MovieScore

###############################################################

def main():
    print(GetMusicCompatibility(GetUserToken("Dexter", ""), GetUserToken("Tudor", "")))

    MoviesUserOne = ["titanic", "the wizard of oz", "the lion king"]
    MoviesUserTwo = ["jurassic park", "fight club", "pulp fiction"]

    print(GetMovieCompatibility(MoviesUserOne, MoviesUserTwo))


if __name__ == '__main__':
    main()
