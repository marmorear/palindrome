import re
from unicodedata import normalize


def slugfy(word):
    return re.sub('[^a-zA-Z0-9]+', '', normalize(
        'NFKD', word).encode('ASCII', 'ignore').decode('ASCII')).lower()


def valid_palindrome(word):
    if valid_null(word):
        word = re.sub('\s+', '', word)
        text = word == word[::-1] or slugfy(word) and slugfy(word) == slugfy(word)[::-1]
        if text:
            return 'É palindrome!!!'
        else:
            return 'Não é palindrome! :('
    return 'Nada para validar!'


def valid_null(word):
    if word == "" or word.isspace():
        return False
    return True
