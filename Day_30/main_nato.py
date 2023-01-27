import pandas as pd

#TODO 1. Create a dictionary in this format:
letters_dict=pd.read_csv('../Day_26/nato_phonetic_alphabet.csv').set_index('letter').to_dict()['code']

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def word_generation():
    new_word=input('Enter a word: ').upper()
    try:
        output = [letters_dict[letter] for letter in new_word]
    except KeyError:
        print('Sorry, only letter in the input please')
        word_generation()
    else:
        print(output)
        word_generation()

word_generation()





