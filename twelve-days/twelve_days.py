ORDINALS = ['first', 'second', 'third', 'fourth', 'fifth',
            'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

GIFTS = ['and a Partridge in a Pear Tree', 'two Turtle Doves', 'three French Hens', 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying',
         'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']


def recite(start_verse, end_verse):
    return [verse(i) for i in range(start_verse, end_verse + 1)]


def verse(verse_num):
    if verse_num == 1:
        end_of_verse = 'a Partridge in a Pear Tree'
    else:
        end_of_verse = ', '.join(GIFTS[verse_num - 1::-1])

    return f'On the {ORDINALS[verse_num-1]} day of Christmas my true love gave to me: {end_of_verse}.'
