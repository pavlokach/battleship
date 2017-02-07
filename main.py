# My data type is tuple of two lists.
# First list contains unshooted cells.
# Second contains shooted cells.
# Also you can see two fields: field.txt is correct,
# fail_field.txt is incorrect.
import string
alphabet = string.ascii_uppercase


def read_field(fname):
    '''

    (str) -> (data)

    Takes file name and returns data.
    '''
    import string
    alphabet = string.ascii_uppercase
    stars = []
    shots = []
    lines = []
    with open(fname, encoding='UTF-8') as field:
        for line in field:
            lines.append(line)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                stars.append((alphabet[j], i + 1))
            if lines[i][j] == 'X':
                shots.append((alphabet[j], i + 1, False))
    return (stars, shots)


def has_ship(data, coords):
    '''

    (data, list) -> (bool)

     Returns True if coords in data else False.
    '''
    return True if coords in data[0] or coords in data[1] else False


def ship_size(data, coords):
    '''

    (data, list) -> (int/False)

    Returns False if coordinates aren`t in field else returns ship size.
    '''
    stars = data[0] + data[1]
    if has_ship(data, coords) is False:
        return False
    ver, hor = False, False
    size = 1
    fine = []
    coords = list(coords)
    for star in stars:
        if star[0] == coords[0] or star[1] == coords[1]:
            fine.append(star)
    if (coords[0], coords[1] + 1) in fine \
       or (coords[0], coords[1] - 1) in fine:
        ver = True
    else:
        hor = True
    if ver is True:
        num = coords[1]
        while (coords[0], num) in fine:
            size += 1
            num += 1
        num = coords[1]
        while (coords[0], num) in fine:
            size += 1
            num -= 1
        return size - 2
    elif hor is True:
        num = coords[0]
        while (num, coords[1]) in fine:
            size += 1
            num = alphabet[alphabet.index(num) + 1]
        num = coords[0]
        while (num, coords[1]) in fine:
            size += 1
            num = alphabet[alphabet.index(num) - 1]
        return size - 2


def touch_check(data, coords):
    '''
    
    (data, list) -> (bool)
    
    Being used in is_valid(data) to ckeck if two ships aren`t touching.
    '''
    stars = data[0] + data[1]
    hor, ver = False, False
    if (coords[0], coords[1] + 1) in stars \
       or (coords[0], coords[1] - 1) in stars:
        ver = True
    if (alphabet[alphabet.index(coords[0]) + 1], coords[1]) in stars \
       or (alphabet[alphabet.index(coords[0]) - 1], coords[1]) in stars:
        hor = True
    if hor is True and ver is True:
        return False
    if (alphabet[alphabet.index(coords[0]) + 1], coords[1] + 1) in stars \
       or (alphabet[alphabet.index(coords[0]) + 1], coords[1] - 1) in stars:
        return False
    else:
        return True


def is_valid(data):
    '''
    
    (data) -> (bool)
    
    Checks if field is valid to play.
    '''
    stars = data[0] + data[1]
    ships_len = []
    if len(stars) != 20:
        return False
    for star in stars:
        ships_len.append(ship_size(data, star))
    if ships_len.count(2) != 6 or ships_len.count(1) != 4 \
       or ships_len.count(3) != 6 or ships_len.count(4) != 4:
        return False
    for star in stars:
        if touch_check(data, star) is False:
            return False
    return True
