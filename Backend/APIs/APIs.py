from collections import Counter
import spotipy.util as util
import spotipy

###############################################################

def GetMusicTaste(Username):
    # Username = "c6npu7845jgtvuo2864jxzpup" (Username-ul meu pt testing daca iti trb)
    Genres = ""
    Scope = "user-top-read"
    ClientID = 'f33ea24085634624b58c3622dedf563c'
    ClientSecret = 'af327494a245416baeb06580cf584350'
    RedirectURL = 'https://dexter0-0.github.io/'
    Spotify = spotipy.Spotify(auth = util.prompt_for_user_token(Username, Scope, ClientID, ClientSecret, RedirectURL))

    TopArtists = Spotify.current_user_top_artists()

    for i in range(len(TopArtists)):
        for j in range(len(TopArtists["items"][i]["genres"])):
            Genres = Genres + TopArtists["items"][i]["genres"][j] + ","

    Genres = Genres.split(",")
    return Counter(Genres)

###############################################################

def main():
    print(GetMusicTaste())


if __name__ == '__main__':
    main()
