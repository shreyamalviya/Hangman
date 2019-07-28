from collections import OrderedDict

GAME_WORDS = ['ability', 'about', 'above', 'absolute', 'accessible',
              'accommodation', 'accounting', 'ambassador', 'anniversary',
              'appointment', 'awkward', 'bagpipes', 'beautiful', 'birthday',
              'bookstore', 'brand', 'calculator', 'circumstance', 'clever',
              'confused', 'congratulate', 'dangerous', 'decrease', 'development',
              'dictionary', 'dwarves', 'earthquake', 'engaged', 'engineer',
              'enough', 'entertainment', 'environment', 'environment', 'exhausted',
              'frequent', 'gypsy', 'handsome', 'haphazard', 'hyphen', 'impossible',
              'information', 'interested', 'ivory', 'jukebox', 'luggage',
              'mathematics', 'memento', 'mystify', 'necessary', 'opposite',
              'overweight', 'oxygen', 'perhaps', 'pixel', 'possible',
              'refrigerator', 'responsible', 'rhythmic', 'rogue', 'scissors',
              'sphinx', 'strawberry', 'temperature', 'twelfth', 'vacation', 'yacht',
              'xylophone', 'zealous', 'zombie']

MESSAGES = OrderedDict([
    ('NEXT', {
        'msg': "What's your next guess?",
        # 'play': True,
    }),
    ('ALREADY_GUESSED', {
        'msg': "You can't guess a letter that you've guessed before. Try again.",
        # 'play': 
    }),
    ('INVALID', {
        'msg': "Invalid guess. Try again."
    }),
    ('CORRECT', {
        'msg': "Good guess!"
    }),
    ('INCORRECT', {
        'msg': "Oops... That letter isn't in this word."
    }),
    ('GAME_OVER', {
        'msg': "Oh no! You couldn't guess the word in time.\nGame over!"
    })
])

IMG_PATH = {
    0:  'images/hangman-0.png',
    1:  'images/hangman-1.png',
    2:  'images/hangman-2.png',
    3:  'images/hangman-3.png',
    4:  'images/hangman-4.png',
    5:  'images/hangman-5.png',
    # 6:  'images/hangman-6.png',
    6: 'images/game_over.png'
}
