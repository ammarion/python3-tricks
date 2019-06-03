def make_album(artist_name, album_title, number=None):
    album = {
        "artist".title(): artist_name.title(), 
        "album".title(): album_title.title()
        }

    if number:
        album['number'.title()] = number
    return album






one = make_album('koko', 'wheels on the bus')
two = make_album('bobo', 'I losh you')
three = make_album('chu chu', 'handa', number=4)

print(one)
print(two)
print(three)