import string
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
def alphabet_position(letter):
    #this returns the numerical position of a given letter
    char_value = ''
    for char in letter:
        if char in alphabet_lower:
            char_value = alphabet_lower.index(char)
        if char in alphabet_upper:
            char_value = alphabet_upper.index(char)
    return char_value

def rotate_character(char, rot):
    #this changes a character by rotating the character by a given amount
    if char not in string.ascii_letters:
        rot_char = char
        return rot_char
    orig_char = alphabet_position(char)
    new_char = orig_char + rot
    if new_char < 26:
        rot_char_ix = new_char
    if new_char > 26:
        rot_char_ix = new_char % 26
    if new_char == 26:
        rot_char_ix = 0
    if char in alphabet_lower:
        rot_char = alphabet_lower[rot_char_ix]
    if char in alphabet_upper:
        rot_char = alphabet_upper[rot_char_ix]
    return rot_char

def encrypt(text, rot):
    # this rotates the characters in a text to create an encrypted text
    encrypted = ''
    for i in text:
        encrypt_letter = rotate_character(i, rot)
        encrypted = encrypted + encrypt_letter
    return encrypted
