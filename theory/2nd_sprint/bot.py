import random

bot_answers = {
    'How are you?': ['I am fine', 'It\'s OK', 'Not so good'],
    'What is the weather?': ['It is sunny', 'It is very cold', 'I was not on the street'],
    'What is your name?': ['I am a Tima-bot', 'LJhgjhlkjhk', 'I am your computer, dummy'],
    'Bye!': ['Good luck', 'Go away bastard!', 'Whats a pity'],
}
question = ''

while question != 'Bye!':
    try:
        question = input('Man:')
        print('Bot:', bot_answers[question][random.randint(0, 2)])
    except KeyError:
        print('I don\' understand you')
