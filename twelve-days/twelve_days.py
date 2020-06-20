def recite(start_verse, end_verse):
    ordinal_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
                       'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

    gifts = [' and a Partridge in a Pear Tree', ' two Turtle Doves', ' three French Hens', ' four Calling Birds', ' five Gold Rings', ' six Geese-a-Laying',
             ' seven Swans-a-Swimming', ' eight Maids-a-Milking', ' nine Ladies Dancing', ' ten Lords-a-Leaping', ' eleven Pipers Piping', ' twelve Drummers Drumming']

    lyrics = []
    for i in range(start_verse, end_verse + 1):
        if i == 1:
            end_of_verse = ' a Partridge in a Pear Tree'
        else:
            end_of_verse = ','.join(gifts[i - 1::-1])
        line = f'On the {ordinal_numbers[i-1]} day of Christmas my true love gave to me:{end_of_verse}.'
        lyrics.append(line)

    return lyrics
