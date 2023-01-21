import pandas as pd

#TODO 1. Create a dictionary in this format:
letters_dict=pd.read_csv('nato_phonetic_alphabet.csv').set_index('letter').to_dict()['code']

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
new_word=input('Enter a word: ').upper()

output=[letters_dict[letter] for letter in new_word]
print(output)


