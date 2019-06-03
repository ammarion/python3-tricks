def make_album(artist_name, album_title, number=None):
    album = {
        "artist".title(): artist_name.title(), 
        "album".title(): album_title.title()
        }

    if number:
        album['number'.title()] = number
    return album

while True:
    print("\nPlease enter information: ")
    print("\nIf you want to quit type q")
    
    artist = input("artist name please: ")
    if artist == 'q':
        break

    album = input("album name please: ")
    if album == 'q':
        break


    three = make_album(artist, album, number=4)


    print(three)