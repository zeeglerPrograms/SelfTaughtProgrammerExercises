#ChapterFiveExercises

#create a list of your favorite musicians
goats = ['beatles', 'prince', 'bill evans', 'johnny cash', 'nirvana']
for goat in goats:
    print(goat)

#create a list of tuples, of longitudes and latitutes youve visited
bigList = [(30.4249, 95.4799), (37.7749, 122.4194), (33.2148, 97.1331)]
for coordinate in bigList:
    print(coordinate)

#create a dictionary that contains different attributes about you: height, fave color, fave instrument
my_attributes = {'height':'6 feet', 'faveColor':'blue', 'faveInstrument':'too hard to choose'}

print("Type 'height' to know my height. Type 'faveColor' to know my favorite color. type 'faveInstrument' to know my favorite instrument.")
choice = input("Your choice: ")
print(my_attributes[choice])

#create a dictionary mapping your favorite artist to a list of songs by them
billEvansSongs = ['When I fall In Love', 'Blue In Green', 'Autumn Leaves']
beatlesSongs = ['Let It Be', 'Imagine', 'Dont Let Me Down']
princeSongs = ['Wanna Be Ur Lover', 'Kiss', 'Purpe Rain']
artistSongDict = {}
for song in billEvansSongs:
    artistSongDict = {'billEvans':song}
for song in beatlesSongs:
    artistSongDict = {'beatles':song}
for song in princeSongs:
    artistSongDict = {'prince':song}