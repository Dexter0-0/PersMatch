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
    for i in range(len(MoviesUserOne)):
        MovieID = MovieAPI().search_movie(MoviesUserOne[i])[0]
        print(MovieID)

    for i in range(len(MoviesUserTwo)):
        Movie = MovieAPI().search_movie(MoviesUserTwo[i])[0]
        print(Movie)

###############################################################

def main():
    print(GetMusicCompatibility(GetUserToken("Dexter", ""), GetUserToken("Tudor", "")))
    MoviesUserOne = ["titanic", "the wizard of oz", "star wars 4", "the lion king", "the godfather"]
    MoviesUserTwo = ["jurassic park", "the dark knight", "jaws", "fight club", "pulp fiction"]
    GetMovieCompatibility(MoviesUserOne, MoviesUserTwo)


if __name__ == '__main__':
    main()
