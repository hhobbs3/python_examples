import re

def generate_pig_latin_word(word):
    """
    Takes a word and converts it into a pig latin word
    :param word: str - word to be converted
    :return: str - pig latin-ized word
    """
    vowel = 'aeiou'
    if word[0].isalpha():
        # check for lowercase vowel
        if word[0].lower() in vowel and word[0].islower():  
            first_letter = 'w'
            body_letters = word
        # check for uppercase vowel
        elif word[0].lower() in vowel and word[0].isupper():  
            first_letter = 'w'
            body_letters = word
        # wh, th, kn phonetic exceptions are kept together
        elif word[:2].lower() == 'wh' or word[:2].lower() == 'th' or word[:2].lower() == 'kn':  
            first_letter = word[:2]
            body_letters = word[2:]
        # sch phonetic exception kept together
        elif word[:3].lower() == 'sch':  
            first_letter = word[:3]
            body_letters = word[3:]
        # default
        else:
            first_letter = word[0]
            body_letters = word[1:]
        return f"{body_letters}-{first_letter}ay"
    else:
        return word  # don't pig latinize number or special character

def solution(phrase):
    """
    Takes a phrase, breaks it into words and passes those words to generate_pig_latin_word()
    :param phrase: str - a phrase, often with spaces and special characters
    :return: str - pig latin-ized string
    
    """
    pig_latin_builder = ''

    word = ''
    break_characters = '0123456789 !?@#$%^&*((){},.'
    for ch in phrase:
        if ch in break_characters and word != '':
            pig_latin_builder += generate_pig_latin_word(word)
            word = ''
        if ch in break_characters and word == '':
            pig_latin_builder += ch
        else:
            word += ch
    if word != '':
        pig_latin_builder += generate_pig_latin_word(word)  # add the last word that doesn't benefit from the space to inform new word
    return pig_latin_builder

if __name__ == '__main__':
    print(solution("Pig Latin is used t in schools to teach language constructs. It's helpful for people to learn new things!"))
