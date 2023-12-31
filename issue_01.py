"""Morse Code Translator"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе

    >>> encode('SOS')
    '... --- ...'
    >>> encode('python') # doctest: +SKIP
    '.--. -.-- - .... --- -.'
    >>> encode(22222222222222)
    Traceback (most recent call last):
        ...
    ValueError: Входной текст должен быть строкой
    >>> encode(('yes', 'no'))
    Traceback (most recent call last):
        ...
    ValueError: Входной текст должен быть строкой
    """
    if not isinstance(message, str):
        raise ValueError('Входной текст должен быть строкой')

    upper_message = message.upper()

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in upper_message
    ]

    return ' '.join(encoded_signs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True, optionflags=doctest.NORMALIZE_WHITESPACE)
