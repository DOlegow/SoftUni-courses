number_of_pieces = int(input())
collection = {}

# create s dictionary with piece of music
for p in range ( number_of_pieces ):
    piece_of_music = input().split('|')
    collection[piece_of_music[0]] = [piece_of_music[1], piece_of_music[2]]

# performing commands
while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split ( '|' )
    if command[0] == 'Add':
        if command[1] in collection:
            print ( f"{command[1]} is already in the collection!" )
        else:
            collection[command[1]] = [command[2], command[3]]
            print ( f"{command[1]} by {command[2]} in {command[3]} added to the collection!" )

    elif command[0] == 'Remove':
        if command[1] in collection:
            del collection[command[1]]
            print ( f"Successfully removed {command[1]}!" )
        else:
            print ( f"Invalid operation! {command[1]} does not exist in the collection." )

    elif command[0] == 'ChangeKey':
        if command[1] in collection:
            collection[command[1]][1] = command[2]
            print ( f"Changed the key of {command[1]} to {command[2]}!" )
        else:
            print ( f"Invalid operation! {command[1]} does not exist in the collection." )

# print the music collection data
for piece, composer_scale in collection.items():
    composer = composer_scale[0]
    key = composer_scale[1]

    print ( f"{piece} -> Composer: {composer}, Key: {key}")
