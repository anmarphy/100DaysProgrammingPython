import string

user_action=input('Do you have a message? Type Yes or No')
if user_action=='Yes':
    should_continue = True
else:
    should_continue = False
    print('Good bye. See you soon')

while should_continue==True:
    alphabet = list(string.ascii_lowercase)
    action=input('Do you want to encode or decode the message?')
    message=input('Enter your message: ').lower()
    shift= int(input('Enter the secret shift: '))

    print(f'The message {message} will be {action} with a {shift} shift')


    def encode_decode(message, action, shift):
        new_alphabet = alphabet[shift:] + alphabet[0:shift]
        decode_alphabet=new_alphabet[-shift:]+new_alphabet[:-shift] ##Improve using -1

        if action=='decode':
            original_alphabet =new_alphabet
            final_alphabet =decode_alphabet
        elif action=='encode':
           original_alphabet = alphabet
           final_alphabet = new_alphabet

        original_index = []
        for i in message:
            original_index.append(original_alphabet.index(i))

        cipher_message = ''
        for ind in original_index:
            cipher_message += final_alphabet[ind]

        return print(f'The {action} message is: {cipher_message}')

    encode_decode(message=message, action=action, shift=shift)



